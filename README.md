<p align="center">
    <a href="https://t.me/ALONEKINGSTAR77">
        <kbd>
            <img width="250" src="https://graph.org/file/639fe4239b78e5862b302.jpg" alt="⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Logo">
        </kbd>
    </a>
</p>

<h1 align="center">⚡ ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Mirror-Leech Bot ⚡</h1>

<p align="center">
<i>A powerful, feature-rich Mirror-Leech Telegram Bot. Optimized for VPS and production deployments.</i>
</p>

---

## 🌟 Features

- **Smart Track Remover**: Selectively remove audio/subtitle tracks with `/audio`.
- **Smart Auto Extract**: Auto extraction of `.zip`, `.rar`, and `.7z` archives.
- **Advanced Auto Merge**: Automatically merges multi-part videos using FFmpeg (concat).
- **Auto Split**: Automatic splitting of files over 4GB for Telegram (Leech).
- **Custom Metadata**: Apply custom metadata to processed files.
- **Advanced UI**: Premium 12-segment progress bar and interactive inline keyboards.
- **Fully Optimized**: Python 3.12+ with `uvloop` and async processing for maximum speed.
- **Multi-Cloud Support**: Integrated support for GDrive, Rclone, and popular DDL hosts.

---

## 🚀 VPS Deployment Guide

### Prerequisites
- A VPS running **Ubuntu 20.04+** or **Debian 10+**.
- Basic knowledge of Linux command line.
- Python 3.10+ installed.

### Step-by-Step Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kiraahemanth-sketch/LEECHBOT2 mirrorbot && cd mirrorbot
   ```

2. **Run the deployment script**:
   ```bash
   bash deploy_vps.sh
   ```
   *This script installs all system dependencies (ffmpeg, aria2, qbittorrent-nox, etc.) and sets up a Python virtual environment.*

3. **Configure the bot**:
   - Open `config.py` with your favorite text editor (e.g., `nano config.py`).
   - Fill in the required variables: `BOT_TOKEN`, `OWNER_ID`, `TELEGRAM_API`, `TELEGRAM_HASH`, and `DATABASE_URL`.

4. **Start the bot**:
   - Activate the virtual environment: `source venv/bin/activate`
   - Run the bot: `python3 -m bot`

### 🛡️ Set up as a System Service (Recommended)

To ensure the bot auto-restarts on failure or server reboot:

1. Copy the provided service file:
   ```bash
   sudo cp hemanth-bot.service /etc/systemd/system/hemanth-bot.service
   ```
   *Note: Ensure the `WorkingDirectory` and `ExecStart` paths in the service file match your actual installation path.*

2. Enable and start the service:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable hemanth-bot
   sudo systemctl start hemanth-bot
   ```

---

## ⚙️ Configuration (config.py)

| Variable | Description |
| :--- | :--- |
| `BOT_TOKEN` | Your Telegram Bot Token from @BotFather |
| `OWNER_ID` | Your Telegram User ID |
| `TELEGRAM_API` | Telegram API ID from my.telegram.org |
| `TELEGRAM_HASH` | Telegram API Hash from my.telegram.org |
| `DATABASE_URL` | MongoDB Connection String |
| `AUTHORIZED_CHATS` | Space separated Chat IDs allowed to use the bot |
| `LEECH_DUMP_CHAT` | Chat ID where leeched files will be dumped |

---

## 🏅 Bot Authors

- [HEMANTH](https://github.com/kiraahemanth-sketch)
- [alonekingstar77](https://github.com/alonekingstar77)
- [RjRiajul](https://github.com/rjriajul)

---

## 📢 Support & Updates

- **Channel**: [⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Updates](https://t.me/ALONEKINGSTAR77)
- **Support**: [@alonekingstar77](https://t.me/ALONEKINGSTAR77)
