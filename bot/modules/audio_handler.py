from pyrogram.filters import command, regex
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ButtonStyle
from os import path as ospath
from asyncio import create_subprocess_exec, gather
from asyncio.subprocess import PIPE
import json

from bot import LOGGER, DOWNLOAD_DIR, task_dict, task_dict_lock, bot_loop
from bot.core.tg_client import TgClient
from bot.core.config_manager import Config, BinConfig
from bot.helper.ext_utils.bot_utils import new_task, sync_to_async, arg_parser
from bot.helper.ext_utils.media_utils import get_streams, FFMpeg
from bot.helper.ext_utils.status_utils import MirrorStatus, get_readable_file_size
from bot.helper.telegram_helper.message_utils import send_message, edit_message, delete_message, auto_delete_message
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.button_build import ButtonMaker
from bot.helper.listeners.task_listener import TaskListener
from bot.helper.mirror_leech_utils.status_utils.ffmpeg_status import FFmpegStatus
from bot.helper.ext_utils.files_utils import clean_target, get_path_size

audio_data = {}

class AudioProcess(TaskListener):
    def __init__(self, client, message, link=None):
        self.message = message
        self.client = client
        self.link = link
        super().__init__()
        self.is_leech = True
        self.as_doc = True
        self.new_path = ""
        self.streams = []
        self.selected_streams = []

    async def start(self):
        reply_to = self.message.reply_to_message
        file_path = None
        file_name = None
        file_size = 0

        if reply_to and (reply_to.document or reply_to.video or reply_to.audio):
            file = reply_to.document or reply_to.video or reply_to.audio
            if not file.file_name.lower().endswith((".mkv", ".mp4", ".mov")):
                await send_message(self.message, "Only MKV, MP4, and MOV files are supported!")
                return
            file_name = file.file_name
            file_size = file.file_size
            msg = await send_message(self.message, "📥 Downloading file for processing...")
            self.dir = ospath.join(DOWNLOAD_DIR, str(self.mid))
            try:
                file_path = await self.client.download_media(reply_to, file_name=ospath.join(self.dir, file_name))
            except Exception as e:
                await edit_message(msg, f"❌ Download failed: {e}")
                await clean_target(self.dir)
                return
        elif len(self.message.command) > 1:
            self.link = self.message.command[1]
            msg = await send_message(self.message, "📥 Downloading link for processing...")
            self.dir = ospath.join(DOWNLOAD_DIR, str(self.mid))
            # Use aria2c for link download
            cmd = [BinConfig.ARIA2_NAME, "-d", self.dir, "--allow-overwrite=true", self.link]
            process = await create_subprocess_exec(*cmd, stdout=PIPE, stderr=PIPE)
            stdout, stderr = await process.communicate()
            if process.returncode != 0:
                await edit_message(msg, f"❌ Download failed: {stderr.decode()}")
                await clean_target(self.dir)
                return
            # Find the downloaded file
            from os import listdir
            files = listdir(self.dir)
            if files:
                file_name = files[0]
                file_path = ospath.join(self.dir, file_name)
                file_size = await get_path_size(file_path)
            else:
                await edit_message(msg, "❌ Download failed: No file found.")
                await clean_target(self.dir)
                return
        else:
            await send_message(self.message, "Reply to a media file or provide a link!")
            return

        self.name = file_name
        self.size = file_size
        await self.show_streams(file_path, msg)

    async def show_streams(self, file_path, msg):
        self.streams = await get_streams(file_path)
        if not self.streams:
            await edit_message(msg, "Error: Could not extract streams from file!")
            await clean_target(self.dir)
            return

        self.selected_streams = [True] * len(self.streams) # Initially all selected

        audio_data[self.mid] = {
            "file_path": file_path,
            "streams": self.streams,
            "selected": self.selected_streams,
            "listener": self,
            "msg": msg
        }

        await self.update_stream_buttons(msg)

    async def update_stream_buttons(self, msg):
        data = audio_data.get(self.mid)
        if not data:
            return

        streams = data["streams"]
        selected = data["selected"]

        buttons = ButtonMaker()

        for i, stream in enumerate(streams):
            stype = stream.get("codec_type")
            if stype not in ["audio", "subtitle", "video"]:
                continue

            lang = stream.get("tags", {}).get("language", "und")
            codec = stream.get("codec_name", "unknown")
            index = stream.get("index")

            icon = "✅" if selected[i] else "❌"
            label = f"{icon} {stype.capitalize()}: {lang} - {codec}"

            if stype == "audio":
                bitrate = stream.get("bit_rate")
                if bitrate:
                    label += f" ({int(bitrate)//1000}kbps)"

            buttons.data_button(label, f"audio {self.mid} toggle {i}")

        buttons.data_button("🚀 Encode & Send", f"audio {self.mid} process", position="footer", style=ButtonStyle.SUCCESS)
        buttons.data_button("❌ Cancel", f"audio {self.mid} cancel", position="footer", style=ButtonStyle.DANGER)

        text = "🎯 <b><u>Smart Track Remover System</u></b>\n\n"
        text += f"<b>📁 File:</b> <code>{self.name}</code>\n"
        text += "━━━━━━━━━━━━━━━━━━━━━━━\n"
        text += "<i>Select the tracks you want to KEEP. Tracks marked with ❌ will be removed from the final file.</i>\n\n"
        text += "<b>Track List:</b>"

        await edit_message(msg, text, buttons.build_menu(1))

    async def process_file(self):
        data = audio_data.get(self.mid)
        if not data:
            return

        file_path = data["file_path"]
        streams = data["streams"]
        selected = data["selected"]
        msg = data["msg"]

        await edit_message(msg, "⚙️ Processing your request... Please wait.")

        map_args = []
        for i, is_selected in enumerate(selected):
            if is_selected:
                map_args.extend(["-map", f"0:{streams[i]['index']}"])

        if not map_args:
            # If nothing selected, keep at least video? Or error?
            # Actually user probably shouldn't do this.
            # Default to keep video if none selected?
            await edit_message(msg, "❌ Error: No tracks selected to keep!")
            return

        output_path = ospath.join(self.dir, f"PROCESSED_{self.name}")

        cmd = [
            BinConfig.FFMPEG_NAME,
            "-hide_banner",
            "-loglevel",
            "error",
            "-progress", "pipe:1",
            "-i", file_path
        ]
        cmd.extend(map_args)
        cmd.extend(["-c", "copy", "-map_metadata", "0", output_path, "-y"])

        ffmpeg = FFMpeg(self)
        async with task_dict_lock:
            task_dict[self.mid] = FFmpegStatus(self, ffmpeg, self.mid, "AudioProcess")

        self.subsize = await get_path_size(file_path)
        res = await ffmpeg.ffmpeg_cmds(cmd, file_path)

        if res:
            await edit_message(msg, "📤 Uploading processed file to your DM...")
            # Send to DM
            try:
                processed_file_size = await get_path_size(output_path)
                readable_size = get_readable_file_size(processed_file_size)
                await self.client.send_document(
                    chat_id=self.user_id,
                    document=output_path,
                    caption=f"<b>✅ Processed Successfully!</b>\n\n<b>📁 File:</b> <code>{self.name}</code>\n<b>💰 Size:</b> <code>{readable_size}</code>\n\n<b>Powered by ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡</b>",
                    file_name=self.name
                )
                await edit_message(msg, "<b>📩 Processed file has been sent to your DM.</b>")
            except Exception as e:
                LOGGER.error(f"Error sending file to DM: {e}")
                await edit_message(msg, f"❌ Error sending file to DM: {e}")
        else:
            await edit_message(msg, "❌ FFmpeg process failed!")

        await clean_target(self.dir)
        async with task_dict_lock:
            if self.mid in task_dict:
                del task_dict[self.mid]
        if self.mid in audio_data:
            del audio_data[self.mid]

@new_task
async def audio_handler(client, message):
    if not message.from_user:
        return

    if message.chat.type.name != "PRIVATE":
        await send_message(message, "📩 Check your DM to receive the processed file.")

    process = AudioProcess(client, message)
    await process.start()

@new_task
async def audio_callback(client, query):
    data = query.data.split()
    mid = int(data[1])
    action = data[2]

    if mid not in audio_data:
        await query.answer("Task expired or not found!", show_alert=True)
        return

    task_data = audio_data[mid]
    if query.from_user.id != task_data["listener"].user_id:
        await query.answer("Not your task!", show_alert=True)
        return

    if action == "toggle":
        idx = int(data[3])
        task_data["selected"][idx] = not task_data["selected"][idx]
        await task_data["listener"].update_stream_buttons(task_data["msg"])
        await query.answer()
    elif action == "process":
        await query.answer("Processing started...")
        bot_loop.create_task(task_data["listener"].process_file())
    elif action == "cancel":
        await task_data["listener"].on_upload_error("Process cancelled by user.")
        await clean_target(task_data["listener"].dir)
        await delete_message(task_data["msg"])
        if mid in audio_data:
            del audio_data[mid]
        await query.answer("Cancelled.")

# Registration will be done in handlers.py
