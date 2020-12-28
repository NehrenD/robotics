from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

class Camera():

    def __init__(self,img_size=None):
        self.img_size = img_size
        self.camera = PiCamera()


    def take_shot(self):
        rawCapture = PiRGBArray(self.camera)
        self.camera.capture(rawCapture, format='bgr')
        image = rawCapture.array
        if self.img_size is None:
            return image
        else:
            return cv2.resize(image, self.img_size)