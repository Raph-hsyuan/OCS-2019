#!/usr/bin/python
import led_controller as led
import distance_reader as dis
import TH_reader as th
import motor_controller as mt
import time

cled = led.Led_Controller(6)
led.Led_Controller(1)
cled.setColor(1)
time.sleep(.2)
cled.setColor(2)
time.sleep(.2)
cled.setColor(3)
time.sleep(.2)
cled.setColor(0)
time.sleep(.2)
cled.setColor(-1)

rdis = dis.Distance_Reader(5)
print(rdis.foundSomething())

rth = th.TH_Reader(2,0)
print(rth.getTH())

cmt = mt.Motor_Controller(7)
cmt.rotate()

# while True:
#     try:
#         a = rdis.foundSomething()
#         print(a)
#         time.sleep(.5)

#     except IOError:
#         print ("Error")



