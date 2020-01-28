#!/usr/bin/python
import time
import grovepi

class Led_Controller():

    pin = 6

    def __init__(self, pin):
        self.pin = pin
        grovepi.pinMode(pin,"OUTPUT")
        grovepi.chainableRgbLed_init(pin, 1)


    def setColor(self, color):
        thisLedOnly = 0
        if color == 0:
            grovepi.storeColor(0,0,255) #blue
            print("set: p" + str(self.pin) + " to blue")

        elif color == 1:
            grovepi.storeColor(0,255,0) #green
            print("set: p" + str(self.pin) + " to greens")
        elif color == 2:
            grovepi.storeColor(255,0,0) #red
            print("set: p" + str(self.pin) + " to red")
        elif color == -1:
            grovepi.storeColor(0,0,0) #off
            print("set: p" + str(self.pin) + " to off")
        else:
            grovepi.storeColor(255,255,255)
            print("set: p" + str(self.pin) + " to default white")
        grovepi.chainableRgbLed_pattern(self.pin, thisLedOnly, 0)

    def setColorBySecond(self, color, second):
        self.setColor(color)
        time.sleep(second)
        self.setColor(-1)

    def setBlinkBySecond(self, color, times):
        for n in range(times):
            self.setColor(color)
            time.sleep(.2)
            self.setColor(-1)
            time.sleep(.2)

