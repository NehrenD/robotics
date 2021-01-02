from .pantilt import CameraPanTilt
from .two_wheel_drive import TwoWheelDrive
from .sensor_pack import SensorPack


class Robot:

    def __init__(self, params):
        self.params = params
        # Pan Tilt
        (pan_channel, tilt_channel) = params.pan_tilt_channels
        self.pan_tilt = CameraPanTilt(pan_channel, tilt_channel)

        # 2WD
        (lef_motor_channel, right_motor_channel) = params.dc_motor_channels
        (left_encoder_pin, right_encoder_pin) = params.wheel_encoders_pins
        self.twd = TwoWheelDrive(lef_motor_channel, right_motor_channel, left_encoder_pin, right_encoder_pin)

        # Sensor Pack
        (left_sensor_pins, right_sensor_pins) = params.sensor_pack_pins
        self.sensor_pack = SensorPack(left_sensor_pins, right_sensor_pins)

    def start(self):
        self.pan_tilt.start()
        self.twd.start()
        self.sensor_pack.start()

    def stop(self):
        self.pan_tilt.stop()
        self.twd.stop()
        self.sensor_pack.stop()
