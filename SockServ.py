import socket
import json
import xmlrpclib

port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('' ,port))

s.listen(1)
c, addr = s.accept()
proxy1 = xmlrpclib.ServerProxy("http://127.0.0.1:3600")

while True:
    data = c.recv(1024)
    pesan = json.loads(data)
    pilihan = pesan['pil']
    if pilihan == 1:
        nim = int(pesan['nim'])
        quiz = int(pesan['quiz'])
        uts = int(pesan['uts'])
        uas = int(pesan['uas'])
        print "pesan diterima pada server : ",proxy1
        hasil = proxy1.rata(quiz,uts,uas,nim)
        kirim = float(hasil)
        c.send(str(kirim))
    elif pilihan == 2:
        f = int(pesan['nim3'])
        hasil = proxy1.cek(f)
        c.send(str(hasil))
        if hasil == f:
            data1 = c.recv(1024)
            pesan1 = json.loads(data1)
            f1 = int(pesan1['nim3'])
            g = int(pesan1['quiz1'])
            h = int(pesan1['uts1'])
            i = int(pesan1['uas1'])
            print "pesan diterima pada server : ",proxy1
            hasil1 = proxy1.edit(g,h,i,f1)
    elif pilihan == 3:
        b = int(pesan['nim2'])
        print "pesan diterima pada server : ",proxy1
        hasil = proxy1.hapus(b)
        c.send(str(hasil))
    elif pilihan == 4:
        a = int(pesan['nim1'])
        print "pesan diterima pada server : ",proxy1
        hasil = proxy1.lihat(a)
        kirim = float(hasil)
        c.send(str(kirim))
    else:
        print "Perintah tidak ditemukan"
        c.close()