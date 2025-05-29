#!/usr/bin/env python3
# Vampire Call Bomber (Advanced Edition)
# Author: Muhammad Shourov (VAMPIRE) 🧛
# Team: Vampire Squad

import os
import time
import requests
import getpass
from sys import exit

# Colors
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
B = '\033[1;34m'
C = '\033[1;36m'
W = '\033[1;37m'
N = '\033[0m'

CORRECT_PASSWORD = "SH404"

# Banner
def show_banner():
    os.system("clear")
    if os.path.exists("logo.txt"):
        with open("logo.txt", "r") as f:
            print(G + f.read() + N)
    else:
        print(G + "[ Vampire Call Bomber ]" + N)
    print(f"{Y}Team: {W}Vampire Squad")
    print(f"{Y}Author: {W}Muhammad Shourov (VAMPIRE)\n")

# Password protect
def ask_password():
    print(f"{C}🔐 This tool is password protected by Vampire Squad.")
    pw = getpass.getpass(f"{B}Enter password to continue: {N}")
    if pw != CORRECT_PASSWORD:
        print(f"{R}✖ Incorrect password! Exiting...{N}")
        exit()
    else:
        print(f"{G}✔ Access Granted!{N}")
        time.sleep(1)

# Disclaimer
def disclaimer():
    print(f"{Y}⚠️  This tool is for educational and ethical testing only.")
    print(f"{Y}❌ Unauthorized misuse is prohibited.")
    print(f"{Y}✅ Use only on your own number or with permission.\n")
    input(f"{B}Press ENTER to continue...{N}")

# Call API
def call_bomb(number, repeat):
    url = "https://call-bombers.vercel.app/send-call"
    params = {
        "key": "Gift By DH Alamin",
        "number": number,
        "repeat": repeat
    }

    try:
        print(f"{B}[•] Sending {repeat} call(s) to {number}...{N}")
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            print(f"{G}[✓] Success: Calls sent successfully!{N}")
        else:
            print(f"{R}[×] Failed: Status Code {response.status_code}{N}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{N}")

# Main Menu
def menu():
    while True:
        print(f"""
{C}📱 MENU:
{G}[1]{W} Start Call Bombing
{G}[2]{W} Tool Info
{G}[3]{W} Disclaimer
{G}[4]{W} Exit
""")
        choice = input(f"{Y}Choose an option: {N}")
        if choice == "1":
            number = input(f"{C}[?] Enter target number: {N}")
            if not number.isdigit() or len(number) < 10:
                print(f"{R}[×] Invalid number format!{N}")
                continue
            repeat = input(f"{C}[?] Number of calls to send: {N}")
            if not repeat.isdigit() or int(repeat) <= 0:
                print(f"{R}[×] Invalid repeat count!{N}")
                continue
            call_bomb(number, repeat)
        elif choice == "2":
            print(f"""{G}
Tool Name : Vampire Call Bomber
Version   : 2.0 [Advanced]
Author    : Muhammad Shourov (VAMPIRE)
Team      : Vampire Squad 🩸
API Used  : DH Alamin Gifted API
Purpose   : Education / Ethical Hacking only
{N}""")
        elif choice == "3":
            disclaimer()
        elif choice == "4":
            print(f"{C}Thank you for using Vampire Call Bomber. Goodbye!{N}")
            exit()
        else:
            print(f"{R}[×] Invalid option! Try again.{N}")

# Main
def main():
    show_banner()
    ask_password()
    disclaimer()
    menu()

if __name__ == "__main__":
    main()
