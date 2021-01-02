from components.sensor_pack import SensorPack
import time

if __name__ == '__main__':
    sensor_pack = SensorPack((12,16),(20,21))

    try:
        while True:
            left_distance,right_distance = sensor_pack.take_measurement()
            print(f'left: {left_distance}cm, right: {right_distance}cm')

            time.sleep(0.5)

    except KeyboardInterrupt:
        pass