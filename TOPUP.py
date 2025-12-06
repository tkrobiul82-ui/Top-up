from os import system as c
import time
import random
import os

# Colors
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
P = '\x1b[38;5;201m'

def logo():
    c('clear')
    print(f"""{R}
██████╗ ██╗ ██████╗ 
██╔══██╗██║██╔════╝ 
██████╔╝██║██║  ███╗
██╔═══╝ ██║██║   ██║
██║     ██║╚██████╔╝
╚═╝     ╚═╝ ╚═════╝ 
{P} HACKING WORLD - ROOT DIAMOND VIP TOOL
""")

def check_
   
    time.sleep(2)
    if not os.path.exists("/system/xbin/su"):
        print(f"{R}[✓] ROOT ACCESS  FOUND!")
        
        
    else:
        print(f"{G}[✓] ROOT ACCESS GRANTED!\n")
        time.sleep(1)

def loading(task, sec):
    print(f"\n{C}[+] {task}...")
    for i in range(sec):
        print(f"{Y}[*] Loading{'.' * (i % 4)}")
        time.sleep(1)

def diamond_hack():
    logo()
    check_root()
    cookie = input(f"{C}ENTER YOUR FF COOKIE: ")
    loading("Verifying Cookie", 4)
    print(f"{G}[✓] Cookie Verified!\n")
    uid = input(f"{C}ENTER YOUR FREE FIRE UID: ")
    loading("Connecting to Garena VIP Server", 4)
    print(f"{G}[✓] UID Verified!\n")
    loading("Injecting 99999 Diamonds", 8)
    print(f"{Y}[!] Finalizing Process...")
    time.sleep(2)
    print(f"{G}[✓] 10000 Diamonds Successfully Added to UID: {uid}")
    print(f"{P}Enjoy your Diamonds VIP Boss 🔥🔥🔥\n")
    input(f"{A}Press Enter to Return to Menu...")
    menu()

def menu():
    logo()
    print(f"{A}[1] Start Unlimited Diamond Hack (ROOT ONLY)")
    print(f"{A}[0] Exit Tool")
    choice = input(f"{Y}Select Option: ")
    if choice == '1':
        diamond_hack()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] Invalid Option!")
        time.sleep(1)
        menu()

menu()