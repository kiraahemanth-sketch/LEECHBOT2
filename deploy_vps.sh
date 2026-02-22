#!/bin/bash

# Update and install system dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip ffmpeg git libmagic-dev screen -y

# Install uv
pip3 install uv || pip install uv

# Install requirements
uv pip install --system -r requirements.txt || pip3 install -r requirements.txt

# Start command
echo "--------------------------------------------------"
echo "👑 ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡👑 VPS Deployment Successful!"
echo "Owner: @alonekingstar77"
echo "To start the bot, run: python3 -m bot"
echo "To run in background: screen -dmS wzml python3 -m bot"
echo "--------------------------------------------------"
