from components.pantilt import CameraPanTilt
import time
import cv2

if __name__ == '__main__':


    pan_tilt = CameraPanTilt(1,0)
    pan_tilt.start()
    time.sleep(1)

    image = pan_tilt.take_camera_shot()

    cv2.imshow("Image", image)
    cv2.waitKey(0)

    pan_tilt.set_angles(-45,-45)
    time.sleep(0.5)
    image = pan_tilt.take_camera_shot()

    cv2.imshow("Image",image)
    cv2.waitKey(0)

    pan_tilt.set_angles(0,-45)
    time.sleep(0.5)
    image = pan_tilt.take_camera_shot()

    cv2.imshow("Image",image)
    cv2.waitKey(0)
    time.sleep(0.5)
    pan_tilt.set_angles(45,-45)

    image = pan_tilt.take_camera_shot()

    cv2.imshow("Image",image)
    cv2.waitKey(0)

    pan_tilt.stop()