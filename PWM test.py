from gpiozero import MCP3008
from gpiozero import Motor
from time import sleep

motor = Motor(forward=19, backward=13)
while True:
    motor.forward(speed=0.25)
    sleep(1)
    motor.stop
    sleep(1)
    motor.backward(speed=0.25)
    sleep(1)
    motor.stop