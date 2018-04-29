# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

print("Hello, World!")
mqttc = mqtt.Client("python_pub")
mqttc.connect("s0.iotnesia.com", 1883)
mqttc.publish("supri", "Hello, World!")
mqttc.loop(2) #timeout = 2s
