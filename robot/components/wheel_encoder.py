from gpiozero import DigitalInputDevice
import math


class WheelEncoder:
    WHEEL_DIAMETER_MM = 70
    PULSES_PER_REVOLUTION = 40
    PULSES_TO_MM = (math.pi / PULSES_PER_REVOLUTION) * WHEEL_DIAMETER_MM

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

    def stop(self):
        self.encoder.close()

    def get_distance_mm(self):
        return self.pulse_count * WheelEncoder.PULSES_TO_MM

    def encoder_changed(self, ticks, state):
        self.pulse_count += self.direction
