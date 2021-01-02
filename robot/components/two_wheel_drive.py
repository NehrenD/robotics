from .dc_motor import DCMotor
from .wheel_encoder import WheelEncoder

class TwoWheelDrive:

    def __init__(self,left_motor_channel,right_motor_channel,left_encoder_pin, right_encoder_pin, i2c_address=0x40):
        self.left_motor = DCMotor(left_motor_channel, i2c_address=i2c_address)
        self.right_motor = DCMotor(right_motor_channel, i2c_address=i2c_address)
        self.left_encoder = WheelEncoder(left_encoder_pin)
        self.right_encoder = WheelEncoder(right_encoder_pin)

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
        self.left_encoder.stop()
        self.right_encoder.stop()

    def move_forward(self, speed):
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed)

    def move_backwards(self, speed):
        self.left_motor.set_speed(-speed)
        self.right_motor.set_speed(-speed)

    def turn_left(self,speed,ratio):
        self.left_motor.set_speed(speed*ratio)
        self.right_motor.set_speed(speed)

    def turn_right(self,speed,ratio):
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed*ratio)

    def rotate_left(self,speed):
        self.left_motor.set_speed(-speed)
        self.right_motor.set_speed(speed)

    def rotate_right(self,speed):
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(-speed)

    def set_speed(self, speed):
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed)