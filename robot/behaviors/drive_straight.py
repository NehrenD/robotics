from simple_pid import PID
import time

from .behavior_base import BehaviorBase


class DriveStraightBehavior(BehaviorBase):

    def __init__(self, robot, pid_params,eval_time, speed,running_time):
        super(DriveStraightBehavior, self).__init__(robot)
        self.eval_time = eval_time
        self.pid = PID(*pid_params,sample_time=0.01)
        self.speed = speed
        self.running_time = running_time

    def run_behavior(self):

        end_time = time.time() + self.running_time

        self.robot.start()
        self.robot.twd.set_speed(self.speed)
        while time.time() < end_time:
            time.sleep(self.eval_time)
            (left_pulse,right_pulse) = self.robot.twd.get_encoder_pulses()

            error = left_pulse - right_pulse
            adjustment = int(self.pid(-error))
            right_speed = self.speed + adjustment
            self.robot.twd.set_right_speed(right_speed)
            print(f'left: {left_pulse}, right: {right_pulse}, err: {error}, adj: {adjustment}, rs:{right_speed}')

