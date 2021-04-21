#!/usr/bin/python
import time
import grovepi
import mail
import os, sys, signal

# Connection des capteurs a chaque ports

relay = 7
water_sensor = 6
led = 4
buzzer = 5
ultrasonic_ranger = 2

# Initialisation des variables  

result = [500]*3 #Initialisation d'un tableau de 3 valeurs : [500, 500, 500]
alight = False #Booleen pour savoir si la led est allumee ou non 

# Initialisation des ports en tant qu'entree ou sortie 
grovepi.pinMode(water_sensor,"INPUT")
grovepi.pinMode(led,"OUTPUT")
grovepi.pinMode(buzzer,"OUTPUT")
grovepi.pinMode(relay,"OUTPUT")
grovepi.pinMode(ultrasonic_ranger,"INPUT")
                                                                                                                                            
# Definition d'une action a effectuer lors de la reception du signal d'interruption 
def fin_signal_INTERRUPTION(sig,ignore):
        print("\nquelqu'un vient de m'interrompre\n")
        grovepi.digitalWrite(relay,0)
        sys.exit()

# Indique au programme d'ecouter le signal d'interruption 
signal.signal(signal.SIGINT, fin_signal_INTERRUPTION)

# Fonctions: utilisation de tableau de valeur pour le capteur ultrason 
def addValue(tab,val):
	# Ajoute une valeur au tableau : le tableau garde toujours que 3 valeurs 
        tab[0]=tab[1]
        tab[1]=tab[2]
        tab[2]=val
        return tab

def mean(tab):
	# Fait la moyenne des valeurs du tableau 
        sum=0
        for i in tab:
        	sum+=i
        return sum/len(tab)

# Programme principal 
while True: 
	try : 
		# On regarde si le niveau d'eau est suffisant
		print(grovepi.digitalRead(water_sensor))
		if grovepi.digitalRead(water_sensor)==1:
			# s'il ne l'ai pas on verifie si la led est deja allumee 
                	if not alight:
				# si elle ne l'ai pas on previent l'utilisateur que le niveau d'eau est trop faible 
                        	mail.sendMail("leobrunet91@gmail.com","Attention, le niveau d'eau  de votre fontaine est bas. Il faut la remplir.")
                        	grovepi.digitalWrite(led,1)
                        	alight = True
                        	grovepi.digitalWrite(buzzer,1)
                        	time.sleep(0.1)
                       		grovepi.digitalWrite(buzzer,0)
			# Sinon on ne fait rien : l'utilisateur est deja prevenu 
        	else:
			# le niveau d'eau est suffisant : la led doit etre eteinte 
                	grovepi.digitalWrite(led,0)
                	alight = False
			time.sleep(.5)

 		# On lit les valeurs du capteur ultrason 
        	val = grovepi.ultrasonicRead(ultrasonic_ranger)
		if val!= 65535:
			# parfois une mauvaise valeur est retourne, pour eviter que cela fausse notre programme on l'evite
                	addValue(result,val)
                	print(val)
        	if mean(result)<20 :
			# si la moyenne des valeurs est inferieur a 20cm on active la pompe 
                	grovepi.digitalWrite(relay,1)
                	time.sleep(10) #on laisse la pompe active pendant 10secondes
                	grovepi.digitalWrite(relay,0)
                	result = [500]*3 #reinnitialisation des valeurs a une distance importante pour pas que la pompe ne se reactive direct sans raison 
			
	except IOError:
        	print ("Error")

