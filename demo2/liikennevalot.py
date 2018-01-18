import RPi.GPIO as GPIO
import time
jVihLED=17
jPunLED=4
AVihLED=16
AKelLED=12
APunLED=25
PAINIKE=6
JSigLED=21

GPIO.setmode (GPIO.BCM)
GPIO.setup (jVihLED, GPIO.OUT)
GPIO.setup (jPunLED, GPIO.OUT)
GPIO.setup (AVihLED, GPIO.OUT)
GPIO.setup (AKelLED, GPIO.OUT)
GPIO.setup (APunLED, GPIO.OUT)
GPIO.setup (PAINIKE, GPIO.IN)
GPIO.setup (JSigLED, GPIO.IN)


loppu = time.time() + 20
while time.time() < loppu:
      GPIO.output(AVihLED, 1)
      GPIO.output(jPunLED,1)
      if(GPIO.input(PAINIKE)==1):
          GPIO.output(AVihLED,0)
          GPIO.output(AKelLED,1)
          GPIO.output(JSigLED,1)
          time.sleep(2)
          GPIO.output(AKelLED,0)
          GPIO.output(jPunLED,0)
          GPIO.output(APunLED,1)
          GPIO.output(jVihLED,1)
          GPIO.output(JSigLED,0)
          time.sleep(3)
          GPIO.output(jVihLED,0)
          GPIO.output(APunLED,0)
          GPIO.output(AKelLED,1)
          GPIO.output(jPunLED,1)
          time.sleep(2)
          GPIO.output(AKelLED,0)
      time.sleep (0.1) # ilman tata prossukaytto 100%

GPIO.cleanup ()
