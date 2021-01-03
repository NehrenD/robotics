from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


class Camera():

    def __init__(self, img_size=None, flip_image=False):
        self.img_size = img_size
        self.flip_image = flip_image
        self.camera = PiCamera()
        if img_size is not None:
            self.camera.resolution = img_size

        if flip_image:
            self.camera.rotation = 180

    def take_shot(self):
        rawCapture = PiRGBArray(self.camera)
        self.camera.capture(rawCapture, format='bgr')
        image = rawCapture.array

        result, image = cv2.imencode('.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY),90])

        return image
