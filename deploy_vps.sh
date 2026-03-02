#!/bin/bash

echo "🚀 Starting ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Bot Auto-Deployment..."

# Fix for common Docker errors on VPS
fix_docker_error() {
    if command -v pip3 &> /dev/null; then
        echo "🔧 Fixing Docker API compatibility issues..."
        pip3 install "urllib3<2.0.0" --upgrade &> /dev/null
    fi
}

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

    # Install Docker if missing
    if ! command -v docker &> /dev/null; then
        echo "🐳 Installing Docker..."
        curl -fsSL https://get.docker.com -o get-docker.sh
        sh get-docker.sh
    fi

    # Fix the specific error: Not supported URL scheme http+docker
    fix_docker_error

    # Install/Upgrade Docker Compose to V2 (plugin)
    echo "🐳 Setting up Docker Compose V2..."
    sudo apt-get update
    sudo apt-get install docker-compose-plugin -y

    # Ensure uv is installed for fast dependency management
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
    echo "To run with Docker: docker compose up -d"
    echo "To run in background: screen -dmS hemanth python3 -m bot"
fi
echo "--------------------------------------------------"
