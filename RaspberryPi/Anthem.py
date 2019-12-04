#Frequency credits : https://mypianonotes.com/indian-national-anthem/

import RPi.GPIO as GPIO
import signal
import time
import sys

redLED,whiteLED,greenLED = 21,20,16

BUZZER = 23

redState,whiteState,greenState = True,False,False

notes = "cdeeeeeeeeedef eeedddbdc ccgggggggggaf fffffeddf eedeedeggaff eeeeeddbdc cdeeeedf efgggfedfe feeeddbdc ccggggeggggga fffffedfe egc bab aga ccddeedef "

beats = [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1,
                2, 1, 1, 2, 1, 1, 1, 1, 1, 1,
                2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1,
                2, 1, 1, 2, 1, 1, 1, 1, 1, 1,
                2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1,
                2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1,
                1, 1, 1, 1, 2, 2, 2, 1, 1,
                1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1,
                2, 2, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1,
                2, 1, 1, 2, 1, 1, 1, 1, 1, 1,
                1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 4, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 4, 1 ]

notesDict = {'c':1915, 'd':1700, 'e':1519, 'f':1432, 'g':1275, 'a':1136, 'b':1014, 'C':956 }

tempo = 390

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(redLED, GPIO.OUT)
GPIO.setup(whiteLED, GPIO.OUT)
GPIO.setup(greenLED, GPIO.OUT)


def signalHandler(sig,frame):
        GPIO.output(BUZZER,False)
        GPIO.output(redLED,False)
        GPIO.output(whiteLED,False)
        GPIO.output(greenLED,False)
        sys.exit(0)

signal.signal(signal.SIGINT,signalHandler)

def buzz(noteFreq, duration):
    GPIO.output(redLED,redState)
    GPIO.output(whiteLED,whiteState)
    GPIO.output(greenLED,greenState)

    for i in range(0,duration,noteFreq*2):
       GPIO.output(BUZZER, True)
       time.sleep(noteFreq/1000000)
       GPIO.output(BUZZER, False)
       time.sleep(noteFreq/1000000)

for i in range(0,len(notes)):
	if notes[i] == ' ':
		time.sleep(beats[i]*tempo/1000)
	else:
		buzz(notesDict[notes[i]],beats[i]*tempo*1000)
		redState,whiteState,greenState = i%3==0,(i+1)%3==0,(i+2)%3==0

GPIO.output(redLED,True)
GPIO.output(whiteLED,True)
GPIO.output(greenLED,True)
