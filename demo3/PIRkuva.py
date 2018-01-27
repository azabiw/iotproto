import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
pin = 24
GPIO.setup(pin, GPIO.IN)

loppu = time.time() + 40
while time.time() < loppu:
    i=GPIO.input(pin)
    if i==1:
        print "Liiketta havaittu.  Otetaan kuva"
        os.system("raspistill -o kuva.jpg")
    time.sleep(0.1)

GPIO.cleanup()
