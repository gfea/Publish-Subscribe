import paho.mqtt.client as mqtt


def on_connect(client, userdata, rc):
	client.subscribe("data/123")

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))

client = mqtt.Client(client_id='subscriber1')
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)

client.loop_forever()
