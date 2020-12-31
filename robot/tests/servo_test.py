import RPi.GPIO as GPIO
from components.servo2 import ServoMotor
import time

if __name__ == '__main__':
    servo = ServoMotor(0, min_angle=-45, max_angle=45)
    servo.start()

try:
    while True:
        servo.set_angle(0)
        time.sleep(0.5)
        servo.set_angle(-45)
        time.sleep(0.5)
        servo.set_angle(0)
        time.sleep(0.5)
        servo.set_angle(45)
        time.sleep(0.5)
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

