import RPi.GPIO as GPIO
import time


servoPIN = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)



p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization

def set_angle(angle):
	duty = angle / 18 + 2
	GPIO.output(servoPIN, True)
	p.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.output(servoPIN, False)
	p.ChangeDutyCycle(0)
try:
  while True:
    set_angle(0)
    time.sleep(0.5)
    set_angle(45)
    time.sleep(0.5)
    set_angle(90)
    time.sleep(0.5)
    set_angle(135)
    time.sleep(0.5)
    set_angle(180)
    time.sleep(0.5)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()