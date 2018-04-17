import pyautogui # Keystrokes
import socket # OSC Messaging

UDP_IP = "127.0.0.1" # localhost
UDP_PORT_SEND = 6448 # default OSC wekinator input
UDP_PORT_RECE = 12000 # default OSC wekinator output

sock_RECE = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_RECE.bind((UDP_IP, UDP_PORT_RECE))

# Much of this was pulled from the example by IMLHC4I Project Group 'Final-Samurai-Piledrivers'

while(1):
    # Listen for the wek/outputs
    data, addr = sock_RECE.recvfrom(1024)  # buffer size is 1024 bytes

    # USE THIS FOR FINDING NEW CLASSES
    # print ("20:", data[20])
    # print ("21:", data[21])
	 
	
    if data[20] == '?':
        # class 1
        pyautogui.keyDown('w')
        pyautogui.keyUp('w')
        print("up")

    elif data[20] == '@':
        if data[21] == '\x00':
            #class 2
            pyautogui.keyDown('a')
            pyautogui.keyUp('a')
            print("left")
        elif data[21] == '@':
            #class 3
            pyautogui.keyDown('s')
            pyautogui.keyUp('s')
            print("down")
        elif data[21] == '\x80':
            #class 4
            pyautogui.keyDown('d')
            pyautogui.keyUp('d')
            print("right")
        elif data[21] == '\xa0':
            #class 5
            pyautogui.keyDown('h')
            pyautogui.keyUp('h')
            print("throw")
        elif data[21] == '\xc0':
            #class 6
            pyautogui.keyDown('j')
            pyautogui.keyUp('j')
            print("quick")
        elif data[21] == '\xe0':
            #class 7
            pyautogui.keyDown('k')
            pyautogui.keyUp('k')
            print("heavy")

    elif data[20] == 'A':
        if data[21] != '\x00':
            #class 8
            pyautogui.keyDown('l')
            pyautogui.keyUp('l')
            print("dodge")