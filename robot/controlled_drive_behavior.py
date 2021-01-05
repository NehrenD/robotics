import time
import math
import sys

from components.robot import Robot
from components.wheel_encoder import WheelEncoder
from utils.pid_controller import PIDController
from utils.parameters import Parameters


def drive_distance(bot, left_distance, right_distance, speed, pid_coeff):
    if abs(left_distance) >= abs(right_distance):

        print("Left is primary")
        set_primary = bot.twd.set_left_speed
        primary_encoder = bot.twd.left_encoder

        set_secondary = bot.twd.set_right_speed
        secondary_encoder = bot.twd.right_encoder

        primary_distance = left_distance
        secondary_distance = right_distance
    else:
        print('Right is primary')
        set_primary = bot.twd.set_right_speed
        primary_encoder = bot.twd.left_encoder

        set_secondary = bot.twd.set_left_speed
        secondary_encoder = bot.twd.right_encoder

        primary_distance = right_distance
        secondary_distance = left_distance

    speed_ratio = secondary_distance / (primary_distance * 1.0)
    secondary_speed = int(speed * speed_ratio)
    print(f'Targets: primary: {speed}, secondary: {secondary_speed}, ratio: {speed_ratio}')

    primary_encoder.reset()
    secondary_encoder.reset()

    controller = PIDController(*pid_coeff)
    set_primary(speed)
    set_secondary(secondary_speed)

    while abs(primary_encoder.pulse_count) < abs(primary_distance) or \
            abs(secondary_encoder.pulse_count) < abs(secondary_distance):

        time.sleep(0.05)

        secondary_target = primary_encoder.pulse_count * speed_ratio
        error = secondary_target - secondary_encoder.pulse_count
        adjustment = controller.get_adjustment(error)
        print(f'secondary speed: {secondary_speed + adjustment}, adj: {adjustment}, error:{error}')
        set_secondary(int(secondary_speed + adjustment))

        if abs(primary_encoder.pulse_count) >= abs(primary_distance):
            set_primary(0)
            secondary_speed = 0
    set_primary(0)
    set_secondary(0)

def drive_arc(bot, turn_in_degrees, radius, speed, pid_coeff,wheel_distance_adj):
    half_width_ticks = WheelEncoder.mm_to_ticks(bot.twd.WHEEL_DISTANCE_MM / 2) + wheel_distance_adj
    if turn_in_degrees < 0:
        left_radius = radius - half_width_ticks
        right_radius = radius + half_width_ticks
    else:
        left_radius = radius + half_width_ticks
        right_radius = radius - half_width_ticks

    print(f'Arc Left: {left_radius}, right: {right_radius}')
    radians = math.radians(abs(turn_in_degrees))
    left_distance = int(left_radius * radians)
    right_distance = int(right_radius * radians)
    print(f'Arc left d: {left_distance}, right d:{right_distance}')

    drive_distance(bot, left_distance, right_distance,speed,pid_coeff)


def process_drive_cmd(bot, cmd, pid_coeff):
    (distance, speed) = [int(x) for x in cmd.split(',')]
    ticks = WheelEncoder.mm_to_ticks(distance)
    print(f'Driving {distance}mm ({ticks} ticks) at {speed}')
    drive_distance(bot, ticks, ticks, speed=speed, pid_coeff=pid_coeff)

def process_turn_cmd(bot, cmd, radius, pid_coeff,wheel_distance_adj):
    (angle, speed) = [int(x) for x in cmd.split(',')]
    print(f'Turning {angle}d at {speed}')
    drive_arc(bot, angle, radius, speed=speed, pid_coeff=pid_coeff,wheel_distance_adj=wheel_distance_adj)

def process_pid_coeff_cmd(cmd):
    new_coeff =  (float(x) for x in cmd.split(','))
    print(f"Changing pid coeff to: {new_coeff}")
    return new_coeff

if __name__ == '__main__':

    params = Parameters.load_from_file('./robot_params.json')
    bot = Robot(params)

    turn_radius = bot.twd.WHEEL_DISTANCE_MM + 100
    radius_in_ticks = WheelEncoder.mm_to_ticks(turn_radius)
    pid_coeff=(5,0.2)
    wheel_distance_adj = 0
    try:
        while True:
            line = input("Type Command:")

            if 'q' == line.rstrip():
                break

            cmd_type = line[0]
            cmd = line[1:]

            if cmd_type == 'd':
                process_drive_cmd(bot,cmd,pid_coeff,wheel_distance_adj)
                continue

            if cmd_type == 't':
                process_turn_cmd(bot,cmd,radius_in_ticks,pid_coeff,wheel_distance_adj)
                continue

            if cmd_type == 'p':
                pid_coeff = process_pid_coeff_cmd(cmd)
                continue

            if cmd_type == 'w':
                wheel_distance_adj = int(cmd)
                continue

            print(f'unrecognized type : {cmd_type}-> {cmd}')

    finally:
        bot.stop()
