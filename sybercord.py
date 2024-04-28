import os
import time

def mainmenu():
    os.system("apt-get install figlet")
    os.system("clear")
    os.system("figlet SyberCord")
    print("""
           _________________
    
            SyberCord/Tools 
           _________________
           
           
[-] \033[94mTool Created By Muhtalipcan\033[0m
           
           
         [01]   NMAP       
         [02]   TRACER      
         [03]   Pishing
         [04]   usserrecon
         
         
          99-   Exit
    """)

def nmapscan():
    os.system("python3 nmap.py")

import os

def zphisher():
    if not os.path.exists("zphisher"):
        os.system("git clone https://github.com/htr-tech/zphisher.git")
    os.chdir("zphisher")
    os.system("bash zphisher.sh")
    
    
def usserecon():
     if not os.path.exists("userrecon"):
        os.system("git clone https://github.com/wishihab/userrecon.git")
     os.chdir("userrecon")
     print("loading...")
     time.sleep(3)
     os.system("clear")
     os.system("bash userrecon.sh")
     print("press Ctrl + C to abort.")



    
def ip_tracer():
      if not  os.path.exists("IP-Tracer"):
           os.system("git clone https://github.com/rajkumardusad/IP-Tracer")
      os.system("cd IP-Tracer")
      ip = input("IP Adress: ") 
      os.system(f"trace -t {ip}") 
      sistem = input("Muhtalipcan$")
    
    
    



def main():
    while True:
        mainmenu()
        choice = input("[-] Select an option : ")
        if choice == '1':
            nmapscan()
        elif choice == '2':  
            zphisher()
        if choice == '3':
            ip_tracer()
        if choice == '4':
            usserecon()
        elif choice == '99':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
