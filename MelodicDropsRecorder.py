#!/usr/bin/python

import pygame, sys, time, os
from pygame.locals import *

def recordDrops(audioFile):
	#set de vars
	frequency = 44100
	bitsize = -16
	channels = 2
	_buffer = 1024
	framerate = 30
	speed = 1
	width = 1000
	bgcolor = 0, 0, 0
	events = []
	i = 5

	#stel scherm in en programklok
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	playSurface = pygame.display.set_mode((width, 100))
	pygame.display.set_caption('Recorder')
	clock = pygame.time.Clock()

	#init mixer
	pygame.mixer.init(int(frequency * speed), bitsize, channels, _buffer)

	#check de lengte in ms
	a = pygame.mixer.Sound(audioFile)
	length = int(a.get_length()* 1000)

	#Laad de audio
	pygame.mixer.music.load(audioFile)

	#countdown
	print 'We beginnen in:'
	while i >= 0:
		time.sleep(1)
		print(i)
		i -= 1

	#spelen maar!
	pygame.mixer.music.play()

	#tijdens het spelen loop
	while pygame.mixer.music.get_busy():
		clock.tick(framerate)
		playSurface.fill(bgcolor)
		for x in events:
			currentPix = int(x / float(length) * width)
			pygame.draw.line(playSurface, (255,255,255), (currentPix, 0), (currentPix, 100))
		currentPix = int(pygame.mixer.music.get_pos() / float(length) * width)
		pygame.draw.line(playSurface, (255,0,0), (currentPix, 0), (currentPix, 100))	
		
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					events.append(pygame.mixer.music.get_pos())
					current = events[len(events)-1]
					print current
		pygame.display.flip()

	#Bestand opslaan
	f = open(audioFile.partition('.')[0] + '.drops', 'w')
	f.write(str(length))
	f.write("\n")
	f.write(str(-100))
	f.write("\n")
	for i in events:
		f.write(str(i))
		f.write(", \n")
	print f
	f.close()
