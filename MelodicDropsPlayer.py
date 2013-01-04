#!/usr/bin/python

import sys, pygame, serial
from time import sleep

def toInt( d ):
		var = 0
		if int(d[0]) == 1:
			var = 1
		if int(d[1]) == 1:
			var = var + 2
		if int(d[2]) == 1:
			var = var + 4
		if int(d[3]) == 1:
			var = var + 8
		if int(d[4]) == 1:
			var = var + 16
		if int(d[5]) == 1:
			var = var + 32
		if int(d[6]) == 1:
			var = var + 64
		if int(d[7]) == 1:
			var = var + 128
		return var

def playDrops(audioFile):
	#set de vars
	frequency = 44100
	bitsize = -16
	channels = 2
	_buffer = 1024
	framerate = 30
	events = []
	command = []
	serialDevice = '/dev/ttyUSB0'
	baudRate = 19200
	#audioFile = sys.argv[1]
	#audioFile = 'tune.ogg'
	dropsFile = audioFile.partition('.')[0] + '.drops'

	serialLink = serial.Serial(serialDevice, baudRate)
	serialLink.write('' + chr(1) + chr(0) + chr(0) + chr(0))
	sleep(0.1)

	f = open(dropsFile, 'r')
	data = f.readlines()
	length = data.pop(0)
	shift = int(data.pop(0))

	for i in data:
		t = i.partition(', ')
		events.append(int(t[0]))
		command.append(toInt(t[2]))

	total = len(events)
	toDo = total

	pygame.mixer.init(frequency, bitsize, channels, _buffer)

	clock = pygame.time.Clock()
	pygame.mixer.music.load(audioFile)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		clock.tick(framerate)
		while toDo > 0:
			if events[total-toDo] < pygame.mixer.music.get_pos() + shift:
				print events[total-toDo]
				serialLink.write('' + chr(3) + chr(0) + chr(command[total-toDo]) + chr(3 ^ 0 ^ command[total-toDo]))
				toDo -= 1
	serialLink.write('' + chr(3) + chr(0) + chr(0) + chr(3 ^ 0 ^ 0))
