from components.wheel_encoder import WheelEncoder
import time

if __name__ == '__main__':
    left_encoder = WheelEncoder(20)
    right_encoder = WheelEncoder(21)

    direction = 1
    c_time = time.time()
    try:
        while True:
            ct = time.time()
            if ct - c_time > 5:
                #direction = -1*direction
                left_encoder.set_direction(direction)
                right_encoder.set_direction(direction)
                print('direction = {direction}')
                c_time = ct

            print(f'left: {left_encoder.pulse_count}, right:{right_encoder.pulse_count}')
            print(f'f left d: {left_encoder.get_distance_mm()}mm, right d: {right_encoder.get_distance_mm()}mm')
            time.sleep(0.1)

    except KeyboardInterrupt:
        pass
