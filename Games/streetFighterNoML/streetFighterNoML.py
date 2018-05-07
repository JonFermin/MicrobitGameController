# Jonathan Fermin
# Street Fighter
# https://emulatoronline.com/gba-games/mario-kart-super-circuit/

import serial
import pyautogui
from threading import Thread
import time
# pyautogui.PAUSE = .5 
# set a pause between each keystroke function


def acceleration_controller(LHaccx, LHaccy, LHaccz, RHaccx, RHaccy, RHaccz):
	# print("acc")
	# find break points here by printing out data and finding when the tilt becomes too much
	# leftTilt = 600 
	# rightTilt = 400
	# upper:
	uppery =  50
	upperz = 700

	# hook:
	hookx = 100
	hooky =  100

	Lhookx = 700
	Lhooky = 700

	# straight:
	straightx = 400
	straighty = 150
	straightz = 400

	straighty2 = 800
	straightz2 = 650

	print (str(RHaccx) + "," + str(RHaccy) + "," + str(RHaccz))
	# print (str(LHaccx) + "," + str(LHaccy) + "," + str(LHaccz))

	if (RHaccy < uppery and RHaccz > upperz):
		print("YA")
	elif (RHaccx < hookx and RHaccy < hooky):
		print("BA")
	elif ((RHaccx < straightx and RHaccy < straighty) or (RHaccy > straighty2 and RHaccz > straightz2)) :
		print("NA")
	# if (LHaccy < uppery and LHaccz > upperz):
	# 	print("YA")
	# elif (LHaccx > Lhookx and LHaccy > Lhooky):
	# 	print("BA")
	# elif (LHaccx > straightx and LHaccy < straighty and LHaccz < straightz):
	# 	print("NA")


	

def lh_controller(LHbutton1, LHbutton2):
	leftButton1 = 'x'
	leftButton2 = 'a'
	if LHbutton1 == "1":
		pyautogui.keyDown(leftButton1)
		print("lb1")
				# print(leftButton1)
	else:
		pyautogui.keyUp(leftButton1)
		# print("off")
	if LHbutton2 == "1":
		pyautogui.keyDown(leftButton2)
		print("lb2")
		# print(leftButton2)
	else:
		pyautogui.keyUp(leftButton2)
		# print("off")

def rh_controller(RHbutton1, RHbutton2):
	# print (RHbutton1 + RHbutton2)
	rightButton1 = 'd'
	rightButton2 = 'z'
	if RHbutton1 == "1":
		pyautogui.keyDown(rightButton1)
		print("rb1")
		# print("off")
	else:
		pyautogui.keyUp(rightButton1)
	if RHbutton2 == "1":
		pyautogui.keyDown(rightButton2)
		print("rb2")
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

	# print(a1, ",", a2, ",", b1, ",", b2)
	while True:
		# print(bx)
		# print(a1, a2)
		# print(b1, b2) 
		acceleration_controller(ax, ay, az, bx, by, bz)
		# lh_controller(a1, a2)
		# rh_controller(b1, b2)
		time.sleep(.1)

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

	line = str(ser.readline())
	# print(line)
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

			# print (str(bx) + "," + str(by) + "," + str(bz))

# 


	# Pass the global values into the keystroke controllers

	# acceleration_controller(ax, ay, az, bx, by, bz)
	# lh_controller(a1, a2)
	# rh_controller(b1, b2)




