import RPi.GPIO as GPIO
import time


class ServoMotor():

    def __init__(self, pin, min_angle=-90, max_angle=90, initial_angle=0):
        self.initial_angle = initial_angle
        self.gpio_pin = pin
        self.min_angle = min_angle
        self.max_angle = max_angle
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        self.servo_pwm = GPIO.PWM(self.gpio_pin, 50)

    def start(self):
        self.servo_pwm.start(0)
        time.sleep(0.2)
        self.set_angle(self.initial_angle)

    def stop(self):
        self.set_angle(self.initial_angle)
        time.sleep(0.2)
        self.servo_pwm.stop()

    def set_angle(self, angle):
        if angle < -90 or angle > 90:
            raise ValueError("Angle should be between -90 and 90 degrees")
        adj_angle = max(angle, self.min_angle)
        adj_angle = min(adj_angle, self.max_angle)

        duty = (90 + adj_angle ) / 18 + 2
        GPIO.output(self.gpio_pin, True)
        self.servo_pwm.ChangeDutyCycle(duty)
        time.sleep(0.2)
        GPIO.output(self.gpio_pin, False)
        self.servo_pwm.ChangeDutyCycle(0)
