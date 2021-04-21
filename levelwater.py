#!/usr/bin/python
import mail
import time
import grovepi
import os, sys, signal
# Connect the Grove Water Sensor to digital port D2
# SIG,NC,VCC,GND
water_sensor = 6
led = 4
alight = False
buzzer = 5

grovepi.pinMode(water_sensor,"INPUT")
grovepi.pinMode(led,"OUTPUT")
grovepi.pinMode(buzzer,"OUTPUT")

def fin_signal_INTERRUPTION(sig,ignore):
        print("\nquelqu'un vient de m'interrompre je suis levelWatern\n")
        grovepi.digitalWrite(led,0)
	grovepi.digitalWrite(buzzer,0)
        sys.exit()

signal.signal(signal.SIGINT, fin_signal_INTERRUPTION)

while True:
    try:
        if grovepi.digitalRead(water_sensor)==1:
		if not alight:
			mail.sendMail("leobrunet91@gmail.com","Attention, le niveau d'eau  de votre fontaine est bas. Il faut la remplir.")
			grovepi.digitalWrite(led,1)
                	alight = True
        		grovepi.digitalWrite(buzzer,1)
                	time.sleep(0.1)
			grovepi.digitalWrite(buzzer,0)
	else: 
		grovepi.digitalWrite(led,0)
                alight = False
        time.sleep(.5)

    except IOError:
        print ("Error")
