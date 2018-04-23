import pyautogui # Keystrokes
import socket # OSC Messaging

UDP_IP = "127.0.0.1" # localhost
UDP_PORT_SEND = 6448 # default OSC wekinator input
UDP_PORT_RECE = 12000 # default OSC wekinator output

sock_RECE = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_RECE.bind((UDP_IP, UDP_PORT_RECE))

while(1):
    # Listen for the wek/outputs
    data, addr = sock_RECE.recvfrom(3000)  # buffer size is 1024 bytes
    # print(data)
    d = data.split(",")[1]
    print (d)
    if d[1] == 'ffff\x00\x00\x00?\x80\x00\x00@\x00\x00\x00@\x00\x00\x00?\x80\x00\x00':
        print("class1")
    elif d[1] == 'ffff\x00\x00\x00?\x80\x00\x00?\x80\x00\x00@\x00\x00\x00?\x80\x00\x00':
        print("class2")
    elif d[1] == 'ffff\x00\x00\x00?\x80\x00\x00@\x00\x00\x00@\x00\x00\x00?\x80\x00\x00':
        print ("plas")





ffff @?@@ @@


    'ffff\x00\x00\x00@@\x00\x00?\x80\x00\x00?\x80\x00\x00?\x80\x00\x00'
    'ffff\x00\x00\x00@\x80\x00\x00?\x80\x00\x00?\x80\x00\x00?\x80\x00\x00'
