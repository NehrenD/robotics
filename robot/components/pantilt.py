from .camera import Camera
from .servo import ServoMotor

class CameraPanTilt():

    def __init__(self, bottom_servo_pin, top_servo_pin, initial_angles=(90,90)):
        self.camera = Camera((640,480))
        self.bottom_servo = ServoMotor(bottom_servo_pin,initial_angle=initial_angles[0])
        self.top_servo = ServoMotor(top_servo_pin, 20, 150,initial_angle=initial_angles[1])

    def start(self):
        self.bottom_servo.start()
        self.top_servo.start()

    def stop(self):

        self.bottom_servo.stop()
        self.top_servo.stop()

    def set_angles(self, bottom, top):
        self.bottom_servo.set_angle(bottom)
        self.top_servo.set_angle(top)

    def take_camera_shot(self):
        return self.camera.take_shot()