from .behavior_base import BehaviorBase
import cv2
import time

class Behavior1(BehaviorBase):

    def __init__(self, robot):
        super(Behavior1, self).__init__(robot)

    def run_behavior(self):

        self.robot.twd.move_forward(50)
        time.sleep(3)
        self.robot.twd.stop()

        self.robot.pan_tilt.set_angles(-45,-45)
        image = self.robot.pan_tilt.take_camera_shot()
        cv2.imshow("Image", image)
        cv2.waitKey(0)

        self.robot.pan_tilt.set_angles(45, -45)
        image = self.robot.pan_tilt.take_camera_shot()
        cv2.imshow("Image", image)
        cv2.waitKey(0)

        self.robot.twd.rotate_left(40)
        time.sleep(2)
        self.robot.twd.stop()

        self.robot.pan_tilt.set_angles(-45, -45)
        image = self.robot.pan_tilt.take_camera_shot()
        cv2.imshow("Image", image)
        cv2.waitKey(0)

        self.robot.pan_tilt.set_angles(45, -45)
        image = self.robot.pan_tilt.take_camera_shot()
        cv2.imshow("Image", image)
        cv2.waitKey(0)

        self.robot.twd.rotate_right(40)
        time.sleep(2)
        self.robot.twd.stop()

        self.robot.pan_tilt.set_angles(-45, -45)
        image = self.robot.pan_tilt.take_camera_shot()
        cv2.imshow("Image", image)
        cv2.waitKey(0)

        self.robot.pan_tilt.set_angles(45, -45)
        image = self.robot.pan_tilt.take_camera_shot()
        cv2.imshow("Image", image)
        cv2.waitKey(0)

        self.robot.twd.move_backwards(40)
        time.sleep(3)
        self.robot.stop()
