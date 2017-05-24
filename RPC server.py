from SimpleXMLRPCServer import SimpleXMLRPCServer
import paho.mqtt.client as paho
port = 3600

def on_publish(client, userdata, data):
	print("published data id: "+str(data))

client = paho.Client(client_id="dosen")
client.on_publish = on_publish

client.connect("127.0.0.1", 1883)
client.loop_start()
datamhs = {}
def cek(a):
    if a in datamhs:
        return a
    else:
        z = 0
        return z
def rata(a,b,c,d):
    x = float(a)
    y = float(b)
    z = float(c)
    aa = (x+y+z)/3
    hasil = float(aa)
    datamhs[d] = hasil
    print datamhs
    topik = "data/"+str(d)
    (rc, pub) = client.publish(topik, hasil ,qos=1)
    return hasil
def lihat(a):
    if a in datamhs:
        print datamhs[a]
        return datamhs[a]
    else:
        z = 0
        return z
def edit(a,b,c,d):
    if d in datamhs:
        x = float(a)
        y = float(b)
        z = float(c)
        aa = (x+y+z)/3
        hasil = float(aa)
        datamhs[d] = hasil
        topik = "data/"+str(d)
        (rc, pub) = client.publish(topik, hasil ,qos=1)
        return hasil
    else:
        z = 0
        return z
def hapus(a):
    if a in datamhs:
        del datamhs[a]
        x = 1
        return x
        print datamhs
    else:
        z = 0
        return z
server = SimpleXMLRPCServer(("", port),allow_none=True)
server.register_function(rata, "rata")
server.register_function(edit, "edit")
server.register_function(lihat, "lihat")
server.register_function(hapus, "hapus")
server.register_function(cek, "cek")
server.serve_forever()