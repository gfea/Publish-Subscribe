import socket
import json

inn = 2
server = raw_input("IP Address : ")
port = 5000
s = socket.socket()
s.connect((str(server),int(port)))
while inn != 0:
    print "1. Masuk ke sistem"
    print "0. Keluar"
    inn = input("Masukkan Pilihan : ")
    if inn == 1:
        while True:
            print "Pilihan Menu:"
            print "1. Tambah Nilai"
            print "2. Edit Nilai"
            print "3. Hapus Nilai"
            print "4. Lihat Nilai"
            pil = input("Masukkan Pilihan : ")
            if pil == 1:
                nim = raw_input("Masukkan NIM : ")
                quiz = raw_input("Masukkan Nilai Quiz : ")
                uts = raw_input("Masukkan Nilai UTS : ")
                uas = raw_input("Masukkan Nilai UAS : ")
                pesanjson = {"pil" : pil,
                             "nim" : nim,
                             "quiz" : quiz,
                             "uts" : uts,
                             "uas" : uas}
                pesan = json.dumps(pesanjson)
                s.send(pesan)
                hasil = s.recv(1024)
                print "Data Berhasil Di Inputkan"
            elif pil == 2:
                nim2= raw_input("Masukkan NIM : ")
                pesanjson1 = {"pil" : pil,
                             "nim3" : nim2}
                pesan1 = json.dumps(pesanjson1)
                s.send(pesan1)
                hasil = s.recv(1024)
                if (hasil == "0"):
                    print "Data Tidak Ditemukan"
                else:
                    quiz = raw_input("Masukkan Nilai Quiz : ")
                    uts = raw_input("Masukkan Nilai UTS : ")
                    uas = raw_input("Masukkan Nilai UAS : ")
                    pesanjson = {"pil" : pil,"nim3" : nim2,
                             "quiz1" : quiz,
                             "uts1" : uts,
                             "uas1" : uas}
                    pesan = json.dumps(pesanjson)
                    s.send(pesan)
                    print "Data Berhasil Di Edit"
            elif pil == 3:
                nim2 = raw_input("Masukkan NIM : ")
                pesanjson = {"pil" : pil,
                             "nim2" : nim2}
                pesan = json.dumps(pesanjson)
                s.send(pesan)
                hasil = s.recv(1024)
                if hasil == "0":
                    print "Data Tidak Ditemukan"
                else:
                    print hasil
                    print "Data Berhasil Di Hapus"
            elif pil == 4:
                nim1 = raw_input("Masukkan NIM : ")
                pesanjson = {"pil" : pil,
                             "nim1" : nim1}
                pesan = json.dumps(pesanjson)
                s.send(pesan)
                hasil = s.recv(1024)
                if hasil == "0.0":
                    print "Data Tidak Ditemukan"
                else:
                    print "Nilai Akhir Dari Mahasiswa dengan NIM : ",nim1," Nilai ",float(hasil)
            else:
                print "Perintah operasi tidak ditemukan"
            break
    else:
        break
