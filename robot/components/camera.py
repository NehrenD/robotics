from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

class Camera():

    def __init__(self,img_size=None,flip_image=False):
        self.img_size = img_size
        self.flip_image = flip_image
        self.camera = PiCamera()


    def take_shot(self):
        rawCapture = PiRGBArray(self.camera)
        self.camera.capture(rawCapture, format='bgr')
        image = rawCapture.array

        if self.img_size is not None:
            image = cv2.resize(image, self.img_size)

        if self.flip_image:
            image = cv2.flip(image, 0)

        return image