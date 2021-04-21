#!/usr/bin/python
#from levelWater import *
#from button import *
import os,sys,signal,time

def fin_signal_INTERRUPTION(sig,ignore):
	print("\nquelqu'un vient de m'interrompre\n")
	time.sleep(5)
	sys.exit()

signal.signal(signal.SIGINT, fin_signal_INTERRUPTION)

pid1 = os.fork()
if pid1 == 0:
	print("pid1")
	os.execv('./button.py', ('python', ' '))
pid2 = os.fork()
if pid2 == 0:
	print("pid2")
	os.execv('./levelwater.py', ('python', ' '))
pid3 = os.fork()
if pid3 == 0:
	print("pid3")
	os.execv('./ultrasonic.py', ('python', ' '))

for i in range(2):
	pid,status = os.wait()
	print("err")
