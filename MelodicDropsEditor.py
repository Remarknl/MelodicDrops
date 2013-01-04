#!/usr/bin/python

import pygame, sys, time, os
from pygame.locals import *





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

def editDrops(audioFile):
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.init()
	clock = pygame.time.Clock()

	pygame.key.set_repeat(300, 50)
	surface = pygame.display.set_mode((1010, 500))
	pygame.display.set_caption('Melodic Drops Editor - Richard Ginus')
	dropsFile = audioFile.partition('.')[0] + '.drops'
	font = pygame.font.Font('freesansbold.ttf', 18)

	#set de vars
	bgcolor = 200, 200, 200
	blauw = 0, 0, 200
	zwart = 0, 0, 0
	width = 1000
	events = []
	command = []
	rawCommand = []
	i = 5
	framerate = 30
	selectedClick = 0
	currentCommand = ''
	frequency = 44100
	bitsize = -16
	channels = 2
	_buffer = 1024
	speed = 1
	
	#init mixer
	pygame.mixer.init(int(frequency * speed), bitsize, channels, _buffer)

	#check de lengte in ms
	a = pygame.mixer.Sound(audioFile)
	length = int(a.get_length()* 1000)

	#Laad de audio
	pygame.mixer.music.load(audioFile)

	#spelen maar!
	#
	
	#tijdens het spelen loop
	#while pygame.mixer.music.get_busy():

	try:
		f = open(dropsFile, 'r')
		data = f.readlines()
	except:
		f = open(audioFile.partition('.')[0] + '.drops', 'w')
		f.close()
		data = ['0','0','0, ']
		shift = 0	
	
	#print data.pop(0)
	shift = int(data.pop(0))

	for i in data:
		t = i.partition(', ')
		events.append(int(t[0]))
		if len(t[2]) != 9:
			command.append(toInt('00000000'))
			rawCommand.append('00000000'[0:8])

		else:
			command.append(toInt(t[2]))
			rawCommand.append(t[2][0:8])
	
	
	while True:
		if len(events) != len(command):
			command.append(toInt('00000000'))
			rawCommand.append('00000000'[0:8])

		surface.fill(bgcolor)
		pygame.draw.rect(surface, (0, 0, 0), (5, 5, width, 105))

		#teken geplaatste lijnen
		for x in events:
			currentX = int(x / float(length) * width)
			pygame.draw.line(surface, (255,255,255), (currentX+5, 5), (currentX+5, 110))
		
		#teken cursor
		currentPix = int(events[selectedClick] / float(length) * width)
		pygame.draw.line(surface, (255,0,0), (currentPix+5, 5), (currentPix+5, 110))
		
		#teken speelding
		currentPix = int(pygame.mixer.music.get_pos() / float(length) * width)
		pygame.draw.line(surface, (0,255,0), (currentPix+5, 5), (currentPix+5, 110))
			
		#info
		codeText = font.render(str('commando: ' + rawCommand[selectedClick]), False, blauw)
		surface.blit(codeText, (10, 120))
		codeText = font.render(str('wordt: ' + currentCommand), False, blauw)
		surface.blit(codeText, (57, 140))
		codeText = font.render(str('seconden: ' + str(float(events[selectedClick])/1000)), False, blauw)
		surface.blit(codeText, (10, 160))
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					if events[0] == 0:
						events.pop(0)
						events.append(pygame.mixer.music.get_pos())
					else:
						events.append(pygame.mixer.music.get_pos())
					current = events[len(events)-1]
					print current
				if event.key == K_s:
					#Bestand opslaan
					y = 0				
					while y < len(events):
						if events[y] < events[y-1]:
							t = events.pop(y)
							r = command.pop(y)
							u = rawCommand.pop(y)
							events.insert(y-1, t)
							command.insert(y-1, r)
							rawCommand.insert(y-1, u)
							y = 0
						print events[y]
						y += 1
					
					
					
					f = open(audioFile.partition('.')[0] + '.drops', 'w')
					f.write(str(length))
					f.write("\n")
					f.write(str(0))
					f.write("\n")
					y = 0				
					while y < len(events):
						f.write(str(events[y]))
						f.write(", ")
						f.write(rawCommand[y])
						f.write('\n')
						y += 1
					f.close()				
					print 'Opgeslagen'
				if event.key == K_p:
					print 'play'
					pygame.mixer.music.play()
				if event.key == K_DELETE:
					print 'deleted'
					events.pop(selectedClick)
					command.pop(selectedClick)
					rawCommand.pop(selectedClick)
				if event.key == K_LEFT:
					if selectedClick > 0:
						selectedClick -= 1
				if event.key == K_RIGHT:
					if selectedClick < len(events)-1:
						selectedClick += 1
				if event.key == K_DOWN:
					if event.key == K_LSHIFT:
						events[selectedClick] -= 100
					else:
						events[selectedClick] -= 1
				if event.key == K_UP:
					if event.key == K_LSHIFT:
						events[selectedClick] += 100
					else:
						events[selectedClick] += 1
				if event.key == K_1:
					if len(currentCommand) < 7:
						currentCommand = currentCommand + '1'
					else:
						currentCommand = currentCommand + '1'
						command[selectedClick] = toInt(currentCommand)
						rawCommand[selectedClick] = currentCommand[0:8]
						currentCommand = ''
				if event.key == K_0:
					if len(currentCommand) < 7:
						currentCommand = currentCommand + '0'
					else:
						currentCommand = currentCommand + '0'
						command[selectedClick] = toInt(currentCommand)
						rawCommand[selectedClick] = currentCommand[0:8]
						currentCommand = ''
		pygame.display.update()
		clock.tick(framerate)
