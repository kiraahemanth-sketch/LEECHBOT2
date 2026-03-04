import asyncio
import sys
import logging
import traceback
from datetime import datetime
from logging import Formatter
from time import localtime
from pytz import timezone

import bot
from bot import LOGGER, scheduler, start_qbittorrent
from bot.core.config_manager import Config
from bot.core.tg_client import TgClient

# Global Exception Handler
def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    error_msg = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    LOGGER.error(f"Uncaught Exception: {error_msg}")

    # If LOG_CHANNEL is set, try to send the error there
    if Config.LOG_CHANNEL and TgClient.bot and TgClient.bot.is_connected:
        try:
            asyncio.create_task(TgClient.bot.send_message(Config.LOG_CHANNEL, f"<b>Uncaught Exception:</b>\n<code>{error_msg[:4000]}</code>"))
        except Exception:
            pass

sys.excepthook = handle_exception

# Async global exception handler
def async_exception_handler(loop, context):
    msg = context.get("exception", context["message"])
    LOGGER.error(f"Async Task Error: {msg}")
    if Config.LOG_CHANNEL and TgClient.bot and TgClient.bot.is_connected:
        try:
            asyncio.create_task(TgClient.bot.send_message(Config.LOG_CHANNEL, f"<b>Async Task Error:</b>\n<code>{msg}</code>"))
        except Exception:
            pass

async def main():
    loop = asyncio.get_running_loop()
    loop.set_exception_handler(async_exception_handler)
    bot.bot_loop = loop  # Share the loop with the bot package

    # Load and validate config
    Config.load()

    # Start bot first to get TgClient.ID
    await TgClient.start_bot()

    from bot.core.startup import (
        load_configurations,
        load_settings,
        save_settings,
        update_aria2_options,
        update_nzb_options,
        update_qb_options,
        update_variables,
    )

    await load_settings()

    try:
        tz = timezone(Config.TIMEZONE)
    except Exception:
        from pytz import utc
        tz = utc

    def changetz(*args):
        try:
            return datetime.now(tz).timetuple()
        except Exception:
            return localtime()

    Formatter.converter = changetz

    # Start other Services
    await start_qbittorrent()

    await asyncio.gather(
        TgClient.start_user(),
        TgClient.start_helper_bots()
    )

    await asyncio.gather(load_configurations(), update_variables())

    from bot.core.torrent_manager import TorrentManager
    await TorrentManager.initiate()

    await asyncio.gather(
        update_qb_options(),
        update_aria2_options(),
        update_nzb_options(),
    )

    from bot.core.jdownloader_booter import jdownloader
    from bot.helper.ext_utils.files_utils import clean_all
    from bot.helper.ext_utils.telegraph_helper import telegraph
    from bot.helper.mirror_leech_utils.rclone_utils.serve import rclone_serve_booter
    from bot.modules import (
        get_packages_version,
        initiate_search_tools,
        restart_notification,
    )

    await asyncio.gather(
        save_settings(),
        jdownloader.boot(),
        clean_all(),
        initiate_search_tools(),
        get_packages_version(),
        restart_notification(),
        telegraph.create_account(),
        rclone_serve_booter(),
    )

    # Register Handlers and setup plugins
    from bot.core.handlers import add_handlers
    from bot.helper.ext_utils.bot_utils import create_help_buttons
    from bot.helper.listeners.aria2_listener import add_aria2_callbacks
    from bot.core.plugin_manager import get_plugin_manager
    from bot.modules.plugin_manager import register_plugin_commands

    add_aria2_callbacks()
    create_help_buttons()
    add_handlers()

    plugin_manager = get_plugin_manager()
    plugin_manager.bot = TgClient.bot
    register_plugin_commands()

    # Restart sessions confirm handler
    from pyrogram.handlers import CallbackQueryHandler
    from pyrogram.filters import regex
    from bot.helper.telegram_helper.filters import CustomFilters
    from bot.helper.ext_utils.bot_utils import new_task
    from bot.helper.telegram_helper.message_utils import send_message, edit_message, delete_message

    @new_task
    async def restart_sessions_confirm(_, query):
        data = query.data.split()
        message = query.message
        if data[1] == "confirm":
            reply_to = message.reply_to_message
            restart_message = await send_message(reply_to, "Restarting Session(s)...")
            await delete_message(message)
            await TgClient.reload()
            add_handlers()
            TgClient.bot.add_handler(
                CallbackQueryHandler(
                    restart_sessions_confirm,
                    filters=regex("^sessionrestart") & CustomFilters.sudo,
                )
            )
            await edit_message(restart_message, "Session(s) Restarted Successfully!")
        else:
            await delete_message(message)

    TgClient.bot.add_handler(
        CallbackQueryHandler(
            restart_sessions_confirm,
            filters=regex("^sessionrestart") & CustomFilters.sudo,
        )
    )

    scheduler.start()
    LOGGER.info("Bot started successfully on VPS")

    # Keep the bot running
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        LOGGER.info("Bot stopped by user.")
    except Exception:
        LOGGER.critical(f"Startup Failure: {traceback.format_exc()}")
