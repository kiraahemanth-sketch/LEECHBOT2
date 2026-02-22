<p align="center">
    <a href="https://t.me/ALONEKINGSTAR77">
        <kbd>
            <img width="250" src="https://graph.org/file/639fe4239b78e5862b302.jpg" alt="⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Logo">
        </kbd>
    </a>
</p>

<h1 align="center">⚡ ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ ⚡</h1>

<p align="center">
<i>An advanced, feature-rich Mirror-Leech Telegram Bot. Fully optimized and production-ready.</i>
</p>

---

## 🌟 Features

- **Smart Track Remover System**: Advanced `/audio` command to selectively remove audio and subtitle tracks from video files.
- **Smart Auto Extract**: Automatically extracts files ONLY if the filename or link contains `.zip`.
- **Advanced Auto Merge**: Toggle with `/merge`. Merges multiple video parts (.part1, .part2, .001, etc.) automatically using FFmpeg concat (no re-encode).
- **Auto Split**: Automatically splits files larger than 4GB into 3.9GB parts for seamless Telegram upload.
- **Global Metadata**: Apply custom metadata to your files after merging.
- **Advanced UI**: Premium colorful buttons, attractive inline keyboard, and round-circle progress bars for all stages.
- **Fully Optimized**: Async operations, low RAM usage, and automatic cleanup of temporary files.
- **Ultra High Speed**: Optimized FFmpeg presets (ultrafast), maximum concurrency, and uvloop integration for light-speed performance.
- **Multi-Cloud Support**: Support for GDrive, Rclone, and various DDL hosts.

---

## 🎧 Smart Track Remover (/audio)
How it works:
1. Reply to any media file (MKV, MP4, MOV) or direct link with `/audio`.
2. Bot downloads the file and scans it for all available tracks.
3. Interactive UI shows all Audio tracks (Language + Codec + Bitrate) and Subtitles.
4. Toggle tracks with ✅/❌ to keep or remove them.
5. Press **Encode & Send** to process. Bot uses stream copy where possible for maximum speed.
6. The processed file is sent directly to your **Bot DM**.

---

## 🔄 Workflow

1. **Download**: Bot downloads the requested link/file.
2. **Smart Extract**: If `.zip` is detected in the name/link, it extracts the content.
3. **Auto Merge**: If `/merge` is enabled, the bot detects video parts and merges them using FFmpeg `-c copy`.
4. **Metadata**: Applies user-defined metadata (if enabled via `/us`).
5. **Auto Split**: If the final result exceeds 4GB, it splits into 3.9GB parts.
6. **Upload**: Sends files to Telegram or mirrors them to cloud storage.
7. **Cleanup**: Automatically deletes zip files, parts, and temporary folders.

---

## ⚙️ Commands

- `/us`: User Settings (Metadata, Leech Settings, etc.)
- `/merge`: Toggle Auto Merge (Enabled/Disabled)
- `/audio`: Smart Track Remover UI
- `/mirror`: Mirror to Cloud
- `/leech`: Leech to Telegram
- `/status`: Check active tasks

---

## 🚀 Deployment Guides

### 💜 HEROKU DEPLOY

1. **Required Variables**:
   - `BOT_TOKEN`
   - `API_ID`
   - `API_HASH`
   - `MONGO_DB_URI`
   - `OWNER_ID`
   - `WEBHOOK_URL` (Optional)
2. **One-Click Deploy**:
   [![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/alonekingstar77/⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡)
3. **Worker Dyno**: After deployment, go to the Resources tab and enable the `worker` dyno.

### 💙 KOYEB DEPLOY

1. Use the provided `Dockerfile`.
2. Set the necessary environment variables in Koyeb Dashboard.
3. **Note**: Persistent storage is recommended for large downloads.

### 🖤 RENDER DEPLOY

1. Create a Web Service on Render.
2. Connect your GitHub repository.
3. Add the required Environment Variables.
4. Use `python3 -m bot` as the Start Command.

### 💚 RAILWAY DEPLOY

1. Connect your repository to Railway.app.
2. Add Environment Variables.
3. Railway will auto-detect the Dockerfile.

### 🧡 VPS DEPLOY (Ubuntu 22.04)

1. **Install FFmpeg and Python**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3 python3-pip ffmpeg -y
   ```
2. **Clone and Run**:
   ```bash
   git clone https://github.com/alonekingstar77/⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ mirrorbot/
   cd mirrorbot
   pip3 install -r requirements.txt
   bash start.sh
   ```
3. **One-Click Deploy**:
   ```bash
   bash <(curl -sL https://raw.githubusercontent.com/alonekingstar77/⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡/master/deploy_vps.sh)
   ```
4. **Keep Alive**: Use `screen` or `tmux` to keep the bot running. For auto-restart, use `systemd`.

### 📱 DareMote Mobile Deploy (Termux)

1. **Install Termux** from F-Droid.
2. **Run One-Click Script**:
   ```bash
   bash <(curl -sL https://raw.githubusercontent.com/alonekingstar77/⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡/master/deploy_vps.sh)
   ```
3. **Manual Install**:
   - `pkg update && pkg upgrade`
   - `pkg install python ffmpeg git`
   - `git clone https://github.com/alonekingstar77/⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡`
   - `cd ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ && pip install -r requirements.txt`
   - `bash start.sh`

---

## 🏅 **Bot Authors**

|[`alonekingstar77`](https://github.com/alonekingstar77)|[`RjRiajul`](https://github.com/rjriajul)|[`CodeWithWeeb`](https://github.com/weebzone)|
|:---:|:---:|:---:|

---

## 📢 Support & Channel

- **Channel**: [⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Updates](https://t.me/ALONEKINGSTAR77)
- **Support**: [@alonekingstar77](https://t.me/ALONEKINGSTAR77)
