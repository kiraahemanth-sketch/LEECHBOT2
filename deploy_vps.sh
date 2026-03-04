#!/bin/bash

echo "🚀 Starting ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Bot Auto-Deployment..."

# Update and upgrade system
echo "📦 Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install dependencies
echo "🛠 Installing system-level dependencies..."
sudo apt install -y python3 python3-pip python3-venv ffmpeg git libmagic-dev \
                    aria2 qbittorrent-nox 7zip curl screen lsof rclone

# Install Python dependencies
echo "🐍 Installing Python dependencies..."
# It's better to use a virtual environment
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Create necessary directories
mkdir -p downloads thumbnails tokens rclone watermarks accounts

echo "--------------------------------------------------"
echo "👑 ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡👑 Deployment Setup Successful!"
echo "Owner: @alonekingstar77"
echo ""
echo "Next Steps:"
echo "1. Edit 'config.py' with your bot credentials and settings."
echo "2. Start the bot with: source venv/bin/activate && python3 -m bot"
echo "3. Alternatively, use the systemd service (see README.md)."
echo "--------------------------------------------------"
