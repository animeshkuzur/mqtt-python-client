# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub")
mqttc.connect("192.168.0.127", 1883)
mqttc.publish("room/socket1", "Hello World")
mqttc.loop(2) //timeout = 2s