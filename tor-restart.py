import time
from os import system
import os
import sys
import requests
from colorama import Fore, Style, Back
from colorama import init
from subprocess import *
import subprocess
init(autoreset=True)

system('clear')
def main():
    print(Fore.YELLOW + Style.BRIGHT + " ----------------------------------------------------------------------------------------------------------------------------------------------- ")
    print(Fore.YELLOW + Style.BRIGHT + "|                                                                                                                                              " + Fore.YELLOW + Style.BRIGHT + "|")
    print(Fore.YELLOW + Style.BRIGHT + "|                                                                                                                                              " + Fore.YELLOW + Style.BRIGHT + "|")
    print(Fore.YELLOW + Style.BRIGHT + "|         " + Fore.RED + Style.BRIGHT + "   ▄████████    ▄████████  ▄████████ ███    █▄     ▄████████  ▄█      ███     ▄██   ▄           ▄█    █▄      ▄▄▄▄███▄▄▄▄  " + "          " + Fore.YELLOW + Style.BRIGHT + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|         " + Fore.RED + Style.BRIGHT + "  ███    ███   ███    ███ ███    ███ ███    ███   ███    ███ ███  ▀█████████▄ ███   ██▄        ███    ███   ▄██▀▀▀███▀▀▀██▄" + "          " + Fore.YELLOW + Style.BRIGHT + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|         " + Fore.RED + Style.BRIGHT + "  ███    █▀    ███    █▀  ███    █▀  ███    ███   ███    ███ ███▌    ▀███▀▀██ ███▄▄▄███        ███    ███   ███   ███   ███" +  "          " + Fore.YELLOW + Style.BRIGHT + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|         " + Fore.RED + Style.BRIGHT + "  ███         ▄███▄▄▄     ███        ███    ███  ▄███▄▄▄▄██▀ ███▌     ███   ▀ ▀▀▀▀▀▀███       ▄███▄▄▄▄███▄▄ ███   ███   ███" + "          " + Fore.YELLOW + Style.BRIGHT + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|         " + Fore.RED + Style.BRIGHT + "▀███████████ ▀▀███▀▀▀     ███        ███    ███ ▀▀███▀▀▀▀▀   ███▌     ███     ▄██   ███      ▀▀███▀▀▀▀███▀  ███   ███   ███" + "          " + Fore.YELLOW + Style.BRIGHT + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|         " + Fore.RED + Style.BRIGHT + "         ███   ███    █▄  ███    █▄  ███    ███ ▀███████████ ███      ███     ███   ███        ███    ███   ███   ███   ███" + "          " + Fore.YELLOW + Style.BRIGHT + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|         " + Fore.RED + Style.BRIGHT + "   ▄█    ███   ███    ███ ███    ███ ███    ███   ███    ███ ███      ███     ███   ███        ███    ███   ███   ███   ███" + "          " + Fore.YELLOW + Style.BRIGHT + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|         " + Fore.RED + Style.BRIGHT + " ▄████████▀    ██████████ ████████▀  ████████▀    ███    ███ █▀      ▄████▀    ▀█████▀         ███    █▀     ▀█   ███   █▀ " + "          " + Fore.YELLOW + Style.BRIGHT + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|         " + Fore.RED + Style.BRIGHT + "                                                  ███    ███                                                               " + "          " + Fore.YELLOW + Style.BRIGHT + "|") 
    print(Fore.YELLOW + Style.BRIGHT + "|______________________________________________________________________________________________________________________________________________|")
    print(Fore.YELLOW + Style.BRIGHT + "|" + Fore.RED + Style.BRIGHT + "                                                                    " + Fore.RED + Style.BRIGHT + "v2.05" + "                                                                     " + Fore.YELLOW + Style.BRIGHT + "|")
    print(Fore.YELLOW + Style.BRIGHT + " ----------------------------------------------------------------------------------------------------------------------------------------------- ")


