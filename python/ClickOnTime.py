#!/usr/bin/python

import time

kaas = True

events = [1, 1.5, 6.5]

beginTime = time.time()
print 'begin'

while kaas:
	for x in events:
		if time.time() > x + beginTime:
			print x
			del(events[x-1])
