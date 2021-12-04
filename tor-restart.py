import time
from os import system
import os
import sys
import requests
from colorama import Fore, Style, Back
from subprocess import *
import subprocess
import requests
from requests import sessions
from requests.sessions import session
from stem import Signal
from stem.control import Controller
from colored import fg 

system('clear')
def main():
    system('clear') 
    print(fg('#FF0000') + " --------------------------------------------------------------------------------- ")
    print(fg('#FF0000') + "|                                                                                 |")
    print(fg('#FF0000') + "|   " + fg("#FF7F00") + "▀█████████▄  " + fg("#FFFF00") + "   ▄████████ " + fg("#00FF00") + "████████▄      " + fg("#0000FF") + " ▀█████████▄  " + fg("#4B0082") + " ▄██████▄  " + fg("#9400D3") + "▄██   ▄   " + fg('#FF0000') + "  |")
    print(fg('#FF0000') + "|   " + fg("#FF7F00") + "  ███    ███ " + fg("#FFFF00") + "  ███    ███ " + fg("#00FF00") + "███   ▀███     " + fg("#0000FF") + "   ███    ███ " + fg("#4B0082") + "███    ███ " + fg("#9400D3") + "███   ██▄ " + fg('#FF0000') + "  |")
    print(fg('#FF0000') + "|   " + fg("#FF7F00") + "  ███    ███ " + fg("#FFFF00") + "  ███    ███ " + fg("#00FF00") + "███    ███     " + fg("#0000FF") + "   ███    ███ " + fg("#4B0082") + "███    ███ " + fg("#9400D3") + "███▄▄▄███ " + fg('#FF0000') + "  |")
    print(fg('#FF0000') + "|   " + fg("#FF7F00") + " ▄███▄▄▄██▀  " + fg("#FFFF00") + "  ███    ███ " + fg("#00FF00") + "███    ███     " + fg("#0000FF") + "  ▄███▄▄▄██▀  " + fg("#4B0082") + "███    ███ " + fg("#9400D3") + "▀▀▀▀▀▀███ " + fg('#FF0000') + "  |")
    print(fg('#FF0000') + "|   " + fg("#FF7F00") + "▀▀███▀▀▀██▄  " + fg("#FFFF00") + "▀███████████ " + fg("#00FF00") + "███    ███     " + fg("#0000FF") + " ▀▀███▀▀▀██▄  " + fg("#4B0082") + "███    ███ " + fg("#9400D3") + "▄██   ███ " + fg('#FF0000') + "  |")
    print(fg('#FF0000') + "|   " + fg("#FF7F00") + "  ███    ██▄ " + fg("#FFFF00") + "  ███    ███ " + fg("#00FF00") + "███    ███     " + fg("#0000FF") + "   ███    ██▄ " + fg("#4B0082") + "███    ███ " + fg("#9400D3") + "███   ███ " + fg('#FF0000') + "  |")
    print(fg('#FF0000') + "|   " + fg("#FF7F00") + "  ███    ███ " + fg("#FFFF00") + "  ███    ███ " + fg("#00FF00") + "███   ▄███     " + fg("#0000FF") + "   ███    ███ " + fg("#4B0082") + "███    ███ " + fg("#9400D3") + "███   ███ " + fg('#FF0000') + "  |")
    print(fg('#FF0000') + "|   " + fg("#FF7F00") + "▄█████████▀  " + fg("#FFFF00") + "  ███    █▀  " + fg("#00FF00") + "████████▀      " + fg("#0000FF") + " ▄█████████▀  " + fg("#4B0082") + " ▀██████▀  " + fg("#9400D3") + " ▀█████▀  " + fg('#FF0000') + "  |")
    print(fg('#FF0000') + "|_________________________________________________________________________________|")
    print(fg('#FF0000') + "|" + fg(220) + "Git: security-hm                  " + fg(57) + "Version Alpha" + fg(73) + "               tel: o_xBad_boyo_x" + fg('#FF0000') + " |")
    print(fg('#FF0000') + " --------------------------------------------------------------------------------- ")


