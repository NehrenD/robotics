import time
import math

from components.robot import Robot
from components.wheel_encoder import WheelEncoder
from utils.pid_controller import PIDController
from utils.parameters import Parameters

params = Parameters.load_from_file('./robot_params.json')
bot = Robot(params)

distance_to_drive = 1000
distance_in_ticks = WheelEncoder.mm_to_ticks(distance_to_drive)
turn_radius = bot.twd.WHEEL_DISTANCE_MM + 100
radius_in_ticks = WheelEncoder.mm_to_ticks(turn_radius)

def drive_distance(bot, left_distance,right_distance, speed=50):

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

    speed_ratio = secondary_distance/(primary_distance*1.0)
    secondary_speed = int(speed*speed_ratio)
    print(f'Targets: primary: {speed}, secondary: {secondary_speed}, ratio: {speed_ratio}')

    primary_encoder.reset()
    secondary_encoder.reset()

    controller = PIDController(5,0.2)
    set_primary(speed)
    set_secondary(secondary_speed)

    while abs(primary_encoder.pulse_count) < abs(primary_distance) or \
            abs(secondary_encoder.pulse_count) < abs(secondary_distance):

        time.sleep(0.05)

        secondary_target = primary_encoder.pulse_count * speed_ratio
        error = secondary_target - secondary_encoder.pulse_count
        adjustment = controller.get_adjustment(error)
        set_secondary(int(secondary_speed + adjustment))

        if abs(primary_encoder.pulse_count) >= abs(primary_distance):
            set_primary(0)
            secondary_speed = 0

def drive_arc(bot,turn_in_degrees, radius, speed=50):

    half_width_ticks =  WheelEncoder.mm_to_ticks(bot.twd.WHEEL_DISTANCE_MM/2)
    if turn_in_degrees <0:
        left_radius = radius - half_width_ticks
        right_radius = radius + half_width_ticks
    else:
        left_radius = radius + half_width_ticks
        right_radius = radius - half_width_ticks

    print(f'Arc Left: {left_radius}, right: {right_radius}')
    radians = math.radians(abs(turn_in_degrees))
    left_distance = int(left_radius*radians)
    right_distance = int(right_radius*radians)
    print(f'Arc left d: {left_distance}, right d:{right_distance}')
    drive_distance(bot,left_distance,right_distance)

try:
    for n in range(4):
        drive_distance(bot,distance_in_ticks,distance_in_ticks)
        drive_arc(bot,90,radius_in_ticks, speed = 50)
finally:
    bot.stop()