#!/usr/bin/python
import grovepi
import time
import os, sys, signal 
# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
 
ultrasonic_ranger = 2
result = [500]*3
relay = 4
grovepi.pinMode(relay,"OUTPUT")
grovepi.digitalWrite(relay,0)

def fin_signal_INTERRUPTION(sig,ignore):
        print("\nquelqu'un vient de m'interrompre je suis ultrasonic\n")
        grovepi.digitalWrite(relay,0)
        sys.exit()

signal.signal(signal.SIGINT, fin_signal_INTERRUPTION)

def addValue(tab,val):
	tab[0]=tab[1]
	tab[1]=tab[2]
	tab[2]=val
	return tab

def mean(tab):
	sum=0
	for i in tab:
		sum+=i
	return sum/len(tab)

while True:
    try:
        # Read distance value from Ultrasonic
        val = grovepi.ultrasonicRead(ultrasonic_ranger)
 	time.sleep(1)
	print result
	if val!= 65535:
		addValue(result,val)
		print val
	#print "Moyenne des valeurs" + str(mean(result))		
	if mean(result)<20 :
		grovepi.digitalWrite(relay,1)
		time.sleep(10)
		grovepi.digitalWrite(relay,0)
		result = [500]*3  
 
    #except TypeError as err:
       # print "TypeError : {0}".format(err)
    except IOError as err:
        print "IOError : {0}".format(err)
