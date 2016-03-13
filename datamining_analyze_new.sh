#!/bin/sh


awk -F"[ :]" '{all[$5]++; if ($(NF-2)==200) succes[$5]++} END {for (hour in all) printf " per hour (%d) # succes req - %d,  in percent - %.1f%\n", hour, succes[hour], succes[hour]/all[hour]*100}' datamining.log > results.txt
