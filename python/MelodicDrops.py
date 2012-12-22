#!/usr/bin/python

import sys
import serial
from time import sleep

serialLink = serial.Serial("/dev/ttyUSB0", 19200)

# var = int(sys.argv[1])
var = 1
print 'AAAAAAAAAAAAAAAA', var

serialLink.write('' + chr(1) + chr(0) + chr(0) + chr(0))

sleep(0.1)

while var < 256:
	print var	
	serialLink.write('' + chr(3) + chr(0) + chr(var) + chr(3 ^ 0 ^ var))
	var = var + 1
	sleep(1.0)
