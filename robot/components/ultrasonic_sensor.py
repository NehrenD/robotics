from gpiozero import DigitalInputDevice, DigitalOutputDevice
import time


class UltrasonicSensor:
    HALF_SOUND_SPEED_CM = 17150

    def __init__(self, echo_pin, trig_pin):
        self.trig_device = DigitalOutputDevice(trig_pin)
        self.echo_device = DigitalInputDevice(echo_pin)
        self.trig_device.value = False
        time.sleep(0.5)

    def take_measurement(self):
        time_out = time.time() + 1

        self.trig_device.value = True
        time.sleep(0.00001)
        self.trig_device.value = False

        pulse_start = time.time()
        while self.echo_device.pin.state == 0:
            if pulse_start > time_out:
                # Timeout
                return -1

        pulse_end = time.time()
        while self.echo_device.pin.state == 1:
            pulse_end = time.time()
            if pulse_end > time_out:
                # Timeout
                return -1

        pulse_duration = pulse_end - pulse_start
        distance = round(pulse_duration * UltrasonicSensor.HALF_SOUND_SPEED_CM, 2)
        return distance

    def stop(self):
        self.trig_device.close()
        self.echo_device.close()