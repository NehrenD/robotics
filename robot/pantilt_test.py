import RPi.GPIO as GPIO

from components.pantilt import CameraPanTilt
import time
import cv2

def initialize_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

initialize_gpio()

pan_tilt = CameraPanTilt(3,2)
pan_tilt.start()
time.sleep(1)

image = pan_tilt.take_camera_shot()

cv2.imshow("Image",image)
cv2.waitKey(0)

pan_tilt.set_angles(45,90)
image = pan_tilt.take_camera_shot()

cv2.imshow("Image",image)
cv2.waitKey(0)

pan_tilt.set_angles(135,45)

image = pan_tilt.take_camera_shot()

cv2.imshow("Image",image)
cv2.waitKey(0)

pan_tilt.stop()