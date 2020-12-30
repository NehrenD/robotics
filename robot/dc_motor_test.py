from components.dc_motor import DCMotor
import time

motor1 = DCMotor(0)
motor2 = DCMotor(1)

print("forward 2 s")
motor1.set_speed(30)
#motor2.set_speed(30)

time.sleep(2)

print("backward 2 s")
motor1.set_speed(-30)
#motor2.set_speed(-30)
time.sleep(2)

print("stop")
motor1.stop()
motor2.stop()