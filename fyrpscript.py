from gpiozero import Motor
from gpiozero import MCP3008
from time import sleep

forward = MCP3008(channel=0)
reverse = MCP3008(channel=1)

motor = Motor(forward=19, backward=13)
while True:
        forwarddata = forward.value
        if forwarddata < 0.2:
            forwarddata = 0
        print("forward:" + str(forwarddata))
        
        reversedata = reverse.value
        if reversedata < 0.2:
            reversedata = 0
        print("reverse: " + str(reversedata))
        
        netdata = 0.65*(forwarddata - reversedata)
        print("movement:" + str(netdata))
        
        if netdata > 0:
            motor.forward(speed=netdata) #provide duty cycle in the range 0-100
        
        elif netdata < 0:
            movereverse = abs(netdata)
            motor.backward(speed=movereverse)
            
        else:
            motor.forward(speed=0)
            motor.backward(speed=0)
            