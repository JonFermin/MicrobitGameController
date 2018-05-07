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
		pyautogui.keyDown('left')
	elif (LHaccx <= rightTilt and RHaccx <= rightTilt):
		pyautogui.keyDown('right')
	elif ((LHaccx > rightTilt and RHaccx > rightTilt) or(LHaccx < leftTilt and RHaccx < leftTilt)):
		pyautogui.keyUp('left')
		pyautogui.keyUp('right')

def lh_controller(LHbutton1, LHbutton2):
	leftButton1 = 'x'
	leftButton2 = 'a'
	if LHbutton1 == "1":
		print("LB1")
		pyautogui.keyDown(leftButton1)
	else:
		pyautogui.keyUp(leftButton1)
	if LHbutton2 == "1":
		print("LB2")
		pyautogui.keyDown(leftButton2)

	else:
		pyautogui.keyUp(leftButton2)
		# print("off")

def rh_controller(RHbutton1, RHbutton2):
	# print (RHbutton1 + RHbutton2)
	rightButton1 = 'd'
	rightButton2 = 'z'
	if RHbutton1 == "1":
		print("RB1")
		pyautogui.keyDown(rightButton1)
	else:
		pyautogui.keyUp(rightButton1)
	if RHbutton2 == "1":
		print("RB2")
		pyautogui.keyDown(rightButton2)
		# print(rightButton2)
	else:
		pyautogui.keyUp(rightButton2)


# First Microbit
# ax = 0
# ay = 0
# az = 0
# a1 = 0
# a2 = 0

# bx = 0
# by = 0
# bz = 0
# b1 = 0
# b2 = 0


# def run_controller():
# 	while True:
# 		# print("hit")
# 		acceleration_controller(ax, ay, az, bx, by, bz)
# 		lh_controller(a1, a2)
# 		rh_controller(b1, b2)

# run_thread = Thread(target=run_controller, args = ())
# run_thread.start()

if __name__ == "__main__":
	# Data comes in looking like this:
	# b'a530,503,253,0,0              \r\n'
	# b'b409,448,273,0,0              \r\n'
	# b'a526,503,249,0,0              \r\n'

	# To format this in a way that we can use it
	ser = serial.Serial("/dev/cu.usbmodem1422", 115200)
	while True:
		# convert from bytes to a string

		line = str(ser.readline());
		print(line)
		if line:
			# if the character coming in is an a
			# we want to set it to a certain value
			# a = [0,0,0,0,0]
			# b = [0,0,0,0,0]
			if (line[2] == "a"): 
				# remove the b'a
				# print (line)
				line = line.replace("b'a", "") 
				# remove the trailing \r\n' at the end
				line = line[:-5] 
				# left with 409,448,273,0,0
				a = line.split(",")
				# split creates an array delimited by a comma
				# set these to the global values


				# ax = int(a[0])
				# ay = int(a[1])
				# az = int(a[2])
				# a1 = a[3]
				# a2 = a[4].replace(" ", "")
				# print (a[4])
				lh_controller(a[3], a[4].replace(" ", ""))
			elif (line[2] == "b"):
				# print("before" + line)
				line = line.replace("b'b", "")
				line = line[:-5]
				# print ("after" + line)
				b = line.split(',')
				# print (b)
				# bx = int(b[0])
				# by = int(b[1])
				# bz = int(b[2])
				# b1 = b[3]
				# b2 = b[4].replace(" ", "")
				rh_controller(b[3], b[4].replace(" ", ""))
			# acceleration_controller(int(a[0]),int(a[1]), int(a[2]), int(b[0]), int(b[1]), int(b[2]))
		# Pass the global values into the keystroke controllers



