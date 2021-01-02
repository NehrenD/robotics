from simple_pid import PID
from components.wheel_encoder import WheelEncoder
import time

from .behavior_base import BehaviorBase


class DriveDistanceBehavior(BehaviorBase):

    def __init__(self, robot,distance,speed):
        super(DriveDistanceBehavior, self).__init__(robot)

        self.pid = PID(*(6,0.05,0.0),sample_time=0.01)
        self.speed = speed
        self.pulses = WheelEncoder.get_pulses_for_distance(distance)

    def run_behavior(self):

        set_primary = self.robot.twd.set_left_speed
        set_secondary = self.robot.twd.set_right_speed
        primary_encoder = self.robot.twd.left_encoder
        secondary_encoder = self.robot.twd.right_encoder

        self.robot.start()
        self.robot.twd.set_speed(self.speed)

        while primary_encoder.pulse_count < self.pulses or secondary_encoder.pulse_count < self.pulses:
            time.sleep(0.05)

            to_do = self.pulses - primary_encoder.pulse_count

            error = primary_encoder.pulse_count - secondary_encoder.pulse_count
            adjustment = int(self.pid(-error))
            right_speed = self.speed + adjustment
            set_secondary(right_speed)
            print(f'left: {primary_encoder.pulse_count}, right: {secondary_encoder.pulse_count}, err: {error}, adj: {adjustment}, to_do:{to_do}')

