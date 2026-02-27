<p align="center">
    <a href="https://t.me/ALONEKINGSTAR77">
        <kbd>
            <img width="250" src="https://graph.org/file/639fe4239b78e5862b302.jpg" alt="⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Logo">
        </kbd>
    </a>
</p>

<h1 align="center">⚡ ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ ⚡</h1>

<p align="center">
<i>The Ultimate Advanced Mirror-Leech Telegram Bot. Fully Optimized, Feature-Rich, and Production-Ready.</i>
</p>

---

## 🌟 Premium Features

- **🎯 Smart Track Remover System**: Advanced `/audio` command to selectively remove audio and subtitle tracks with an interactive UI. High speed via stream copying.
- **📦 Smart Auto Extract**: Automatically detects and extracts `.zip`, `.rar`, and `.7z` files upon download.
- **🔗 Advanced Auto Merge**: Toggle with `/merge`. Automatically merges multi-part video files (.001, .part1, etc.) using FFmpeg concat without re-encoding.
- **✂️ Auto Split**: Seamlessly splits files larger than 4GB into 3.9GB parts for standard Telegram uploads.
- **🏷️ Global Metadata**: Apply custom metadata (Title, Artist, Album, etc.) globally to all processed files.
- **🛠️ Interactive Force Tools**: Use the `-ft` flag to trigger an interactive menu for Screenshot Grids, Watermarking, Encoding, and more mid-task.
- **📸 Screenshot Grid & PDF**: Generate high-quality tiled screenshot grids with optional automatic PDF conversion and export.
- **🖼️ Custom Watermarking**: Upload your own `.png` watermark via `/us` and overlay it on videos with optimized speed.
- **🚀 Ultra High Speed**:
  - **uvloop Integration**: Lightning-fast asynchronous execution.
  - **Optimized FFmpeg**: Uses `ultrafast` presets for all encoding/processing tasks.
  - **Dynamic Threading**: Auto-scaling thread pool for low-RAM (1-2GB) VPS environments.
  - **High Concurrency**: Supports up to 200 concurrent Telegram transmissions.
- **🎨 Premium UI**: Colorful interactive buttons, randomized styles, and 12-segment round-circle progress bars.
- **☁️ Multi-Cloud Support**: Integrated GDrive (Service Accounts/Token), Rclone (Custom Configs), and DDL Hosters (Gofile, BuzzHeavier, PixelDrain).

---

## 🎧 Smart Track Remover (/audio)
**How it works:**
1. Reply to any MKV/MP4/MOV file or link with `/audio`.
2. Bot scans and displays all available Audio (Language/Codec) and Subtitle tracks.
3. Toggle tracks with ✅/❌ to keep or remove them.
4. Press **🚀 Encode & Send** to process. Bot uses **Stream Copy** for near-instant results.
5. Processed file is sent directly to your **Bot DM**.

---

## 🔄 Workflow Logic

1. **Download**: Bot fetches the content via Aria2, qBit, yt-dlp, or direct download.
2. **Smart Extract**: Unpacks archives if detected.
3. **Auto Merge**: Joins parts if `/merge` is active.
4. **Processing**: Applies Metadata, Watermarks, or Encoding based on user settings or `-ft` flag.
5. **Auto Split**: Ensures Telegram upload limits are respected.
6. **Upload**: Sends to Telegram (Leech) or mirrors to Cloud Storage.
7. **Cleanup**: Intelligent temporary file deletion to save disk space.

---

## ⚙️ Essential Commands

- `/us` | `/usetting`: Comprehensive User Settings (Metadata, Leech, Cloud, FF Tools).
- `/merge`: Quick toggle for Auto Merge feature.
- `/audio`: Trigger the Smart Track Remover UI.
- `/mirror` | `/m`: Mirror files to Cloud storage.
- `/leech` | `/l`: Leech files directly to Telegram.
- `/status` | `/s`: Check active tasks with detailed progress.
- `/stats` | `/st`: View Bot, OS, and System statistics.

---

## 🚀 Deployment

### 🧡 VPS / Linux (Master Deployer)
The most stable way to run the bot.
```bash
git clone https://github.com/kiraahemanth-sketch/LEECHBOT2 mirrorbot && cd mirrorbot && bash deploy_vps.sh
```
- Edit `config.py` or use environment variables.
- Run via Docker: `docker compose up -d`
- Run via Screen: `screen -dmS hemanth python3 -m bot`

### 💙 Cloud Platforms
| Platform | Deploy Button |
| :--- | :--- |
| **Heroku** | [![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/kiraahemanth-sketch/LEECHBOT2) |
| **Koyeb** | [![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=kiraahemanth-sketch/LEECHBOT2&branch=master&name=hemanth-bot) |
| **Render** | [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/kiraahemanth-sketch/LEECHBOT2) |

---

## 🏅 Bot Authors
- [`HEMANTH`](https://github.com/kiraahemanth-sketch)
- [`alonekingstar77`](https://github.com/alonekingstar77)
- [`RjRiajul`](https://github.com/rjriajul)

## 📢 Support & Updates
- **Channel**: [⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Updates](https://t.me/ALONEKINGSTAR77)
- **Support**: [@alonekingstar77](https://t.me/ALONEKINGSTAR77)
