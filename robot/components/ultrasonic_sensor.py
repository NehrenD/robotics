from gpiozero import DigitalInputDevice,DigitalOutputDevice
import time

class UltrasonicSensor:

    def __init__(self,echo_pin,trig_pin):
        self.echo_pin = echo_pin
        self.trig_pin = trig_pin