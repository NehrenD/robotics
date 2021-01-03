import time
import cv2
import numpy as np

from utils.image_app_core import start_server_process, get_control_instruction, put_output_image
from utils import pi_camera_stream
from utils.pid_controller import PIDController
from components.robot import Robot


class ColorTrackingBehavior:

    def __init__(self, robot):
        self.robot = robot

        self.low_range = (25, 70, 25)
        self.high_range = (80, 255, 255)
        self.correct_radius = 90
        self.center = 90

        self.running = False

    def process_control(self):

        instruction = get_control_instruction()
        if instruction == 'start':
            self.running = True
        elif instruction == 'stop':
            self.running = False
        elif instruction == 'exit':
            print('Stopping!')
            exit()

    def find_object(self, original_frame):
        frame_hsv = cv2.cvtColor(original_frame, cv2.COLOR_BGR2HSV)
        masked = cv2.inRange(frame_hsv, self.low_range, self.high_range)
        contour_image = np.copy(masked)
        contours, _ = cv2.findContours(contour_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        circles = [cv2.minEnclosingCircle(cnt) for cnt in contours]
        if len(circles) == 0:
            return masked, (-1,-1),-1

        circles = sorted(circles, key=lambda x: -x[1])
        (x,y), radius = circles[0]

        return masked, (int(x),int(y)), int(radius)

    def make_display(self, frame, processed):
        display_frame = np.concatenate((frame, processed), axis=1)
        encoded_bytes = pi_camera_stream.get_encoded_bytes_for_frame(display_frame)
        put_output_image(encoded_bytes)

    def process_frame(self, frame):

        masked, coordinates, radius = self.find_object(frame)
        processed = cv2.cvtColor(masked, cv2.COLOR_GRAY2BGR)
        if radius >0:
            cv2.circle(frame, coordinates, radius, [255, 0, 0])
        self.make_display(frame, processed)
        return coordinates, radius


    def run(self):

        camera = pi_camera_stream.setup_camera()

        for frame in pi_camera_stream.start_stream(camera):
            (x,y), radius = self.process_frame(frame)
            self.process_control()
            print(f'coord: ({x},{y}) r: {radius}')

behavior = ColorTrackingBehavior(None)

process = start_server_process('color_track_behavior.html')
try:
    behavior.run()
finally:
    process.terminate()
