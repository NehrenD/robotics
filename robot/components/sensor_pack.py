from .ultrasonic_sensor import UltrasonicSensor


class SensorPack:

    def __init__(self, left_sensor_pins, right_sensor_pins):
        self.left_sensor = UltrasonicSensor(*left_sensor_pins)
        self.right_sensor = UltrasonicSensor(*right_sensor_pins)

    def take_measurement(self):
        return self.left_sensor.take_measurement(), self.right_sensor.take_measurement()

    def start(self):
        pass

    def stop(self):
        self.left_sensor.stop()
        self.right_sensor.stop()