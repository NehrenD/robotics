from .pantilt import CameraPanTilt
from .two_wheel_drive import TwoWheelDrive



class Robot():

    def __init__(self, params):
        self.params = params
        (pan_channel, tilt_channel) = params.pan_tilt_channels
        (lef_motor_channel,right_motor_channel) = params.dc_motor_channels
        self.pan_tilt = CameraPanTilt(pan_channel,tilt_channel)
        self.twd = TwoWheelDrive(lef_motor_channel,right_motor_channel)

    def start(self):
        self.pan_tilt.start()
        self.twd.stop()

    def stop(self):
        self.pan_tilt.stop()
        self.twd.stop()