#!/usr/bin/python

import sys
import serial
from time import sleep

serialLink = serial.Serial("/dev/ttyUSB0", 19200)

var = 0

if int(sys.argv[1]) == 1:
	var = 1
if int(sys.argv[2]) == 1:
	var = var + 2
if int(sys.argv[3]) == 1:
	var = var + 4
if int(sys.argv[4]) == 1:
	var = var + 8
if int(sys.argv[5]) == 1:
	var = var + 16
if int(sys.argv[6]) == 1:
	var = var + 32
if int(sys.argv[7]) == 1:
	var = var + 64
if int(sys.argv[8]) == 1:
	var = var + 128

print 'AAAAAAAAAAAAAAAA', var

serialLink.write('' + chr(1) + chr(0) + chr(0) + chr(0))

sleep(0.1)

serialLink.write('' + chr(3) + chr(0) + chr(var) + chr(3 ^ 0 ^ var))

