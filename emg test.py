from gpiozero import MCP3008
from time import sleep

forward = MCP3008(channel=0)
reverse = MCP3008(channel=1)
    
while True:
    forwarddata = forward.value
    if forwarddata < 0.1:
            forwarddata = 0
    #print("forward:" + str(forwarddata))
    reversedata = reverse.value
    if reversedata < 0.1:
            reversedata = 0
    #print("reverse: " + str(reversedata))
    netdata = 0.65*(forwarddata - reversedata)
    print("movement:" + str(netdata))
    sleep(1)