#!/usr/bin/python

import sys
import serial
from time import sleep

def setDrops(arguments):
	serialLink = serial.Serial("/dev/ttyUSB0", 19200)
	var = 0
	if int(arguments[0]) == 1:
		var = 1
	if int(arguments[1]) == 1:
		var = var + 2
	if int(arguments[2]) == 1:
		var = var + 4
	if int(arguments[3]) == 1:
		var = var + 8
	if int(arguments[4]) == 1:
		var = var + 16
	if int(arguments[5]) == 1:
		var = var + 32
	if int(arguments[6]) == 1:
		var = var + 64
	if int(arguments[7]) == 1:
		var = var + 128

	serialLink.write('' + chr(1) + chr(0) + chr(0) + chr(0))
	sleep(0.1)
	serialLink.write('' + chr(3) + chr(0) + chr(var) + chr(3 ^ 0 ^ var))
	print 'done'
