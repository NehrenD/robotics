from .dc_motor import DCMotor
from .wheel_encoder import WheelEncoder
import numpy as np


class TwoWheelDrive:

    def __init__(self, left_motor_channel, right_motor_channel, left_encoder_pin, right_encoder_pin, i2c_address=0x40):
        self.left_motor = DCMotor(left_motor_channel, i2c_address=i2c_address)
        self.right_motor = DCMotor(right_motor_channel, i2c_address=i2c_address)
        self.left_encoder = WheelEncoder(left_encoder_pin)
        self.right_encoder = WheelEncoder(right_encoder_pin)

    def start(self):
        self.left_motor.start()
        self.right_motor.start()
        self.left_encoder.start()
        self.right_encoder.start()

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
        self.left_encoder.stop()
        self.right_encoder.stop()

    def move_forward(self, speed):
        self.set_left_speed(speed)
        self.set_right_speed(speed)

    def move_backwards(self, speed):
        self.set_left_speed(-speed)
        self.set_right_speed(-speed)

    def turn_left(self, speed, ratio):
        self.set_left_speed(speed * ratio)
        self.set_right_speed(speed)

    def turn_right(self, speed, ratio):
        self.set_left_speed(speed)
        self.set_right_speed(speed * ratio)

    def rotate_left(self, speed):
        self.left_motor.set_speed(-speed)
        self.set_right_speed(speed)

    def rotate_right(self, speed):
        self.set_left_speed(speed)
        self.set_right_speed(-speed)

    def set_speed(self, speed):
        self.set_left_speed(speed)
        self.set_right_speed(speed)

    def set_left_speed(self, speed):
        self.left_encoder.set_direction(np.sign(speed))
        self.left_motor.set_speed(speed)

    def set_right_speed(self, speed):
        self.right_encoder.set_direction(np.sign(speed))
        self.right_motor.set_speed(speed)

    def get_left_distance(self):
        return self.left_encoder.get_distance_mm()

    def get_right_distance(self):
        return self.right_encoder.get_distance_mm()

    def get_encoder_distances(self):
        return self.left_encoder.get_distance_mm(), self.right_encoder.get_distance_mm()
