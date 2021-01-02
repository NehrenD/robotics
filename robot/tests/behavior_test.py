import atexit
from components.robot import Robot
from parameters import Parameters
from behaviors.drive_distance import DriveDistanceBehavior

if __name__ == '__main__':
    params = Parameters.load_from_file('../robot_params.json')
    robot = Robot(params)
    behavior = DriveDistanceBehavior(robot,2000,50)
    try:
        behavior.run_behavior()
    finally:
        robot.stop()
