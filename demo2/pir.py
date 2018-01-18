import RPi.GPIO as GPIO
import time
# kurssin malliskripti
GPIO.setmode(GPIO.BCM)

# Luetaan pinnissä 11 kiinni olevaa PIR sensoria.
GPIO.setup(11, GPIO.IN)

loppu = time.time() + 10
while time.time() < loppu:
    i=GPIO.input(11)
    if i==0:
        print "Ei havaita liikettä"
        time.sleep(0.1)
    elif i==1:
        print "Liikettä havaittu"
        time.sleep(0.1)

GPIO.cleanup()
