import serial
ser = serial.Serial("/dev/cu.usbmodem1422", 115200)


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
while True:
	# line = io.TextIOWrapper(ser, newline="\r")

	line = str(ser.readline());
	if line:
		# print (str(line))
		# print (str(line)[2])
		if (line[2] == "a"): 
			# print("a")
			line = line.replace("b'a", "")
			line = line[:-5]
			a = line.split(",")
			ax = int(a[0])
			ay = int(a[1])
			az = int(a[2])
			a1 = bool(a[3])
			a2 = bool(a[4])
			# print (a2)
			# print(a[4])
		elif (line[2] == "b"):
			line = line.replace("b'b", "")
			b = line.split(',')
			bx = int(b[0])
			by = int(b[1])
			bz = int(b[2])
			b1 = bool(b[3])
			b2 = bool(b[4])
			print (bx)

ser.close()

