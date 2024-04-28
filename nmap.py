import os

def nmap_hello():
    print("""
    __

        SyberCord/Nmap
    __


    0-              NMAP
    1-              -sC -sV
    """)

    ip = input("ip Adresini Giriniz : ")
    islemno = input("islem No Giriniz : ")
    if islemno == "0":
        os.system("nmap " + ip)
    elif islemno == "1":
        os.system("nmap -sC -sV " + ip)

nmap_hello()
