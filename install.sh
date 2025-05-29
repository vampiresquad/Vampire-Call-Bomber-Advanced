#!/bin/bash

# Colors
R='\033[0;31m'
G='\033[0;32m'
Y='\033[1;33m'
B='\033[0;34m'
N='\033[0m'

clear
echo -e "${B}
██╗   ██╗ █████╗ ███╗   ███╗██████╗ ██╗██████╗ ███████╗
╚██╗ ██╔╝██╔══██╗████╗ ████║██╔══██╗██║██╔══██╗██╔════╝
 ╚████╔╝ ███████║██╔████╔██║██████╔╝██║██║  ██║█████╗  
  ╚██╔╝  ██╔══██║██║╚██╔╝██║██╔═══╝ ██║██║  ██║██╔══╝  
   ██║   ██║  ██║██║ ╚═╝ ██║██║     ██║██████╔╝███████╗
   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚══════╝
        ${Y}Vampire Call Bomber Installer${N}
"

echo -e "${Y}[*] Updating packages...${N}"
pkg update -y && pkg upgrade -y

echo -e "${Y}[*] Installing Python, Git, and other requirements...${N}"
pkg install python -y
pkg install git -y
pip install --upgrade pip
pip install requests

echo -e "${G}[✓] Dependencies installed successfully!${N}"

echo -e "${Y}[*] Making script executable...${N}"
chmod +x vampire_bomber.py

echo -e "${G}[✓] Setup complete.${N}"
echo -e "${C}To run the tool, type: ${G}python3 vampire_bomber.py${N}"
