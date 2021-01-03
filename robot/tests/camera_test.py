from components.camera import Camera
import time
import cv2

if __name__ == '__main__':

    camera  = Camera((320,240),flip_image=True)
    image = camera.take_shot()
    cv2.imshow("Image",image)
    cv2.waitKey(0)