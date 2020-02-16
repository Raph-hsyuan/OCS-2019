#!/usr/bin/python
import time
import grovepi
import math

class TH_Reader():

    pin = 2
    model = 0 #blue = 0, white = 1
    temp1 = -1
    humidity1 = -1
    def __init__(self, pin, model):
        self.pin = pin
        self.model = model
        grovepi.pinMode(pin,"INPUT")


    def getTH(self):
        [temp,humidity] = grovepi.dht(self.pin,self.model)  
        if math.isnan(temp) == False and math.isnan(humidity) == False:
	    temp1 = math.isnan(temp)
	    humidity1 = math.isnan(humidity)
            return '{"temp":%.02f, "humidity":%.02f}'%(temp, humidity)
        else:
            return '{"temp":%.02f, "humidity":%.02f}'%(self.temp1, self.humidity1)

