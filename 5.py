import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
p=GPIO.PWM(21,1000)
p.start(0)
time.sleep(0.2)
p.ChangeDutyCycle(44)
time.sleep(0.2)
p.ChangeFrequency(950)
time.sleep(0.2)
p.ChangeFrequency(900)
time.sleep(0.2)
p.ChangeFrequency(850)
time.sleep(0.2)
p.ChangeFrequency(550)
time.sleep(0.2)
p.ChangeFrequency(700)
time.sleep(0.2)
p.ChangeFrequency(800)
time.sleep(0.2)
p.ChangeFrequency(900)
time.sleep(0.2)
p.ChangeFrequency(1000)
time.sleep(0.2)
p.stop()
GPIO.cleanup()
