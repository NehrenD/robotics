from components.camera import Camera
import time
import cv2

camera  = Camera((640,480))
image = camera.take_shot()
cv2.imshow("Image",image)
cv2.waitKey(0)