"""Small example OSC server
This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import math

import pyautogui

from pythonosc import dispatcher
from pythonosc import osc_server

def print_test(arg1, arg2, arg3, arg4, arg5, arg6):
	try:
		print( str(arg2) + str(arg3) + str(arg4) + str(arg5) + str(arg6))
	except ValueError: pass

def keystroke_controller(wek_outputs, accLH, buttonsLH, accRH, buttonsRH):
	try:
		# ACCELEROMETER LEFT HAND
		# first set of classes
		if(accLH == 1):
			print ("rest")
		elif(accLH == 2):
			pyautogui.keyDown('up')
            pyautogui.keyUp('up')
			print ("up")
		elif(accLH == 3):
			pyautogui.keyDown('down')
            pyautogui.keyUp('down')
			print ("down")
		elif(accLH == 4):
			pyautogui.keyDown('left')
            pyautogui.keyUp('left')
			print ("left")
		elif(accLH == 5):
			pyautogui.keyDown('right')
            pyautogui.keyUp('right')
			print ("right")

		# BUTTONS LEFT HAND	
		# second set of classes
		if(buttonsLH == 1):
			print ("rest")
		elif(buttonsLH == 2):
			pyautogui.keyDown('a')
            pyautogui.keyUp('a')
			print ("pin0")
		elif(buttonsLH == 3):
			pyautogui.keyDown('b')
            pyautogui.keyUp('b')
			print ("pin1")

		# ACCELEROMETER RIGHT HAND	
		# third set of classes
		if(accRH == 1):
			print ("rest")
		elif(accRH == 2):
			print ("buttonPush1")
		elif(accRH == 3):
			print ("buttonPush2")
		elif(accRH == 4):
			print ("buttonPush3")
		elif(accRH == 5):
			print ("buttonPush4")

		# BUTTONS LEFT HAND	
		# fourth set of classes
		if(buttonsLH == 1):
			print ("rest")
		elif(buttonsLH == 2):
			pyautogui.keyDown('c')
            pyautogui.keyUp('c')
			print ("pin0")
		elif(buttonsLH == 3):
			pyautogui.keyDown('d')
            pyautogui.keyUp('d')
			print ("pin1")


	except ValueError: pass


if __name__ == "__main__":
	#Listen into an OSC port
	parser = argparse.ArgumentParser()
	parser.add_argument("--ip",
	  default="127.0.0.1", help="The ip to listen on")
	parser.add_argument("--port",
	  type=int, default=12001, help="The port to listen on")
	args = parser.parse_args()

	dispatcher = dispatcher.Dispatcher()
	dispatcher.map("/wek/outputs", keystroke_controller)

	pyautogui.typewrite('Hello world!', interval=0.25)

	server = osc_server.ThreadingOSCUDPServer(
	  (args.ip, args.port), dispatcher)
	print("Serving on {}".format(server.server_address))
	server.serve_forever()
