import paho.mqtt.client as paho

mqttc = paho.Client(client_id="pub")
mqttc.connect("localhost", 1883)
mqttc.publish("hello/world", "Hello, World!")
mqttc.loop(4)