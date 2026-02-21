#!/bin/bash

echo "⚡ Starting ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ One-Click Deployment ⚡"

if [ -d "/data/data/com.termux/files/home" ]; then
    echo "📱 Detecting Termux environment..."
    pkg update && pkg upgrade -y
    pkg install python ffmpeg git -y
else
    echo "🖥 Detecting VPS/Linux environment..."
    sudo apt update && sudo apt upgrade -y
    sudo apt install python3 python3-pip ffmpeg git -y
fi

echo "📂 Cloning repository..."
git clone https://github.com/alonekingstar77/⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ mirrorbot
cd mirrorbot

echo "📦 Installing requirements..."
pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "🚀 Starting the Bot..."
bash start.sh
