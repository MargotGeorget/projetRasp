#!/usr/bin/python
import time
import grovepi
import mail
import os, sys, signal

# Connect the Grove Button to digital port D3
# SIG,NC,VCC,GND
mail.sendMail('leobrunet91@gmail.com','Programme lance')
button = 8
relay = 4
alight = False
etatButton = 0

def fin_signal_INTERRUPTION(sig,ignore):
        print("\nquelqu'un vient de m'interrompre je suis button\n")
	grovepi.digitalWrite(relay,0)
	sys.exit()

signal.signal(signal.SIGINT, fin_signal_INTERRUPTION)
   

grovepi.pinMode(button,"INPUT")
grovepi.pinMode(relay,"OUTPUT")
#grovepi.digitalWrite(relay,0)

while True:
        try:
                time.sleep(0.3)
                etatButton = grovepi.digitalRead(button)
		print(str(etatButton)) 
                if etatButton == 1:
			print("j'ai appuye sur le bouton pelo")
                        grovepi.digitalWrite(relay,1)
                        time.sleep(10)
                	grovepi.digitalWrite(relay,0)
	except IOError:
                print ("Error")


