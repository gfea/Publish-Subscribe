import time, random, sys
import paho.mqtt.client as paho
import xmlrpclib

def on_publish(client, userdata, data):
	print("published data id: "+str(data))

client = paho.Client(client_id="dosen")
client.on_publish = on_publish

client.connect("127.0.0.1", 1883)
client.loop_start()

while True:
	data = 1
	(rc, pub) = client.publish("data/matakuliah", data ,qos=1)



