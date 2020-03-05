import paho.mqtt.client as mqtt
import time
import led_controller as led
import distance_reader as dis
import TH_reader as th
import motor_controller as mt
import json

def on_message_briller(client, userdata, message):
    payload = str(message.payload.decode("utf-8"))
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic.decode("utf-8"))
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

def on_message_env(client, userdata, message):
    payload = str(message.payload.decode("utf-8"))
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic.decode("utf-8"))
    res = rth.getTH()
    sendHT(str(res))
    print(str(res))

def on_message_detect(client, userdata, message):
    payload = str(message.payload.decode("utf-8"))
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic.decode("utf-8"))
    res = rdis.foundSomething()
    sendDetected(res)
    print(str(res))
        
def on_message_distrib(client, userdata, message):
    payload = str(message.payload.decode("utf-8"))
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic.decode("utf-8"))
    degree=json.loads(payload)["degree"]
    cmt.rotate(degree)
    print("distribution")


def sendDetected(result):
    client.publish(TOPIC_SEND_DETECT, str(result))

def sendHT(result):
    client.publish(TOPIC_SEND_TEMP,str(result))


def on_message(mosq, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

cled = led.Led_Controller(6)
try:
    cled.setBlinkBySecond(0,2) 
    HOST_NAME = "127.0.0.1"
    TOPIC_SEND_TEMP = "pilulier/device1/info/environnement"
    TOPIC_SEND_DETECT = "pilulier/device1/info/detect"
    TOPIC_RECEVE_BRILLER = "pilulier/device1/instruction/briller"
    TOPIC_RECEVE_ENV = "pilulier/device1/instruction/environnement"
    TOPIC_RECEVE_DETECT = "pilulier/device1/instruction/detected"
    TOPIC_RECEVE_DISTRIB = "pilulier/device1/instruction/distribution"


    rdis = dis.Distance_Reader(5)
    rth = th.TH_Reader(2,0)
    cmt = mt.Motor_Controller(7)

    client = mqtt.Client("5V07R0FXA6IN9RLO")
    LIGHT = -1
    client.connect(HOST_NAME, 1884)
    client.message_callback_add(TOPIC_RECEVE_BRILLER, on_message_briller)
    client.message_callback_add(TOPIC_RECEVE_ENV, on_message_env)
    client.message_callback_add(TOPIC_RECEVE_DETECT, on_message_detect)
    client.message_callback_add(TOPIC_RECEVE_DISTRIB, on_message_distrib)

    client.subscribe("pilulier/device1/instruction/#")

    client.on_message = on_message

    cled.setColor(-1)

    while True:
        #cled = led.Led_Controller(6)
        #cled.setColor(1) # blink green when everything goes well
        #cled.setColor(-1) # blink green when everything goes well

        res = rth.getTH()
        sendHT(str(res))
        client.loop_start()
        time.sleep(10)
        client.loop_stop()
except:
    cled.setColor(2) # display red when going wrong
