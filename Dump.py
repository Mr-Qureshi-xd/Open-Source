#!/usr/bin/python3
#encoding=utf:8
#dumpingtool 0.0.1
#--Credit Bilal Haider <3
#---------[ IMPORTING MODULES ]-------->>
from os import system as cmd
from string import whitespace
from time import sleep as slp
#---------[ LOGO / BANNER ]-------->>
red = "\x1b[1;91m"
green = "\x1b[1;92m"
white = "\x1b[1;97m"
#---------[ LOGO / BANNER ]-------->>
def logo():
    cmd("clear")
    print(" ")
    print("-"*49)
#---------[ DUMPING RANDOM ]-------->>
def randdumpusr():
    logo()
    name = input(f"[{green}+{white}] Input Username (ex: Eman Waheed): ")
    filepath = input(f"[{green}+{white}] Input Filename : ")
    try:
        limit = int(input(f"[{green}+{white}] Input Dump limit : "))
    except ValueError:
        limit = 5000
        if limit>5000:
            limit = 5000
    namex = name.replace(" ",".")
    try:
        file = open(filepath,"w")
    except:
        file = name.replace(" ","_")+".txt"
    for number in range(limit):
        number +=1
        file.write(namex.lower()+"."+str(number)+"|"+name+"\n")
    file.close()
    print("-"*49)
    print(f"[+] Your File Save as : {green}{filepath}{white}")
    print(f"[+] Total Limit Dump : {green}{str(limit)}{white}")
    print(f"[+] Your Username For Dump : {green}{name.lower()}{white}")
    print("-"*49)
if __name__=="__main__":
    randdumpusr()
