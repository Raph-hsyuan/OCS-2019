#!/usr/bin/python
import time
import grovepi
import math

class TH_Reader():

    pin = 2
    model = 0 #blue = 0, white = 1

    def __init__(self, pin, model):
        self.pin = pin
        self.model = model
        grovepi.pinMode(pin,"INPUT")


    def getTH(self):
        [temp,humidity] = grovepi.dht(self.pin,self.model)  
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            return "temp = %.02f C humidity =%.02f%%"%(temp, humidity)
        else:
            return "ERROR"
