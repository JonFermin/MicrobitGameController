"""Small example OSC server
This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import math

import pyautogui


# Mario Kart Super Circuit
#https://emulatoronline.com/gba-games/mario-kart-super-circuit/


# pyautogui.PAUSE = .5

from pythonosc import dispatcher
from pythonosc import osc_server

def print_test(wek_outputs, LHaccx, LHaccy, LHaccz, LHbutton1, LHbutton2, RHaccx, RHaccy, RHaccz, RHbutton1, RHbutton2):
	try:
		print ("accx: " + str(RHaccx) + " accy: " + str(RHaccy) + " accz: " + str(RHaccz))
	except ValueError: pass

def keystroke_controller(wek_outputs, LHaccx, LHaccy, LHaccz, LHbutton1, LHbutton2, RHaccx, RHaccy, RHaccz, RHbutton1, RHbutton2):
	try:

		leftTilt = 600
		rightTilt = 400

		upTilt = 300
		downTilt = 700

		leftButton1 = ''
		leftButton2 = ''
		rightButton1 = ''
		rightButton2 = ''


		if (LHaccx >= leftTilt):
			print("left")
			pyautogui.keyDown('left')
		elif (LHaccx <= rightTilt ):
			print("right")
			pyautogui.keyDown('right')
		else:
			pyautogui.keyUp('left')
			pyautogui.keyUp('right')

		if (RHaccy <= upTilt):
			print("up")
			pyautogui.keyDown('up')
		elif (RHaccy >= downTilt):
			print("down")
			pyautogui.keyDown('down')
		else:
			pyautogui.keyUp('up')
			pyautogui.keyUp('down')

		if LHbutton1:
			pyautogui.keyDown(leftButton1)
		else:
			pyautogui.keyUp(leftButton1)
		if LHbutton2:
			pyautogui.keyDown(leftButton2)
		else:
			pyautogui.keyUp(leftButton2)

		if RHbutton1:
			pyautogui.keyDown(rightButton1)
		else:
			pyautogui.keyUp(rightButton1)
		if RHbutton2:
			pyautogui.keyDown(rightButton2)
		else:
			pyautogui.keyUp(rightButton2)
	except ValueError: pass


if __name__ == "__main__":
	#Listen into an OSC port
	parser = argparse.ArgumentParser()
	parser.add_argument("--ip",
	  default="127.0.0.1", help="The ip to listen on")
	parser.add_argument("--port",
	  type=int, default=6448, help="The port to listen on")
	args = parser.parse_args()

	dispatcher = dispatcher.Dispatcher()
	dispatcher.map("/wek/inputs", keystroke_controller)
	# dispatcher.map("/wek/inputs", print_test)

	server = osc_server.ThreadingOSCUDPServer(
	  (args.ip, args.port), dispatcher)
	print("Serving on {}".format(server.server_address))
	server.serve_forever()
