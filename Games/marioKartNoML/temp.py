# Jonathan Fermin
# Mario Kart Super Circuit
# https://emulatoronline.com/gba-games/mario-kart-super-circuit/

import serial
import pyautogui
from threading import Thread
# pyautogui.PAUSE = .5 
# set a pause between each keystroke function

def acceleration_controller(LHaccx, LHaccy, LHaccz, RHaccx, RHaccy, RHaccz):
	# print("acc")
	# find break points here by printing out data and finding when the tilt becomes too much
	leftTilt = 600 
	rightTilt = 400
	if (LHaccx >= leftTilt and RHaccx >= leftTilt):
		# print("left")
		pyautogui.keyDown('left')
	elif (LHaccx <= rightTilt and RHaccx <= rightTilt):
		# print("right")
		pyautogui.keyDown('right')
	elif ((LHaccx > rightTilt and RHaccx > rightTilt) or(LHaccx < leftTilt and RHaccx < leftTilt)):
		pyautogui.keyUp('left')
		pyautogui.keyUp('right')

def h_controller(LHbutton1, LHbutton2, RHbutton1, RHbutton2):
	leftButton1 = 'a'
	leftButton2 = 'b'
	if LHbutton1 == "1":
		pyautogui.keyDown(leftButton1)
		# print("lb1")
				# print(leftButton1)
	else:
		pyautogui.keyUp(leftButton1)
		# print("off")
	if LHbutton2 == "1":
		pyautogui.keyDown(leftButton2)
		# print("lb2")
		# print(leftButton2)
	else:
		pyautogui.keyUp(leftButton2)
		# print("off")

	rightButton1 = 's'
	rightButton2 = 'x'
	if RHbutton1 == "1":
		pyautogui.keyDown(rightButton1)
		# print("rb1")
		# print("off")
	else:
		pyautogui.keyUp(rightButton1)
	if RHbutton2 == "1":
		pyautogui.keyDown(rightButton2)
		# print("rb2")
	else:
		pyautogui.keyUp(rightButton2)
		# print("off")

# First Microbit
ax = 0
ay = 0
az = 0
a1 = 0
a2 = 0

bx = 0
by = 0
bz = 0
b1 = 0
b2 = 0

def run_controller():
	global ax
	global ay
	global az
	global a1
	global a2
	global bx
	global by
	global bz
	global b1
	global b2
	while True:
		acceleration_controller(ax, ay, az, bx, by, bz)
		h_controller(a1, a2, b1, b2)

run_thread = Thread(target=run_controller, args = ())
run_thread.start()



# Data comes in looking like this:
# b'a530,503,253,0,0              \r\n'
# b'b409,448,273,0,0              \r\n'
# b'a526,503,249,0,0              \r\n'

# To format this in a way that we can use it


ser = serial.Serial("/dev/cu.usbmodem1422", 115200)
while True:
	# convert from bytes to a string

	line = str(ser.readline());
	if line:
		# if the character coming in is an a
		# we want to set it to a certain value

		if (line[2] == "a"): 
			# remove the b'a
			# print (line)
			line = line.replace("b'a", "").replace(" ", "")
			# remove the trailing \r\n' at the end
			line = line[:-5] 
			# left with 409,448,273,0,0
			a = line.split(",")
			# split creates an array delimited by a comma
			# set these to the global values
			if(len(a) >= 4):
				ax = int(a[0])
				ay = int(a[1])
				az = int(a[2])
				a1 = a[3]
				a2 = a[4]
				# print (a1)
			# print (a[3] + "," + a[4])
		elif (line[2] == "b"):
			# print("before" + line)
			line = line.replace("b'b", "").replace(" ", "")
			line = line[:-5]
			# print ("after" + line)
			b = line.split(',')
			# print  (b)
			if(len(b) >= 4):
				bx = int(b[0])
				by = int(b[1])
				bz = int(b[2])
				b1 = b[3]
				b2 = b[4]
				# print (bx)

# 


	# Pass the global values into the keystroke controllers

	# acceleration_controller(ax, ay, az, bx, by, bz)
	# lh_controller(a1, a2)
	# rh_controller(b1, b2)




