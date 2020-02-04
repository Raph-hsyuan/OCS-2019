import paho.mqtt.client as mqtt
import time
import led_controller as led
import distance_reader as dis
import TH_reader as th
import motor_controller as mt
import json

HOST_NAME = "127.0.0.1"
TOPIC_SEND_TEMP = "pilulier/device1/info/environnement"
TOPIC_SEND_DETECT = "pilulier/device1/info/detect"
TOPIC_RECEVE_SHINE = "pilulier/device1/instruction/briller"
TOPIC_RECEVE_ENV = "pilulier/device1/instruction/environnement"
TOPIC_RECEVE_DETECT = "pilulier/device1/instruction/detected"
TOPIC_RECEVE_DISTRIB = "pilulier/device1/instruction/distribution"

rdis = dis.Distance_Reader(5)
rth = th.TH_Reader(2,0)
cmt = mt.Motor_Controller(7)

client = mqtt.Client("5V07R0FXA6IN9RLO")
LIGHT = -1
client.connect(HOST_NAME,1884)
client.subscribe(TOPIC_RECEVE_SHINE)
client.subscribe(TOPIC_RECEVE_ENV)
client.subscribe(TOPIC_RECEVE_DETECT)
client.subscribe(TOPIC_RECEVE_DISTRIB)

def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8"))
    instruction = json.loads(payload)["name"]
    # print(str(message.color.decode("utf-8")))
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic.decode("utf-8"))
    # print("message qos=",message.qos.decode("utf-8"))
    # print("message retain flag=",message.retain.decode("utf-8"))
    if instruction == 'briller':
        # print(str(message.color))
        # cled = led.Led_Controller(6)
        # cled.setColor(1)
        # time.sleep(2)
        # cled.setColor(-1)
        color=json.loads(payload)["color"]
        option=json.loads(payload)["option"]
        if option == "open":
            print("yrdddddddd")
            cled = led.Led_Controller(6)
            cled.setColor(color)
        elif option == "opentime":
            cled = led.Led_Controller(6)
            time=json.loads(payload)["time"]
            cled.setColorBySecond(color,int(time))
        elif option == "blink":
            cled = led.Led_Controller(6)
            time=json.loads(payload)["time"]
            cled.setBlinkBySecond(color,int(time))
        print("LightSignal")

    elif instruction == "environnement":
        res = rth.getTH()
        sendHT(str(res))
        print(str(res))
    elif instruction == "detected":
        res = rdis.foundSomething()
        sendDetected(res)
        print(str(res))
    elif instruction == "distribution":
        degree=json.loads(payload)["degree"]
        cmt.rotate(degree)
        print("distribution")

def sendDetected(result):
    client.publish(TOPIC_SEND_DETECT, str(result))

def sendHT(result):
    client.publish(TOPIC_SEND_TEMP,str(result))

client.on_message = on_message
client.loop_start() 
time.sleep(10000000)
client.loop_stop()



