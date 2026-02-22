#!/bin/bash

echo "🚀 Starting ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Bot Auto-Deployment..."

# Detect if we are in Termux
if [ -d "/data/data/com.termux/files/home" ]; then
    echo "📱 Termux environment detected!"
    pkg update && pkg upgrade -y
    pkg install python ffmpeg git libmagic -y
    pip install -r requirements.txt
else
    echo "💻 VPS/Linux environment detected!"
    sudo apt update && sudo apt upgrade -y
    sudo apt install python3 python3-pip ffmpeg git libmagic-dev screen -y
    pip3 install uv || pip install uv
    uv pip install --system -r requirements.txt || pip3 install -r requirements.txt
fi

echo "--------------------------------------------------"
echo "👑 ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡👑 Deployment Successful!"
echo "Owner: @alonekingstar77"
echo "Channel: https://t.me/ALONEKINGSTAR77"
echo ""
echo "To start the bot, run: python3 -m bot"
if [ ! -d "/data/data/com.termux/files/home" ]; then
    echo "To run in background (VPS): screen -dmS wzml python3 -m bot"
fi
echo "--------------------------------------------------"
