# Author : Refri Rifwan Daharmi
# Email : refririfwan@student.ub.ac.id
# Publisher Kelembapan

import paho.mqtt.client as mqtt
import time

broker = "iot.eclipse.org"
port = 1883

client = mqtt.Client()

client.connect(broker,port)
print("publish node is running")

kelembapan = 48

while True:
    client.publish(topic='dtsKelembapan',payload=kelembapan)
    time.sleep(15)
