import RPi.GPIO as GPIO
from gpiozero import DigitalInputDevice,DigitalOutputDevice
import time

HALF_SOUND_SPEED_CM = 17150

echo_pin = 40
trig_pin = 38

def init_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

def make_measurement(trig_device,echo_device):
    time_out = time.time() + 1

    trig_device.value = True
    time.sleep(0.00001)
    trig_device.value = False

    pulse_start = time.time()
    while echo_device.pin.state == 0:
        if pulse_start > time_out:
            print('timed_out')
            return -1

    pulse_end = time.time()
    while echo_device.pin.state == 1:
        pulse_end = time.time()
        if pulse_end > time_out:
            print('timed_out')
            return -1

    pulse_duration = pulse_end - pulse_start
    distance = round(pulse_duration * HALF_SOUND_SPEED_CM,2)
    return distance

if __name__ == '__main__':
    init_gpio()
    trig = DigitalOutputDevice(trig_pin)
    echo = DigitalInputDevice(echo_pin)

    trig.value = False
    time.sleep(0.5)

    try:
        while True:
            distance = make_measurement(trig,echo)
            if distance != -1:
                print(f'Distance: {distance}cm')
            else:
                print('Timeout!')
            time.sleep(0.5)

    except KeyboardInterrupt:
        GPIO.cleanup()

