import RPi.GPIO as GPIO
from components.servo import ServoMotor
import time

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    servo = ServoMotor(3, -45, 45)
    servo.start()

try:
    while True:
        servo.set_angle(0)
        time.sleep(3)
        servo.set_angle(-45)
        time.sleep(3)
        servo.set_angle(0)
        time.sleep(3)
        servo.set_angle(45)
        time.sleep(3)
        # set_angle(45)
        # time.sleep(0.5)
        # set_angle(90)
        # time.sleep(0.5)
        # set_angle(135)
        # time.sleep(0.5)
        # set_angle(180)
        # time.sleep(0.5)
except KeyboardInterrupt:

    servo.stop()
    GPIO.cleanup()
