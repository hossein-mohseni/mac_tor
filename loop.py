import time
from os import system
from colorama import Fore, Style, Back
from colorama import init
init(autoreset=True)

system('clear')
def main3():
    print(Fore.YELLOW + Style.BRIGHT + " ---------------------------------------------------------------------------------------------- ")
    print(Fore.YELLOW + Style.BRIGHT + "|                                                                                              |")
    print(Fore.YELLOW + Style.BRIGHT + "|                                                                                              |")
    print(Fore.YELLOW + Style.BRIGHT + "|         " + Fore.MAGENTA + Style.BRIGHT + "▀█████████▄     ▄████████ ████████▄       ▀█████████▄   ▄██████▄  ▄██   ▄  " + Fore.YELLOW + Style.BRIGHT + "          |")
    print(Fore.YELLOW + Style.BRIGHT + "|         " + Fore.MAGENTA + Style.BRIGHT + "  ███    ███   ███    ███ ███   ▀███        ███    ███ ███    ███ ███   ██▄" + Fore.YELLOW + Style.BRIGHT + "          |")
    print(Fore.YELLOW + Style.BRIGHT + "|         " + Fore.MAGENTA + Style.BRIGHT + "  ███    ███   ███    ███ ███    ███        ███    ███ ███    ███ ███▄▄▄███" + Fore.YELLOW + Style.BRIGHT + "          |")
    print(Fore.YELLOW + Style.BRIGHT + "|         " + Fore.MAGENTA + Style.BRIGHT + " ▄███▄▄▄██▀    ███    ███ ███    ███       ▄███▄▄▄██▀  ███    ███ ▀▀▀▀▀▀███" + Fore.YELLOW + Style.BRIGHT + "          |")
    print(Fore.YELLOW + Style.BRIGHT + "|         " + Fore.MAGENTA + Style.BRIGHT + "▀▀███▀▀▀██▄  ▀███████████ ███    ███      ▀▀███▀▀▀██▄  ███    ███ ▄██   ███" + Fore.YELLOW + Style.BRIGHT + "          |")
    print(Fore.YELLOW + Style.BRIGHT + "|         " + Fore.MAGENTA + Style.BRIGHT + "  ███    ██▄   ███    ███ ███    ███        ███    ██▄ ███    ███ ███   ███" + Fore.YELLOW + Style.BRIGHT + "          |")
    print(Fore.YELLOW + Style.BRIGHT + "|         " + Fore.MAGENTA + Style.BRIGHT + "  ███    ███   ███    ███ ███   ▄███        ███    ███ ███    ███ ███   ███" + Fore.YELLOW + Style.BRIGHT + "          |")
    print(Fore.YELLOW + Style.BRIGHT + "|         " + Fore.MAGENTA + Style.BRIGHT + " ▄█████████▀   ███    █▀  ████████▀       ▄█████████▀   ▀██████▀   ▀█████▀ " + Fore.YELLOW + Style.BRIGHT + "          |")
    print(Fore.YELLOW + Style.BRIGHT + "|______________________________________________________________________________________________|")
    print(Fore.YELLOW + Style.BRIGHT + "|" + Fore.RED + Style.BRIGHT + Back.WHITE + "                                             " + Fore.BLUE + Style.BRIGHT + Back.WHITE + "v1.08" + Back.WHITE + "                                            " + Fore.YELLOW + Style.BRIGHT + Back.BLACK + "|")
    print(Fore.YELLOW + Style.BRIGHT + " ---------------------------------------------------------------------------------------------- ")

count = 0
for count in range(17, 0, -1):
    main3()
    print(Fore.YELLOW + Style.BRIGHT + "                                              [" + Fore.YELLOW + Style.BRIGHT + str(count) + "]")
    print(Fore.BLUE + Style.BRIGHT + "to cansel press: CTRL + C ")
    time.sleep(1)
    system('clear')
if count == 1:
    main3()
    print(Fore.BLUE + Style.BRIGHT + "to cansel press: CTRL + C ")
    time.sleep(1)

    system('clear')
    main3()
    system('sudo service tor restart')
    system('sudo service tor status')
    time.sleep(3)
    system('sudo python3.9 loop.py')
    
