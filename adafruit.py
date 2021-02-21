import paho.mqtt.client as mqtt #import the client1
import time
import random
from random import randint

broker_address="io.adafruit.com"
clientId     ="Ivan"
username     = "ivangiovanni" #username adafruit
password     = "aio_ezgb69UcW3v1tCjZpgBGyle6vCfy"
topic_ac     = "tugas-wpc.aircon"
topic_bt     = "tugas-wpc.battery"
topic_fuel   = "tugas-wpc.fuel"
topic_gen    = "tugas-wpc.generator"
topic_light1 = "tugas-wpc.mainlight"
topic_pwr    = "tugas-wpc.power"
topic_temp   = "tugas-wpc.temp"
topic_water  = "tugas-wpc.water"


message = ""
def on_message(client, userdata, msg):
    message=str(msg.payload.decode("utf-8"))
client = mqtt.Client(clientId) #create new instance
client.username_pw_set(username, password)
client.connect(broker_address) #connect to broker

bt   = 100
water= 120
fuel = 100

while True:
    #publish
    client.subscribe(username+"/feeds/"+topic_gen)
    client.subscribe(username+"/feeds/"+topic_light1)
    client.on_message = on_message
    client.publish(username+"/feeds/"+topic_bt,bt)
    client.publish(username+"/feeds/"+topic_pwr,random.uniform(5, 100))
    client.publish(username+"/feeds/"+topic_temp,random.uniform(16, 25))
    client.publish(username+"/feeds/"+topic_water,water)
    client.publish(username+"/feeds/"+topic_fuel,fuel)

    if message == "ON":
        bt +=0.5
    else:
        bt -= random.uniform(0, 1)

    water -= random.uniform(0, 1)
    fuel -= random.uniform(0, 0.5)
    time.sleep(10)
