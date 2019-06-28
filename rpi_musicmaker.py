import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
p=GPIO.PWM(21,1000)
p.start(0)
p.ChangeDutyCycle(100)
time.sleep(3)
GPIO.cleanup()

