import atexit
from components.robot import Robot
from parameters import Parameters
from behaviors.behavior_1 import Behavior1

if __name__ == '__main__':
    params = Parameters.load_from_file('../robot_params.json')
    robot = Robot(params)

    behavior = Behavior1(robot)
    try:
        behavior.run_behavior()
    finally:
        robot.stop()
