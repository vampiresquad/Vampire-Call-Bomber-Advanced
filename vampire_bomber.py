#!/usr/bin/env python3
import os
import sys
import time
import getpass
import requests

# --------- Color Codes ---------
R = '\033[91m'  # Red
G = '\033[92m'  # Green
Y = '\033[93m'  # Yellow
B = '\033[94m'  # Blue
C = '\033[96m'  # Cyan
N = '\033[0m'   # Reset

# --------- Settings ---------
CORRECT_PASSWORD = "SH404X"
API_URL = "https://call-bombers.vercel.app/send-call"

# --------- Functions ---------
def clear(): os.system("clear" if os.name == "posix" else "cls")

def slow(text, delay=0.04):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    clear()
    print(f"""{R}
██╗   ██╗ █████╗ ███╗   ███╗██████╗ ██╗██████╗ ███████╗
╚██╗ ██╔╝██╔══██╗████╗ ████║██╔══██╗██║██╔══██╗██╔════╝
 ╚████╔╝ ███████║██╔████╔██║██████╔╝██║██║  ██║█████╗  
  ╚██╔╝  ██╔══██║██║╚██╔╝██║██╔═══╝ ██║██║  ██║██╔══╝  
   ██║   ██║  ██║██║ ╚═╝ ██║██║     ██║██████╔╝███████╗
   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚══════╝
         {Y}☠ CALL BOMBER — BY VAMPIRE SQUAD ☠{N}
""")

def disclaimer():
    slow(f"{C}⚠ DISCLAIMER ⚠{N}", 0.03)
    slow(f"{Y}This tool is for educational and authorized use only.", 0.03)
    slow(f"{Y}Misuse is strictly prohibited. Use responsibly.", 0.03)
    slow(f"{G}Author: Muhammad Shourov (VAMPIRE)", 0.03)
    slow(f"{G}Team  : Vampire Squad 🩸", 0.03)
    input(f"\n{B}Press ENTER to continue...{N}")

def password_prompt():
    clear()
    print(f"{B}🔒 This tool is protected. Enter the password to continue.{N}")
    for attempt in range(3):
        pwd = getpass.getpass(f"{Y}🔑 Password: {N}")
        if pwd == CORRECT_PASSWORD:
            print(f"{G}✅ Access Granted!{N}")
            return
        else:
            print(f"{R}❌ Incorrect Password! Try again...{N}")
    print(f"{R}🔒 Access Denied. Exiting...{N}")
    sys.exit(1)

def main_menu():
    while True:
        clear()
        banner()
        print(f"""
{G}1. Start Call Bombing
2. About Tool
3. Exit
{N}""")
        choice = input(f"{Y}[?] Select an option: {N}")
        if choice == "1":
            start_bombing()
        elif choice == "2":
            about()
        elif choice == "3":
            print(f"{C}Goodbye, Vampire! Stay Legal 🩸{N}")
            break
        else:
            print(f"{R}Invalid choice!{N}")
            time.sleep(1)

def about():
    clear()
    banner()
    slow(f"{G}Tool Name : Vampire Call Bomber", 0.02)
    slow(f"{G}Version   : 1.0", 0.02)
    slow(f"{G}Author    : Muhammad Shourov", 0.02)
    slow(f"{G}Team      : Vampire Squad 🩸", 0.02)
    slow(f"{Y}API Used  : Gift By DH Alamin{N}", 0.02)
    input(f"\n{B}Press ENTER to go back...{N}")

def start_bombing():
    clear()
    banner()
    number = input(f"{C}[•] Victim's Number (without +88): {N}")
    limit = input(f"{C}[•] Number of Calls to Send     : {N}")
    key = "Gift By DH Alamin"

    url = f"{API_URL}?key={key}&number={number}&repeat={limit}"

    try:
        slow(f"{Y}[✓] Sending requests to API...{N}", 0.03)
        res = requests.get(url)
        if res.status_code == 200:
            print(f"{G}[✓] Response: {res.text}{N}")
        else:
            print(f"{R}[!] Failed! Status Code: {res.status_code}{N}")
    except Exception as e:
        print(f"{R}[!] Error: {str(e)}{N}")

    input(f"\n{B}Press ENTER to return to menu...{N}")

# --------- Execution ---------
if __name__ == "__main__":
    password_prompt()
    banner()
    disclaimer()
    main_menu()
