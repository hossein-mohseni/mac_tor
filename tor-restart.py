import time
from os import system
import os
import sys
import requests
from colorama import Fore, Style, Back
from colorama import init
init(autoreset=True)

system('clear')
def main():
    print(Fore.YELLOW + Style.BRIGHT + " ----------------------------------------------------------------------------------------------------------------------------------------------- ")
    print(Fore.YELLOW + Style.BRIGHT + "|" + Back.WHITE + "                                                                                                                                              " + Fore.YELLOW + Style.BRIGHT + Back.BLACK + "|")
    print(Fore.YELLOW + Style.BRIGHT + "|" + Back.WHITE + "                                                                                                                                              " + Fore.YELLOW + Style.BRIGHT + Back.BLACK + "|")
    print(Fore.YELLOW + Style.BRIGHT + "|" + Back.WHITE + "         " + Fore.MAGENTA + Style.BRIGHT + Back.WHITE + "   ▄████████    ▄████████  ▄████████ ███    █▄     ▄████████  ▄█      ███     ▄██   ▄           ▄█    █▄      ▄▄▄▄███▄▄▄▄  " + Back.WHITE + "          " + Fore.YELLOW + Style.BRIGHT + Back.BLACK + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|" + Back.WHITE + "         " + Fore.MAGENTA + Style.BRIGHT + Back.WHITE + "  ███    ███   ███    ███ ███    ███ ███    ███   ███    ███ ███  ▀█████████▄ ███   ██▄        ███    ███   ▄██▀▀▀███▀▀▀██▄" + Back.WHITE + "          " + Fore.YELLOW + Style.BRIGHT + Back.BLACK + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|" + Back.WHITE + "         " + Fore.MAGENTA + Style.BRIGHT + Back.WHITE + "  ███    █▀    ███    █▀  ███    █▀  ███    ███   ███    ███ ███▌    ▀███▀▀██ ███▄▄▄███        ███    ███   ███   ███   ███" + Back.WHITE + "          " + Fore.YELLOW + Style.BRIGHT + Back.BLACK + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|" + Back.WHITE + "         " + Fore.MAGENTA + Style.BRIGHT + Back.WHITE + "  ███         ▄███▄▄▄     ███        ███    ███  ▄███▄▄▄▄██▀ ███▌     ███   ▀ ▀▀▀▀▀▀███       ▄███▄▄▄▄███▄▄ ███   ███   ███" + Back.WHITE + "          " + Fore.YELLOW + Style.BRIGHT + Back.BLACK + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|" + Back.WHITE + "         " + Fore.MAGENTA + Style.BRIGHT + Back.WHITE + "▀███████████ ▀▀███▀▀▀     ███        ███    ███ ▀▀███▀▀▀▀▀   ███▌     ███     ▄██   ███      ▀▀███▀▀▀▀███▀  ███   ███   ███" + Back.WHITE + "          " + Fore.YELLOW + Style.BRIGHT + Back.BLACK + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|" + Back.WHITE + "         " + Fore.MAGENTA + Style.BRIGHT + Back.WHITE + "         ███   ███    █▄  ███    █▄  ███    ███ ▀███████████ ███      ███     ███   ███        ███    ███   ███   ███   ███" + Back.WHITE + "          " + Fore.YELLOW + Style.BRIGHT + Back.BLACK + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|" + Back.WHITE + "         " + Fore.MAGENTA + Style.BRIGHT + Back.WHITE + "   ▄█    ███   ███    ███ ███    ███ ███    ███   ███    ███ ███      ███     ███   ███        ███    ███   ███   ███   ███" + Back.WHITE + "          " + Fore.YELLOW + Style.BRIGHT + Back.BLACK + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|" + Back.WHITE + "         " + Fore.MAGENTA + Style.BRIGHT + Back.WHITE + " ▄████████▀    ██████████ ████████▀  ████████▀    ███    ███ █▀      ▄████▀    ▀█████▀         ███    █▀     ▀█   ███   █▀ " + Back.WHITE + "          " + Fore.YELLOW + Style.BRIGHT + Back.BLACK + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|" + Back.WHITE + "         " + Fore.MAGENTA + Style.BRIGHT + Back.WHITE + "                                                  ███    ███                                                               " + Back.WHITE + "          " + Fore.YELLOW + Style.BRIGHT + Back.BLACK + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|______________________________________________________________________________________________________________________________________________|")
    print(Fore.YELLOW + Style.BRIGHT + "|" + Fore.RED + Style.BRIGHT + Back.WHITE + "                                                                    " + Fore.MAGENTA + Style.BRIGHT + Back.WHITE + "v1.08" + Back.WHITE + "                                                                     " + Fore.YELLOW + Style.BRIGHT + Back.BLACK + "|")
    print(Fore.YELLOW + Style.BRIGHT + " ----------------------------------------------------------------------------------------------------------------------------------------------- ")

while 1 == 1:    
  main()
  time.sleep(1)
  system('clear')
  main()
  print(Fore.YELLOW + Style.BRIGHT + "                                                                                                ")
  print(Fore.YELLOW + Style.BRIGHT + "                                                         <<======chose a method======>>                                ")
  print(" ")
  print(Fore.BLUE + Style.BRIGHT + "1) start")
  print(Fore.RED + Style.BRIGHT + "2) Exit")
  break

L = int(input(Fore.YELLOW + Style.BRIGHT + "+++>"))
system('clear')
if L == 1:
   try:
     main()
     response = requests.get('https://www.google.com/')
     if response.status_code == 200:
        system('clear')
        main()
        print("\n")
        print(Fore.GREEN + Style.BRIGHT + "WIFI / eth is connected :)")
        time.sleep(2)
        system('clear')
   except:
       system('clear')
       print("\n")
       main()
       print(Fore.RED + Style.BRIGHT + '[ERROR!] No WIFI / eth Connection')
       time.sleep(2)
       system('clear')
       system('exit')
   else:
       system('clear')
       main()
       print("\n")
       print(Fore.YELLOW + Style.BRIGHT + "your mac Addres will be changed in few second . . ." )
       time.sleep(2)
       system('clear')
       main()
       print("\n")
       print(Fore.CYAN + Style.BRIGHT + "your mac Addres will be changed in few second . . ." )
       time.sleep(2)
       system('clear')
       main()
       print("\n")
       print(Fore.GREEN + Style.BRIGHT + "your mac Addres has been changed :) " )
       time.sleep(2)
       system('clear')
       main() 
       print("\n")
       print(Fore.MAGENTA + Style.BRIGHT + "\t")
       print(Fore.MAGENTA + Style.BRIGHT + "your new MAC Addres is:")
       print(" ")
       system('sudo macchanger -r wlan0')
       system('sudo macchanger -r eth0')
       time.sleep(4)
       system('clear')
       system('python3.9 loop.py')
if L == 2:
   system('clear')
   system('exit')
