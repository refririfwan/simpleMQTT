# Author : Refri Rifwan Daharmi
# Email : refririfwan@student.ub.ac.id
# Subcriber

import paho.mqtt.client as mqtt

broker = "iot.eclipse.org"
port = 1883

def on_connect (client,userdata,flag,rc):
    print("Connect with result code "+rc)


def on_message (client,userdata,message):
    print("Message received  from others: "+message.payload.decode())

def on_message_from_suhu (client,userdata,message):
    print("Message received  from suhu : "+message.payload.decode())

def on_message_from_kelembapan (client,userdata,message):
    print("Message received  from kelembapan : "+message.payload.decode())


client = mqtt.Client()

client.on_connect=on_connect
client.on_message = on_message
client.connect(broker,port)

client.subscribe("dtsOthers", qos=1)
client.subscribe("dtsSuhu", qos=1)
client.subscribe("dtsKelembapan", qos=1)

client.message_callback_add("dtsSuhu", on_message_from_suhu)
client.message_callback_add("dtsKelembapan", on_message_from_kelembapan)

client.loop_forever()
