# Author : Refri Rifwan Daharmi
# Email : refririfwan@student.ub.ac.id
# Publisher Suhu

import paho.mqtt.client as mqtt
import time

broker = "iot.eclipse.org"
port = 1883

client = mqtt.Client()

client.connect(broker,port)
print("publish node is running")

while True:
    suhu=input("masukan nilai suhu : ")
    client.publish(topic='dtsKelembapan',payload=suhu)
    time.sleep(10)
