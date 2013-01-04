#!/usr/bin/python

import sys
import MelodicDropsRecorder
import MelodicDropsPlayer
import MelodicDropsSet
import MelodicDropsEditor

if sys.argv[1] == 'record':
	MelodicDropsRecorder.recordDrops(sys.argv[2])
	
if sys.argv[1] == 'edit':
	MelodicDropsEditor.editDrops(sys.argv[2])

if sys.argv[1] == 'play':
	MelodicDropsPlayer.playDrops(sys.argv[2])
	
if sys.argv[1] == 'set':
	MelodicDropsSet.setDrops([sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9]])

if sys.argv[1] == 'clear':
	MelodicDropsSet.setDrops([0, 0, 0, 0, 0, 0, 0, 0])
