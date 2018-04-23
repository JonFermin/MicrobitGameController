# Microbit Game Controller
By using OSC messages, radio communication, data through serial ports, and machine learning, this project creates a game controller out of the microbit

## Code
The way the python script controls the OSC messages and converts them into 

```python
	if(accLH == 1):
			print ("rest")
		elif(accLH == 2):
			pyautogui.keyDown('up')
            pyautogui.keyUp('up')
			print ("up")
```