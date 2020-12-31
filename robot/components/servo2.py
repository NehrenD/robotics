from .PCA9685 import PCA9685
import time


class ServoMotor():

    FREQ = 50
    PERIOD_MS = 1000/FREQ
    PULSE_STEPS = 4096

    def __init__(self, channel, min_angle=-90, max_angle=90, initial_angle=0, i2c_address=0x41,mid_ms =1.5, right_angle_ms=1.1):

        self.initial_angle = initial_angle
        self.channel = channel
        self.pwm = PCA9685(i2c_address)
        self.pwm.setPWMFreq(ServoMotor.FREQ)

        self.min_angle = min_angle
        self.max_angle = max_angle

        self.steps_ms = ServoMotor.PULSE_STEPS / ServoMotor.PERIOD_MS
        self.servo_mid_ms = mid_ms
        self.deflect_90_ms = right_angle_ms
        self.steps_degree = (self.deflect_90_ms * self.steps_ms)/90
        self.servo_mid_steps = self.servo_mid_ms * self.steps_ms

    def start(self):
        self.set_angle(self.initial_angle)

    def stop(self):
        self.set_angle(self.initial_angle)
        time.sleep(0.2)
        self.pwm.setPWM(self.channel,0, 0)

    def set_angle(self, angle):
        if angle < -90 or angle > 90:
            raise ValueError("Angle should be between -90 and 90 degrees")

        adj_angle = max(angle, self.min_angle)
        adj_angle = min(adj_angle, self.max_angle)

        pwm_value = int(self.servo_mid_steps + adj_angle*self.steps_degree)
        self.pwm.setPWM(self.channel, 0, pwm_value)
