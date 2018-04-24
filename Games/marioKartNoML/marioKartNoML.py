# Jonathan Fermin
# Mario Kart Super Circuit
# https://emulatoronline.com/gba-games/mario-kart-super-circuit/

import serial
import pyautogui
import sys
import glob
# pyautogui.PAUSE = .5 
# set a pause between each keystroke function

def acceleration_controller(LHaccx, LHaccy, LHaccz, RHaccx, RHaccy, RHaccz):
	# print("acc")
	# find break points here by printing out data and finding when the tilt becomes too much
	leftTilt = 600 
	rightTilt = 400
	if (LHaccx >= leftTilt and RHaccx >= leftTilt):
		print("left")
		pyautogui.keyDown('left')
	elif (LHaccx <= rightTilt and RHaccx <= rightTilt):
		print("right")
		pyautogui.keyDown('right')
	elif ((LHaccx > rightTilt and RHaccx > rightTilt) or(LHaccx < leftTilt and RHaccx < leftTilt)):
		pyautogui.keyUp('left')
		pyautogui.keyUp('right')
		




def lh_controller(LHbutton1, LHbutton2):
	leftButton1 = 'x'
	leftButton2 = 'a'
	if LHbutton1:
		pyautogui.keyDown(leftButton1)
	else:
		pyautogui.keyUp(leftButton1)
	if LHbutton2:
		pyautogui.keyDown(leftButton2)
	else:
		pyautogui.keyUp(leftButton2)



def rh_controller(RHbutton1, RHbutton2):
	rightButton1 = 'd'
	rightButton2 = 'z'
	if RHbutton1:
		pyautogui.keyDown(rightButton1)
	else:
		pyautogui.keyUp(rightButton1)
	if RHbutton2:
		pyautogui.keyDown(rightButton2)
	else:
		pyautogui.keyUp(rightButton2)

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

ser = serial.Serial("/dev/cu.usbmodem1422", 115200, timeout = 1)

if __name__ == "__main__":

	

	# Data comes in looking like this:
	# b'a530,503,253,0,0              \r\n'
	# b'b409,448,273,0,0              \r\n'
	# b'a526,503,249,0,0              \r\n'

	# To format this in a way that we can use it
	while True:
		# convert from bytes to a string
		line = str(ser.readline());
		if line:
			# if the character coming in is an a
			# we want to set it to a certain value
			if (line[2] == "a"): 
				# remove the b'a
				line = line.replace("b'a", "") 
				# remove the trailing \r\n' at the end
				line = line[:-5] 
				# left with 409,448,273,0,0
				a = line.split(",")
				# split creates an array delimited by a comma
				# set these to the global values
				ax = int(a[0])
				ay = int(a[1])
				az = int(a[2])
				a1 = bool(a[3])
				a2 = bool(a[4])
			elif (line[2] == "b"):
				line = line.replace("b'b", "")
				line = line[:-5]
				b = line.split(',')

				bx = int(b[0])
				by = int(b[1])
				bz = int(b[2])
				b1 = bool(b[3])
				b2 = bool(b[4])


		# Pass the global values into the keystroke controllers
		acceleration_controller(ax, ay, az, bx, by, bz);
		lh_controller(a1, a2)
		rh_controller(b1, b2)



