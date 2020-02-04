#!/usr/bin/python
import time
import grovepi

class Distance_Reader():

    pin = 5

    def __init__(self, pin):
        self.pin = pin
        grovepi.pinMode(pin,"INPUT")


    def foundSomething(self):
        if grovepi.digitalRead(self.pin) == 0:
            return True
        else:
            return False

