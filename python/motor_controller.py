import RPi.GPIO as GPIO
import time
class Motor_Controller():

    GPIO_port = 7
    
    def __init__(self, GPIO_port):
        self.GPIO_port = GPIO_port
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(GPIO_port,GPIO.OUT)

    def rotate(self, degree = 22.5):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.GPIO_port,GPIO.OUT)
        times = int(round(degree / 7.5))
        print("rotate:"+str(times*7.5)+" degrees")
        for n in range(times):
            GPIO.output(self.GPIO_port,1)#start
            time.sleep(0.00025)
            GPIO.output(self.GPIO_port,0)#stop
            time.sleep(1)
        GPIO.cleanup()



