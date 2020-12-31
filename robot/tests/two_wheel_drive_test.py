from components.two_wheel_drive import TwoWheelDrive
import time

tw_drive = TwoWheelDrive()

print("forward 2 s")
tw_drive.move_forward(40)
time.sleep(2)

print("backward 2 s")
tw_drive.move_backwards(40)
time.sleep(2)

print("rotate left 2 s")
tw_drive.rotate_left(40)
time.sleep(2)

print("rotate right 2 s")
tw_drive.rotate_right(40)
time.sleep(2)

print("turn left 2 s")
tw_drive.turn_left(40,0.7)
time.sleep(2)

print("turn right 2 s")
tw_drive.turn_right(40,0.7)
time.sleep(2)


print("stop")
tw_drive.stop()