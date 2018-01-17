import RPi.GPIO as GPIO
import time

LED=4
PAINIKE=6

GPIO.setmode (GPIO.BCM)
GPIO.setup (LED, GPIO.OUT)
GPIO.setup (PAINIKE, GPIO.IN)

loppu = time.time() + 10
while time.time() < loppu:
      GPIO.output(LED, 1)
      time.sleep (1)
      GPIO.output(LED, 0)
      time.sleep (1)
GPIO.cleanup ()
