from components.ultrasonic_sensor import UltrasonicSensor
import time

HALF_SOUND_SPEED_CM = 17150


if __name__ == '__main__':

    sensor = UltrasonicSensor(20,21)

    try:
        while True:
            distance = sensor.take_measurement()
            if distance != -1:
                print(f'Distance: {distance}cm')
            else:
                print('Timeout!')
            time.sleep(0.5)

    except KeyboardInterrupt:
        pass