oss = subprocess.check_output(['uname', '-o']).strip().decode('utf-8')
if oss == "GNU/Linux":
   main()
   print(Fore.YELLOW + Style.BRIGHT + "\n                           <<======choose a method======>>" + Fore.RED+ Style.BRIGHT +"\n┌[" + Fore.CYAN+ Style.BRIGHT +"Tor-Restarter"+Fore.BLUE+ Style.BRIGHT +"~"+Fore.YELLOW+ Style.BRIGHT +"@ROOT"+Fore.RED+ Style.BRIGHT +"]\n│" + Fore.RED+ Style.BRIGHT +"\n├" + Fore.GREEN + Style.BRIGHT + " 1) start" + Fore.RED+ Style.BRIGHT +"\n│" + Fore.RED+ Style.BRIGHT +"\n├" + Fore.RED + Style.BRIGHT + " 2) Exit" + Fore.RED+ Style.BRIGHT +"\n│")

   try:
      D = int(input(Fore.RED + Style.BRIGHT + "└──╼"+Fore.YELLOW+ Style.BRIGHT +">" + Fore.GREEN + Style.BRIGHT + ">" + Fore.MAGENTA  + Style.BRIGHT + ">" + Fore.YELLOW + Style.BRIGHT + " "))
      system('clear')
      if D == 1:
         main()
         print(Fore.YELLOW + Style.BRIGHT + "\n                           <<======choose a method======>>" + Fore.RED+ Style.BRIGHT +"\n┌[" + Fore.CYAN+ Style.BRIGHT +"Tor-Restarter"+Fore.BLUE+ Style.BRIGHT +"~"+Fore.YELLOW+ Style.BRIGHT +"@ROOT"+Fore.RED+ Style.BRIGHT +"]\n│" + Fore.RED+ Style.BRIGHT +"\n├" + Fore.MAGENTA + Style.BRIGHT + " 1) Auto Tor Restarter And Macchanger" + Fore.RED+ Style.BRIGHT +"\n│" + Fore.RED+ Style.BRIGHT +"\n├" + Fore.GREEN + Style.BRIGHT + " 2) Tor Restarter" + Fore.RED+ Style.BRIGHT +"\n│")
         L = int(input(Fore.RED + Style.BRIGHT + "└──╼"+Fore.YELLOW+ Style.BRIGHT +">" + Fore.GREEN + Style.BRIGHT + ">" + Fore.MAGENTA  + Style.BRIGHT + ">" + Fore.YELLOW + Style.BRIGHT + " "))         
         system('clear')
         main()
         if L == 1:
            def check():
                try:
                  system('clear')
                  main()
                  response = requests.get('https://www.google.com/')
                  if response.status_code == 200:
                     system('clear')
                     main()
                     print("\n")
                     print(Fore.GREEN + Style.BRIGHT + "WIFI / eth is connected :)")
                     time.sleep(2)
                except:
                     system('clear')
                     main()
                     print(" ")
                     print(Fore.RED + Style.BRIGHT + "                              <<====== ERROR ======>>")
                     print("\n")
                     print(Fore.RED + Style.BRIGHT + '[ERROR!] No WIFI / eth Connection')
                     time.sleep(3)
                     system('clear')
                     return check()
                 
                else:
                    system('clear')
                    main()
                    print(Fore.YELLOW + Style.BRIGHT + "\n                           <<======choose a method======>>" + Fore.RED+ Style.BRIGHT +"\n┌[" + Fore.CYAN+ Style.BRIGHT +"Tor-Restarter"+Fore.BLUE+ Style.BRIGHT +"~"+Fore.YELLOW+ Style.BRIGHT +"@ROOT"+Fore.RED+ Style.BRIGHT +"]\n│" + Fore.RED+ Style.BRIGHT +"\n├" + Fore.MAGENTA + Style.BRIGHT + " 1) WIFI" + Fore.RED+ Style.BRIGHT +"\n│" + Fore.RED+ Style.BRIGHT +"\n├" + Fore.GREEN + Style.BRIGHT + " 2) LAN" + Fore.RED+ Style.BRIGHT +"\n│")
           
                    C = int(input(Fore.RED + Style.BRIGHT + "└──╼"+Fore.YELLOW+ Style.BRIGHT +">" + Fore.GREEN + Style.BRIGHT + ">" + Fore.MAGENTA  + Style.BRIGHT + ">" + Fore.YELLOW + Style.BRIGHT + " "))   
                    if C == 1:
                       system('clear')
                       main()
                       print(Fore.YELLOW + Style.BRIGHT + "\nyour mac Addres will be changed in few second . . ." )
                       time.sleep(2)
                       system('clear')
                       main()
                       print(Fore.GREEN + Style.BRIGHT + "\nyour mac Addres has been changed :) " )
                       time.sleep(2)
                       system('clear')
                       main() 
                       print(Fore.MAGENTA + Style.BRIGHT + "\nyour new MAC Addres is:\n")
                       system('sudo ifconfig wlan0 down')
                       system('sudo macchanger -r wlan0')
                       system('sudo ifconfig wlan0 up')
                       time.sleep(4)
                       system('clear')
                       main()
                       print(Fore.YELLOW + Style.BRIGHT + "\n                    <<======insert a Password for Tor Controller ======>>                                ")
                       print(Fore.RED+ Style.BRIGHT +"\n┌[" + Fore.CYAN+ Style.BRIGHT +"Tor-Restarter"+Fore.BLUE+ Style.BRIGHT +"~"+Fore.YELLOW+ Style.BRIGHT +"@ROOT"+Fore.RED+ Style.BRIGHT +"]\n│")
                       passw = input(Fore.RED + Style.BRIGHT + "└──╼"+Fore.YELLOW+ Style.BRIGHT +">" + Fore.GREEN + Style.BRIGHT + ">" + Fore.MAGENTA  + Style.BRIGHT + ">" + Fore.YELLOW + Style.BRIGHT + " ")
                       torpass = subprocess.check_output(['sudo', 'tor' ,'--hash-password' , passw]).decode("utf8").splitlines()[1]
                       control = open("/etc/tor/torrc", "r").readlines()[55]
                       hash = open("/etc/tor/torrc", "r").readlines()[58]
                       if control.startswith("#") == True:
                           control = control[1:]
                       if hash.startswith("#") == True:
                           hash = hash[1:]
                       
                       lin = len(open("/etc/tor/torrc", "r").readlines())
                       lst = []
                       for i in range(0, lin):
                           if i == 55:
                               pass
                               lst.append(control)
                           elif i == 58:
                               lst.append(hash[:22] + torpass + "\n")    
                               pass
                           else:    
                              lst.append(open("/etc/tor/torrc", "r").readlines()[i])
                       loc = os.path.dirname(os.path.abspath(__file__)) 
                       try:
                         os.mkdir(loc + "/torbackup") 
                       except FileExistsError:
                         system("sudo rm -rf " + loc + "/torbackup")   
                         os.mkdir(loc + "/torbackup")      
                       system("sudo cp /etc/tor/torrc " + loc + "/torbackup/")
                       open("/etc/tor/torrc", "w").writelines(lst) 
                       system('clear')
                       main()
                       print(Fore.YELLOW + Style.BRIGHT + "\n             <<======How long is the countdown? (suggested 17 ~ 30)=====>>                                ")
                       print(Fore.RED+ Style.BRIGHT +"\n┌[" + Fore.CYAN+ Style.BRIGHT +"Tor-Restarter"+Fore.BLUE+ Style.BRIGHT +"~"+Fore.YELLOW+ Style.BRIGHT +"@ROOT"+Fore.RED+ Style.BRIGHT +"]\n│")
                       num = int(input(Fore.RED + Style.BRIGHT + "└──╼"+Fore.YELLOW+ Style.BRIGHT +">" + Fore.GREEN + Style.BRIGHT + ">" + Fore.MAGENTA  + Style.BRIGHT + ">" + Fore.YELLOW + Style.BRIGHT + " "))
                       system('clear')
                       if num >= 17:
                          with open(r"cache.txt", "w") as numb:
                               numb.write(str(num))
                               numb.close()
                               def loop():
                                    with open(r"cache.txt", "r") as num:
                                         num = num.read()
                                         for i in range(int(num) , 0 , -1):
                                               i = i-1
                                               main()
                                               print(Fore.YELLOW + Style.BRIGHT + "\n                                         [" + Fore.YELLOW + Style.BRIGHT + str(i) + "]\n" + Fore.BLUE + Style.BRIGHT + "to cansel press: CTRL + C ")
                                               time.sleep(1)
                                               system('clear')  
                                               if i == 0:
                                                  main()
                                                  print(Fore.BLUE + Style.BRIGHT + "to cansel press: CTRL + C ")
                                                  time.sleep(1)
                                                  system('clear')
                                                  main()
                                                  print('')
                                                  with Controller.from_port(port=9051) as controller:
                                                      controller.authenticate(password= passw)
                                                      controller.signal(Signal.NEWNYM)
                                                  time.sleep(3)
                                                  system('clear')
                                                  continue
                               loop()  
                               while True:
                                    loop()   
  
                       elif not num in range(17 , 30):
                            print(Fore.RED + Style.BRIGHT + 'the inserted number is not VALID! (minimum: 17)')
                            time.sleep(6)
                            system('clear')
                            system('exit')  
     
                    if C == 2:
                       system('clear')
                       main()
                       print(Fore.YELLOW + Style.BRIGHT + "\nyour mac Addres will be changed in few second . . ." )
                       time.sleep(2)
                       system('clear')
                       main()
                       print(Fore.GREEN + Style.BRIGHT + "\nyour mac Addres has been changed :) " )
                       time.sleep(2)
                       system('clear')
                       main() 
                       print(Fore.MAGENTA + Style.BRIGHT + "\nyour new MAC Addres is:\n")
                       system('sudo ifconfig eth0 down')
                       system('sudo macchanger -r eth0')
                       system('sudo ifconfig eth0 up')
                       time.sleep(4)
                       system('clear')
                       main()
                       print(Fore.YELLOW + Style.BRIGHT + "\n                    <<======insert a Password for Tor Controller ======>>                                ")
                       print(Fore.RED+ Style.BRIGHT +"\n┌[" + Fore.CYAN+ Style.BRIGHT +"Tor-Restarter"+Fore.BLUE+ Style.BRIGHT +"~"+Fore.YELLOW+ Style.BRIGHT +"@ROOT"+Fore.RED+ Style.BRIGHT +"]\n│")
                       passw = input(Fore.RED + Style.BRIGHT + "└──╼"+Fore.YELLOW+ Style.BRIGHT +">" + Fore.GREEN + Style.BRIGHT + ">" + Fore.MAGENTA  + Style.BRIGHT + ">" + Fore.YELLOW + Style.BRIGHT + " ")
                       torpass = subprocess.check_output(['sudo', 'tor' ,'--hash-password' , passw]).decode("utf8").splitlines()[1]
                       control = open("/etc/tor/torrc", "r").readlines()[55]
                       hash = open("/etc/tor/torrc", "r").readlines()[58]
                       if control.startswith("#") == True:
                           control = control[1:]
                       if hash.startswith("#") == True:
                           hash = hash[1:]
                       
                       lin = len(open("/etc/tor/torrc", "r").readlines())
                       lst = []
                       for i in range(0, lin):
                           if i == 55:
                               pass
                               lst.append(control)
                           elif i == 58:
                               lst.append(hash[:22] + torpass + "\n")    
                               pass
                           else:    
                              lst.append(open("/etc/tor/torrc", "r").readlines()[i])
                       loc = os.path.dirname(os.path.abspath(__file__)) 
                       try:
                         os.mkdir(loc + "/torbackup") 
                       except FileExistsError:
                         system("sudo rm -rf " + loc + "/torbackup")   
                         os.mkdir(loc + "/torbackup")      
                       system("sudo cp /etc/tor/torrc " + loc + "/torbackup/")
                       open("/etc/tor/torrc", "w").writelines(lst) 
                       system('clear')
                       main()
                       print(Fore.YELLOW + Style.BRIGHT + "\n             <<======How long is the countdown? (suggested 17 ~ 30)=====>>                                ")
                       print(Fore.RED+ Style.BRIGHT +"\n┌[" + Fore.CYAN+ Style.BRIGHT +"Tor-Restarter"+Fore.BLUE+ Style.BRIGHT +"~"+Fore.YELLOW+ Style.BRIGHT +"@ROOT"+Fore.RED+ Style.BRIGHT +"]\n│")
                       num = int(input(Fore.RED + Style.BRIGHT + "└──╼"+Fore.YELLOW+ Style.BRIGHT +">" + Fore.GREEN + Style.BRIGHT + ">" + Fore.MAGENTA  + Style.BRIGHT + ">" + Fore.YELLOW + Style.BRIGHT + " "))
                       system('clear')
                       if num >= 17:
                          with open(r"cache.txt", "w") as numb:
                               numb.write(str(num))
                               numb.close()
                               def loop():
                                    with open(r"cache.txt", "r") as num:
                                         num = num.read()
                                         for i in range(int(num) , 0 , -1):
                                               i = i-1
                                               main()
                                               print(Fore.YELLOW + Style.BRIGHT + "                                         [" + Fore.YELLOW + Style.BRIGHT + str(i) + "]\n" + Fore.BLUE + Style.BRIGHT + "to cansel press: CTRL + C ")
                                               time.sleep(1)
                                               system('clear')  
                                               if i == 0:
                                                  main()
                                                  print(Fore.BLUE + Style.BRIGHT + "to cansel press: CTRL + C ")
                                                  time.sleep(1)
                                                  system('clear')
                                                  main()
                                                  print('')
                                                  with Controller.from_port(port=9051) as controller:
                                                      controller.authenticate(password= passw)
                                                      controller.signal(Signal.NEWNYM)
                                                  time.sleep(3)
                                                  system('clear')
                                                  continue
                               loop()  
                               while True:
                                    loop()   
  
                       elif not num in range(17 , 30):
                            print(Fore.RED + Style.BRIGHT + 'the inserted number is not VALID! (minimum: 17)')
                            time.sleep(6)
                            system('clear')
                            system('exit')  
            check()  

         if L == 2:
               system('clear')
               main()
               print(' ')
               print(Fore.YELLOW + Style.BRIGHT + "                    <<======insert you\'r Tor Control Password======>>                                ")
               print(Fore.RED+ Style.BRIGHT +"\n┌[" + Fore.CYAN+ Style.BRIGHT +"Tor-Restarter"+Fore.BLUE+ Style.BRIGHT +"~"+Fore.YELLOW+ Style.BRIGHT +"@ROOT"+Fore.RED+ Style.BRIGHT +"]\n│")
               passw = input(Fore.RED + Style.BRIGHT + "└──╼"+Fore.YELLOW+ Style.BRIGHT +">" + Fore.GREEN + Style.BRIGHT + ">" + Fore.MAGENTA  + Style.BRIGHT + ">" + Fore.YELLOW + Style.BRIGHT + " ")
               torpass = subprocess.check_output(['sudo', 'tor' ,'--hash-password' , passw]).decode("utf8").splitlines()[1]
               control = open("/etc/tor/torrc", "r").readlines()[55]
               hash = open("/etc/tor/torrc", "r").readlines()[58]
               if control.startswith("#") == True:
                   control = control[1:]
               if hash.startswith("#") == True:
                   hash = hash[1:]
               
               lin = len(open("/etc/tor/torrc", "r").readlines())
               lst = []
               for i in range(0, lin):
                   if i == 55:
                       pass
                       lst.append(control)
                   elif i == 58:
                       lst.append(hash[:22] + torpass + "\n")    
                       pass
                   else:    
                      lst.append(open("/etc/tor/torrc", "r").readlines()[i])
               loc = os.path.dirname(os.path.abspath(__file__)) 
               try:
                 os.mkdir(loc + "/torbackup") 
               except FileExistsError:
                 system("sudo rm -rf " + loc + "/torbackup")   
                 os.mkdir(loc + "/torbackup")      
               system("sudo cp /etc/tor/torrc " + loc + "/torbackup/")
               open("/etc/tor/torrc", "w").writelines(lst) 
               system('clear')
               main()
               print(' ')
               print(Fore.YELLOW + Style.BRIGHT + "             <<======How long is the countdown? (suggested 17 ~ 30)=====>>                                ")
               print(Fore.RED+ Style.BRIGHT +"\n┌[" + Fore.CYAN+ Style.BRIGHT +"Tor-Restarter"+Fore.BLUE+ Style.BRIGHT +"~"+Fore.YELLOW+ Style.BRIGHT +"@ROOT"+Fore.RED+ Style.BRIGHT +"]\n│")
               num = int(input(Fore.RED + Style.BRIGHT + "└──╼"+Fore.YELLOW+ Style.BRIGHT +">" + Fore.GREEN + Style.BRIGHT + ">" + Fore.MAGENTA  + Style.BRIGHT + ">" + Fore.YELLOW + Style.BRIGHT + " "))
               system('clear')
               if num >= 17:
                  with open(r"cache.txt", "w") as numb:
                       numb.write(str(num))
                       numb.close()
                       def loop():
                            with open(r"cache.txt", "r") as num:
                                 num = num.read()
                                 for i in range(int(num) , 0 , -1):
                                       i = i-1
                                       main()
                                       print(Fore.YELLOW + Style.BRIGHT + "                                         [" + Fore.YELLOW + Style.BRIGHT + str(i) + "]\n" + Fore.BLUE + Style.BRIGHT + "to cansel press: CTRL + C ")
                                       time.sleep(1)
                                       system('clear')  
                                       if i == 0:
                                          main()
                                          print(Fore.BLUE + Style.BRIGHT + "to cansel press: CTRL + C ")
                                          time.sleep(1)
                                          system('clear')
                                          main()
                                          print('')
                                          with Controller.from_port(port=9051) as controller:
                                              controller.authenticate(password= passw)
                                              controller.signal(Signal.NEWNYM)
                                          time.sleep(3)
                                          system('clear')
                                          continue
                       loop()  
                       while True:
                            loop()   
  
               elif not num in range(17 , 30):
                    print(Fore.RED + Style.BRIGHT + 'the inserted number is not VALID! (minimum: 17)')
                    time.sleep(6)
                    system('clear')
                    system('exit')  



      elif D == 2:
         system('clear')
         system('exit')                         

   except KeyboardInterrupt:  
      system('clear')
      main()
      print(Fore.GREEN + "\n\nGOOD LUCK! :)")


