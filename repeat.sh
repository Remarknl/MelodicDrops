#!/bin/bash
c=1
while [ $c -le 5 ]
do
	./MelodicDrops.py play ~/Documenten/Drops/tune.ogg
	(( c++ ))
done