oss = subprocess.check_output(['uname', '-o']).strip().decode('utf-8')
if oss == "GNU/Linux":
   main()
   print(Fore.YELLOW + Style.BRIGHT + "                                                                                                ")
   print(Fore.YELLOW + Style.BRIGHT + "                                                         <<======chose a method======>>                                ")
   print(Fore.RED+ Style.BRIGHT +"\n┌[" + Fore.CYAN+ Style.BRIGHT +"Tor-Restarter"+Fore.BLUE+ Style.BRIGHT +"~"+Fore.YELLOW+ Style.BRIGHT +"@ROOT"+Fore.RED+ Style.BRIGHT +"]\n│")
   print(Fore.RED+ Style.BRIGHT +"├" + Fore.GREEN + Style.BRIGHT + " 1) start") 
   print(Fore.RED+ Style.BRIGHT +"│")  
   print(Fore.RED+ Style.BRIGHT +"├" + Fore.RED + Style.BRIGHT + " 2) Exit")
   print(Fore.RED+ Style.BRIGHT +"│") 
   try:
      D = int(input(Fore.RED + Style.BRIGHT + "└──╼"+Fore.YELLOW+ Style.BRIGHT +">" + Fore.GREEN + Style.BRIGHT + ">" + Fore.MAGENTA  + Style.BRIGHT + ">" + Fore.YELLOW + Style.BRIGHT + " "))
      system('clear')
      if D == 1:
         main()
         print(Fore.YELLOW + Style.BRIGHT + "                                                                                                ")
         print(Fore.YELLOW + Style.BRIGHT + "                                                         <<======chose a method======>>                                ")
         print(Fore.RED+ Style.BRIGHT +"\n┌[" + Fore.CYAN+ Style.BRIGHT +"Tor-Restarter"+Fore.BLUE+ Style.BRIGHT +"~"+Fore.YELLOW+ Style.BRIGHT +"@ROOT"+Fore.RED+ Style.BRIGHT +"]\n│")
         print(Fore.RED+ Style.BRIGHT +"├" + Fore.MAGENTA + Style.BRIGHT + " 1) Auto Tor Restarter And Macchanger") 
         print(Fore.RED+ Style.BRIGHT +"│")  
         print(Fore.RED+ Style.BRIGHT +"├" + Fore.GREEN + Style.BRIGHT + " 2) Tor Restarter")
         print(Fore.RED+ Style.BRIGHT +"│") 

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
                     print(Fore.RED + Style.BRIGHT + "                                                            <<====== ERROR ======>>                                ")
                     print("\n")
                     print(Fore.RED + Style.BRIGHT + '[ERROR!] No WIFI / eth Connection')
                     time.sleep(3)
                     system('clear')
                     return check()
                 
                else:
                    system('clear')
                    main()
                    print(Fore.YELLOW + Style.BRIGHT + "\n                                                         <<======chose a method======>>                                ")
                    print(Fore.RED+ Style.BRIGHT +"\n┌[" + Fore.CYAN+ Style.BRIGHT +"Tor-Restarter"+Fore.BLUE+ Style.BRIGHT +"~"+Fore.YELLOW+ Style.BRIGHT +"@ROOT"+Fore.RED+ Style.BRIGHT +"]\n│")
                    print(Fore.RED+ Style.BRIGHT +"├" + Fore.MAGENTA + Style.BRIGHT + " 1) WIFI") 
                    print(Fore.RED+ Style.BRIGHT +"│")  
                    print(Fore.RED+ Style.BRIGHT +"├" + Fore.GREEN + Style.BRIGHT + " 2) LAN")
                    print(Fore.RED+ Style.BRIGHT +"│") 
           
                    C = int(input(Fore.RED + Style.BRIGHT + "└──╼"+Fore.YELLOW+ Style.BRIGHT +">" + Fore.GREEN + Style.BRIGHT + ">" + Fore.MAGENTA  + Style.BRIGHT + ">" + Fore.YELLOW + Style.BRIGHT + " "))   
                    if C == 1:
                       system('clear')
                       main()
                       print("\n")
                       print(Fore.YELLOW + Style.BRIGHT + "your mac Addres will be changed in few second . . ." )
                       time.sleep(2)
                       system('clear')
                       main()
                       print("\n")
                       print(Fore.GREEN + Style.BRIGHT + "your mac Addres has been changed :) " )
                       time.sleep(2)
                       system('clear')
                       main() 
                       print(" ")
                       print(Fore.MAGENTA + Style.BRIGHT + "your new MAC Addres is:")
                       print(Fore.MAGENTA + Style.BRIGHT + " ")
                       system('sudo macchanger -r wlan0')
                       time.sleep(4)
                       system('clear')
                       main()
                       print(' ')
                       num = int(input(Fore.YELLOW + Style.BRIGHT + "How long is the countdown? (suggested 17 ~ 30)\n\n+++> "))
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
                                               print(Fore.YELLOW + Style.BRIGHT + "                                                                      [" + Fore.YELLOW + Style.BRIGHT + str(i) + "]")
                                               print(Fore.BLUE + Style.BRIGHT + "to cansel press: CTRL + C ")
                                               time.sleep(1)
                                               system('clear')  
                                               if i == 0:
                                                  main()
                                                  print(Fore.BLUE + Style.BRIGHT + "to cansel press: CTRL + C ")
                                                  time.sleep(1)
                                                  system('clear')
                                                  main()
                                                  print('')
                                                  system('sudo service tor restart')
                                                  system('sudo service tor status')
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
     
                    if C == 1:
                       system('clear')
                       main()
                       print("\n")
                       print(Fore.YELLOW + Style.BRIGHT + "your mac Addres will be changed in few second . . ." )
                       time.sleep(2)
                       system('clear')
                       main()
                       print("\n")
                       print(Fore.GREEN + Style.BRIGHT + "your mac Addres has been changed :) " )
                       time.sleep(2)
                       system('clear')
                       main() 
                       print(" ")
                       print(Fore.MAGENTA + Style.BRIGHT + "your new MAC Addres is:")
                       print(Fore.MAGENTA + Style.BRIGHT + " ")
                       system('sudo macchanger -r eth0')
                       time.sleep(4)
                       system('clear')
                       main()
                       print(' ')
                       num = int(input(Fore.YELLOW + Style.BRIGHT + "How long is the countdown? (suggested 17 ~ 30)\n\n+++> "))
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
                                               print(Fore.YELLOW + Style.BRIGHT + "                                                                      [" + Fore.YELLOW + Style.BRIGHT + str(i) + "]")
                                               print(Fore.BLUE + Style.BRIGHT + "to cansel press: CTRL + C ")
                                               time.sleep(1)
                                               system('clear')  
                                               if i == 0:
                                                  main()
                                                  print(Fore.BLUE + Style.BRIGHT + "to cansel press: CTRL + C ")
                                                  time.sleep(1)
                                                  system('clear')
                                                  main()
                                                  print('')
                                                  system('sudo service tor restart')
                                                  system('sudo service tor status')
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
               num = int(input(Fore.YELLOW + Style.BRIGHT + "How long is the countdown? (suggested 17 ~ 30)\n\n+++> "))
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
                                       print(Fore.YELLOW + Style.BRIGHT + "                                                                      [" + Fore.YELLOW + Style.BRIGHT + str(i) + "]")
                                       print(Fore.BLUE + Style.BRIGHT + "to cansel press: CTRL + C ")
                                       time.sleep(1)
                                       system('clear')  
                                       if i == 0:
                                          main()
                                          print(Fore.BLUE + Style.BRIGHT + "to cansel press: CTRL + C ")
                                          time.sleep(1)
                                          system('clear')
                                          main()
                                          print('')
                                          system('sudo service tor restart')
                                          system('sudo service tor status')
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


elif oss == "Android":
     print(Fore.GREEN + '\nComing soon for termux :)')
     time.sleep(2)
     system('exit')

else:
     print(Fore.GREEN + '\nComing soon for other os :)')
     time.sleep(2)
     system('exit')  