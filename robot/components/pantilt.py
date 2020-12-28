from .camera import Camera
from .servo import ServoMotor


class CameraPanTilt:

    def __init__(self, pan_servo_pin, tilt_servo_pin, initial_angles=(0, 0)):
        self.camera = Camera((640, 480))
        self.pan_servo = ServoMotor(pan_servo_pin,-45,45, initial_angle=initial_angles[0])
        self.tilt_servo = ServoMotor(tilt_servo_pin, -45, 45, initial_angle=initial_angles[1])

    def start(self):
        self.pan_servo.start()
        self.tilt_servo.start()

    def stop(self):
        self.pan_servo.stop()
        self.tilt_servo.stop()

    def set_angles(self, pan_angle, tilt_angle):
        self.pan_servo.set_angle(pan_angle)
        self.tilt_servo.set_angle(tilt_angle)

    def take_camera_shot(self):
        return self.camera.take_shot()