#elif oss == "Android":
#   main()
#   print(Fore.YELLOW + Style.BRIGHT + "\n                           <<======choose a method======>>" + Fore.RED+ Style.BRIGHT +"\n┌[" + Fore.CYAN+ Style.BRIGHT +"Tor-Restarter"+Fore.BLUE+ Style.BRIGHT +"~"+Fore.YELLOW+ Style.BRIGHT +"@ROOT"+Fore.RED+ Style.BRIGHT +"]\n│" + Fore.RED+ Style.BRIGHT +"\n├" + Fore.GREEN + Style.BRIGHT + " 1) start" + Fore.RED+ Style.BRIGHT +"\n│" + Fore.RED+ Style.BRIGHT +"\n├" + Fore.RED + Style.BRIGHT + " 2) Exit" + Fore.RED+ Style.BRIGHT +"\n│")
#
#   try:
#      D = int(input(Fore.RED + Style.BRIGHT + "└──╼"+Fore.YELLOW+ Style.BRIGHT +">" + Fore.GREEN + Style.BRIGHT + ">" + Fore.MAGENTA  + Style.BRIGHT + ">" + Fore.YELLOW + Style.BRIGHT + " "))
#      system('clear')
#      if D == 1:
#         main()
#         print(Fore.YELLOW + Style.BRIGHT + "\n                           <<======choose a method======>>" + Fore.RED+ Style.BRIGHT +"\n┌[" + Fore.CYAN+ Style.BRIGHT +"Tor-Restarter"+Fore.BLUE+ Style.BRIGHT +"~"+Fore.YELLOW+ Style.BRIGHT +"@ROOT"+Fore.RED+ Style.BRIGHT +"]\n│" + Fore.RED+ Style.BRIGHT +"\n├" + Fore.MAGENTA + Style.BRIGHT + " 1) Tor Restarter" + Fore.RED+ Style.BRIGHT +"\n│")
#         L = int(input(Fore.RED + Style.BRIGHT + "└──╼"+Fore.YELLOW+ Style.BRIGHT +">" + Fore.GREEN + Style.BRIGHT + ">" + Fore.MAGENTA  + Style.BRIGHT + ">" + Fore.YELLOW + Style.BRIGHT + " "))         
#         system('clear')
#         main()
#         if L == 1:
#            def check():
#                try:
#                  system('clear')
#                  main()
#                  response = requests.get('https://www.google.com/')
#                  if response.status_code == 200:
#                     system('clear')
#                     main()
#                     print("\n")
#                     print(Fore.GREEN + Style.BRIGHT + "WIFI is connected :)")
#                     time.sleep(2)
#                except:
#                     system('clear')
#                     main()
#                     print(" ")
#                     print(Fore.RED + Style.BRIGHT + "                              <<====== ERROR ======>>")
#                     print("\n")
#                     print(Fore.RED + Style.BRIGHT + '[ERROR!] No WIFI Connection')
#                     time.sleep(3)
#                     system('clear')
#                     check()
#                 
#                else:
#                    system('clear')
#                    main()
#                    print(Fore.YELLOW + Style.BRIGHT + "\n                           <<======choose a method======>>" + Fore.RED+ Style.BRIGHT +"\n┌[" + Fore.CYAN+ Style.BRIGHT +"Tor-Restarter"+Fore.BLUE+ Style.BRIGHT +"~"+Fore.YELLOW+ Style.BRIGHT +"@ROOT"+Fore.RED+ Style.BRIGHT +"]\n│" + Fore.RED+ Style.BRIGHT +"\n├" + Fore.MAGENTA + Style.BRIGHT + " 1) WIFI" + Fore.RED+ Style.BRIGHT +"\n│")
#                    C = int(input(Fore.RED + Style.BRIGHT + "└──╼"+Fore.YELLOW+ Style.BRIGHT +">" + Fore.GREEN + Style.BRIGHT + ">" + Fore.MAGENTA  + Style.BRIGHT + ">" + Fore.YELLOW + Style.BRIGHT + " "))   
#                    if C == 1:
#                       system('clear')
#                       main()
#                       print(Fore.YELLOW + Style.BRIGHT + "\n                    <<======insert a Password for Tor Controller ======>>                                ")
#                       print(Fore.RED+ Style.BRIGHT +"\n┌[" + Fore.CYAN+ Style.BRIGHT +"Tor-Restarter"+Fore.BLUE+ Style.BRIGHT +"~"+Fore.YELLOW+ Style.BRIGHT +"@ROOT"+Fore.RED+ Style.BRIGHT +"]\n│")
#                       passw = input(Fore.RED + Style.BRIGHT + "└──╼"+Fore.YELLOW+ Style.BRIGHT +">" + Fore.GREEN + Style.BRIGHT + ">" + Fore.MAGENTA  + Style.BRIGHT + ">" + Fore.YELLOW + Style.BRIGHT + " ")
#                       torpass = subprocess.check_output(['tor' ,'--hash-password' , passw]).decode("utf8").splitlines()[1]
#                       control = open("/usr/etc/tor/torrc", "r").readlines()[55]
#                       hash = open("/usr/etc/tor/torrc", "r").readlines()[58]
#                       if control.startswith("#") == True:
#                           control = control[1:]
#                       if hash.startswith("#") == True:
#                           hash = hash[1:]
#                       
#                       lin = len(open("/usr/etc/tor/torrc", "r").readlines())
#                       lst = []
#                       for i in range(0, lin):
#                           if i == 55:
#                               pass
#                               lst.append(control)
#                           elif i == 58:
#                               lst.append(hash[:22] + torpass + "\n")    
#                               pass
#                           else:    
#                              lst.append(open("/usr/etc/tor/torrc", "r").readlines()[i])
#                       loc = os.path.dirname(os.path.abspath(__file__)) 
#                       try:
#                         os.mkdir(loc + "/torbackup") 
#                       except FileExistsError:
#                         system("rm -rf " + loc + "/torbackup")   
#                         os.mkdir(loc + "/torbackup")      
#                       system("cp /usr/etc/tor/torrc " + loc + "/torbackup/")
#                       open("/usr/etc/tor/torrc", "w").writelines(lst) 
#                       system('clear')
#                       main()
#                       print(Fore.YELLOW + Style.BRIGHT + "\n             <<======How long is the countdown? (suggested 17 ~ 30)=====>>                                ")
#                       print(Fore.RED+ Style.BRIGHT +"\n┌[" + Fore.CYAN+ Style.BRIGHT +"Tor-Restarter"+Fore.BLUE+ Style.BRIGHT +"~"+Fore.YELLOW+ Style.BRIGHT +"@ROOT"+Fore.RED+ Style.BRIGHT +"]\n│")
#                       num = int(input(Fore.RED + Style.BRIGHT + "└──╼"+Fore.YELLOW+ Style.BRIGHT +">" + Fore.GREEN + Style.BRIGHT + ">" + Fore.MAGENTA  + Style.BRIGHT + ">" + Fore.YELLOW + Style.BRIGHT + " "))
#                       system('clear')
#                       if num >= 17:
#                          with open(r"cache.txt", "w") as numb:
#                               numb.write(str(num))
#                               numb.close()
#                               def loop():
#                                    with open(r"cache.txt", "r") as num:
#                                         num = num.read()
#                                         for i in range(int(num) , 0 , -1):
#                                               i = i-1
#                                               main()
#                                               print(Fore.YELLOW + Style.BRIGHT + "                                         [" + Fore.YELLOW + Style.BRIGHT + str(i) + "]")
#                                               print(Fore.BLUE + Style.BRIGHT + "to cansel press: CTRL + C ")
#                                               time.sleep(1)
#                                               system('clear')  
#                                               if i == 0:
#                                                  main()
#                                                  print(Fore.BLUE + Style.BRIGHT + "to cansel press: CTRL + C ")
#                                                  time.sleep(1)
#                                                  system('clear')
#                                                  main()
#                                                  print('')
#                                                  with Controller.from_port(port=9051) as controller:
#                                                      controller.authenticate(password= passw)
#                                                      controller.signal(Signal.NEWNYM)
#                                                  time.sleep(3)
#                                                  system('clear')
#                                                  continue
#                               loop()  
#                               while True:
#                                    loop()   
#  
#                       elif not num in range(17 , 30):
#                            print(Fore.RED + Style.BRIGHT + 'the inserted number is not VALID! (minimum: 17)')
#                            time.sleep(6)
#                            system('clear')
#                            system('exit')  
#            check()                        
#
#   except KeyboardInterrupt:  
#      system('clear')
#      main()
#      print(Fore.GREEN + "\n\nGOOD LUCK! :)")
#      
else:
     print(Fore.GREEN + '\nComing soon for other os :)')
     time.sleep(2)
     system('exit')  