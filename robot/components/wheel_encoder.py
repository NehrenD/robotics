from gpiozero import DigitalInputDevice
import math


class WheelEncoder:
    ticks_to_mm_const = None

    @staticmethod
    def mm_to_ticks(mm):
        return int(mm/WheelEncoder.ticks_to_mm_const)

    @staticmethod
    def set_constants(wheel_diameter, ticks_per_revolution):
        WheelEncoder.ticks_to_mm_const = (math.pi/ticks_per_revolution)*wheel_diameter

    def __init__(self, encoder_pin):
        self.pulse_count = 0
        self.direction = 1

        self.encoder = DigitalInputDevice(encoder_pin)
        self.encoder.pin.when_changed = self.encoder_changed

    def set_direction(self, direction):
        assert abs(direction) == 1, f'Direction {direction} should be +/-1'
        self.direction = direction

    def reset(self):
        self.pulse_count = 0

    def start(self):
        pass

    def stop(self):
        self.encoder.close()

    def distance_in_mm(self):
        return self.pulse_count * WheelEncoder.ticks_to_mm_const

    def encoder_changed(self, ticks, state):
        self.pulse_count += self.direction
