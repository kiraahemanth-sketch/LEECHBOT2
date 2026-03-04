# ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Mirror-Leech Bot

A comprehensive and optimized Telegram bot for mirroring and leeching files, now refactored for 100% deployment success on VPS.

## 🚀 Features

- **Mirroring:** Mirror files to Google Drive, Rclone supported clouds, and more.
- **Leeching:** Download files and upload them to Telegram as documents or media.
- **Multi-Service Support:** Supports qBittorrent, Aria2, SABnzbd, JDownloader, and yt-dlp.
- **Async Execution:** Fully asynchronous for high performance and responsiveness.
- **Global Error Handling:** Robust system to catch and log errors in both main loop and async tasks.
- **Single Config System:** Easy management with a single `config.py` file.
- **VPS Ready:** Tailored for seamless deployment on Linux servers.

## 🛠 VPS Installation Guide

Follow these steps for a clean installation on your VPS (Ubuntu 20+/Debian recommended).

### 1. Update and Install System Dependencies
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git aria2 qbittorrent-nox ffmpeg p7zip-full rclone -y
```

### 2. Clone the Repository
```bash
git clone <your-repo-url>
cd <repo-folder>
```

### 3. Install Python Dependencies
```bash
pip3 install -r requirements.txt
```

### 4. Configure the Bot
- Open `config.py` with your preferred editor (e.g., `nano`).
- Fill in the required variables (API_ID, API_HASH, BOT_TOKEN, DATABASE_URI, ADMIN).
```bash
nano config.py
```

### 5. Start the Bot
```bash
python3 main.py
```

## ⚙️ Configuration Explanation

The `config.py` file contains all the settings for your bot. Mandatory variables are:

| Variable | Description |
|----------|-------------|
| `API_ID` | Your Telegram API ID from my.telegram.org |
| `API_HASH` | Your Telegram API Hash from my.telegram.org |
| `BOT_TOKEN` | Your Bot Token from @BotFather |
| `DATABASE_URI` | MongoDB Connection String |
| `ADMIN` | Your Telegram User ID (Owner) |

Optional variables like `SESSION`, `LOG_CHANNEL`, and others can be configured for advanced features.

## ❗ Troubleshooting

### Common Errors & Fixes

- **`ValueError: Critical configuration variables are missing`**: Ensure all mandatory variables in `config.py` are filled correctly.
- **`ModuleNotFoundError`**: Ensure you ran `pip3 install -r requirements.txt`.
- **Bot doesn't respond to `/start`**: Verify `BOT_TOKEN` is correct and the bot has necessary permissions in the chat.
- **Startup Failure**: Check `log.txt` for detailed error messages.

### VPS Recommendations
- **Minimum RAM:** 2GB
- **CPU:** 1 Core or more
- **Storage:** Dependent on your download/upload volume.

## 📄 License
This project is licensed under the MIT License.
