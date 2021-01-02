from .PCA9685 import PCA9685
import numpy as np

dc_motor_info = [
    dict(pwm_idx=0, in1=1, in2=2),
    dict(pwm_idx=5, in1=3, in2=4)
]


class DCMotor:

    def __init__(self, motor_idx, i2c_address=0x40, min_speed=0, max_speed=80):
        self.pwm = PCA9685(i2c_address)
        self.pwm.setPWMFreq(50)
        self.pwm_idx = dc_motor_info[motor_idx]['pwm_idx']
        self.in1 = dc_motor_info[motor_idx]['in1']
        self.in2 = dc_motor_info[motor_idx]['in2']
        self.min_speed = min_speed
        self.max_speed = max_speed

    def start(self):
        self.stop()

    def stop(self):
        self.pwm.setDutycycle(self.pwm_idx, 0)

    def set_direction(self, is_forward):
        if is_forward:
            self.pwm.setLevel(self.in1, 0)
            self.pwm.setLevel(self.in2, 1)
        else:
            self.pwm.setLevel(self.in1, 1)
            self.pwm.setLevel(self.in2, 0)

    def set_speed(self, speed):
        direction = np.sign(speed)
        abs_speed = np.abs(speed)
        abs_speed = max(abs_speed, self.min_speed)
        abs_speed = min(abs_speed, self.max_speed)

        self.pwm.setDutycycle(self.pwm_idx, abs_speed)
        self.set_direction(direction > 0)
