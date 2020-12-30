from components.dc_motor import DCMotor

class TwoWheelDrive:

    def __init__(self, ic2_address=0x40):
        self.left_motor = DCMotor(1, ic2_address=ic2_address)
        self.right_motor = DCMotor(0, ic2_address=ic2_address)

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

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