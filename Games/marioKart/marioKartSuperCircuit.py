"""Small example OSC server
This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import math

import pyautogui


# Mario Kart Super Circuit
#https://emulatoronline.com/gba-games/mario-kart-super-circuit/


pyautogui.PAUSE = .5

from pythonosc import dispatcher
from pythonosc import osc_server

def print_test(arg1, arg2, arg3, arg4, arg5):
	try:
		print(str(arg1) + str(arg2) + str(arg3) + str(arg4) + str(arg5))
	except ValueError: pass

def keystroke_controller(wek_outputs, accLH, buttonsLH, accRH, buttonsRH):
	try:
		# ACCELEROMETER LEFT HAND
		# first set of classes
		print (accLH)

		if(accLH == 1):
			# print ("restLH")
			pass
		elif(accLH == 2):
			# while (accLH == 2):
			pyautogui.keyDown('left')
			
			# print ("up")
		elif(accLH == 3):
			pyautogui.keyDown('right')
		pyautogui.keyUp('left')
		pyautogui.keyUp('right')
		# BUTTONS LEFT HAND	
		# second set of classes
		if(buttonsLH == 1):
			# print ("restLHB")
			pass
		elif(buttonsLH == 2):
			pyautogui.keyDown('a')
			pyautogui.keyUp('a')
			# print ("pin0")
		elif(buttonsLH == 3):
			pyautogui.keyDown('d')
			pyautogui.keyUp('d')
			# print ("pin1")

		# BUTTONS RIGHT HAND
		# fourth set of classes
		if(buttonsRH == 1):
			# print ("restRHB")
			pass
		elif(buttonsRH == 2):
			pyautogui.keyDown('z')
			pyautogui.keyUp('z')
			# print ("pin0")
		elif(buttonsRH == 3):
			pyautogui.keyDown('x')
			pyautogui.keyUp('x')
			# print ("pin1")
	except ValueError: pass


if __name__ == "__main__":
	#Listen into an OSC port
	parser = argparse.ArgumentParser()
	parser.add_argument("--ip",
	  default="127.0.0.1", help="The ip to listen on")
	parser.add_argument("--port",
	  type=int, default=9999, help="The port to listen on")
	args = parser.parse_args()

	dispatcher = dispatcher.Dispatcher()
	dispatcher.map("/gameController", keystroke_controller)

	# pyautogui.typewrite('Hello world!', interval=0.25)

	server = osc_server.ThreadingOSCUDPServer(
	  (args.ip, args.port), dispatcher)
	print("Serving on {}".format(server.server_address))
	server.serve_forever()