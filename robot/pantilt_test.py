import RPi.GPIO as GPIO

from components.pantilt import CameraPanTilt
import time
import cv2

def initialize_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
if __name__ == '__main__':

    initialize_gpio()

    pan_tilt = CameraPanTilt(5,3)
    pan_tilt.start()
    time.sleep(1)

    image = pan_tilt.take_camera_shot()

    cv2.imshow("Image",image)
    cv2.waitKey(0)

    pan_tilt.set_angles(-45,-45)
    image = pan_tilt.take_camera_shot()

    cv2.imshow("Image",image)
    cv2.waitKey(0)

    pan_tilt.set_angles(0,0)

    image = pan_tilt.take_camera_shot()

    cv2.imshow("Image",image)
    cv2.waitKey(0)

    pan_tilt.set_angles(45,45)

    image = pan_tilt.take_camera_shot()

    cv2.imshow("Image",image)
    cv2.waitKey(0)

    pan_tilt.stop()