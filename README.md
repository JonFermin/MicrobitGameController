# Microbit Game Controller
By using OSC messages, radio communication, and data through serial ports, this project creates a game controller out of the microbit. 

## Microbit Pseudocode
The microbit just sends the accelerometer data through radio and button presses.
```typescript
	let msg = ""
	basic.showString("A")
		//prints out A on the LED's on the microbit
	radio.setGroup(1)
	radio.setTransmitPower(7)
	basic.forever(() => {
	msg = accx + accy + accz + button1 + button2
	radio.sendString(msg)
	basic.pause(1) 
		//compensates for the hardware
	})
	
```

## Python Script
The way the python script controls the OSC messages and converts them into keystrokes is by using a library called pyautogui

```python
	import pyautogui
	if(accLH == 1):
			print ("rest")
		elif(accLH == 2):
			pyautogui.keyDown('up')
            pyautogui.keyUp('up')
			print ("up")
```
The serial library parses through the port and records the variables based upon the initial character.

```python
	ser = serial.Serial("/dev/cu.usbmodem1422", 115200, timeout = 1)
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
```
Then breakpoints are set in order to find certain actions that the user is doing through the accelerometer
```python
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
```
