import random
import datetime

print("QUIZ TEBAK ANGGARAN HILANG ")

#menampilkan waktu quiz dimulai
sekarang = datetime.datetime.now() #mengambil waktu sekarang dari sistem
print("Quiz dimulai:", sekarang) #menampilkan waktu mulai quiz
print()

#daftar soal quiz (menggunakan struktur data list dan dictionary)
soal = [
    {
        "pertanyaan": "Anggaran bangun taman kota: 2 M.\nTapi tamannya kecil banget.\nMenurut kamu kenapa?",
        "opsi": [
            "1. Harga bahan mahal",
            "2. Banyak biaya tambahan",
            "3. Tidak jelas kemana"
        ],
        "jawaban": "3"
    },
    {
        "pertanyaan": "Proyek jalan desa anggarannya 5 M.\nJalannya cepat rusak.\nKenapa ya?",
        "opsi": [
            "1. Dananya kepotong di jalan",
            "2. Salah perhitungan",
            "3. Kualitas bahan kurang bagus"
        ],
        "jawaban": "1"
    },
    {
        "pertanyaan": "Renovasi gedung kantor katanya habis 3 M.\nTapi kelihatannya tidak banyak berubah.\nMenurut kamu kenapa?",
        "opsi": [
            "1. Banyak biaya rapat",
            "2. Anggarannya entah kemana",
            "3. Biaya tidak terduga"
        ],
        "jawaban": "2"
    }
]

#mengacak urutan soal agar tidak monoton saat dijalankan
random.shuffle(soal)

skor = 0 #variabel untuk menyimpan skor quiz

#menampilkan soal satu per satu
for i in range(len(soal)):
    print("Soal", i+1)                  #menampilkan nomor soal
    print(soal[i]["pertanyaan"])        #menampilkan pertanyaan

    #pilihan jawaban
    for opsi in soal[i]["opsi"]:
        print(opsi)

    #input jawaban user
    jawaban = input("Jawaban kamu: ")

    #cek jawaban user benar atau salah
    if jawaban == soal[i]["jawaban"]:
        print("Betul juga sih 😅")
        skor += 1         #nambah skor jika jawaban benar
    else:
        print("Hmmzz... coba dipikirkan secara logika.")

    print()     #memberi jarak dari soal ke soal

#setelah semua selesai
print("Quiz selesai!") 
print("Skor kamu:", skor, "dari", len(soal))        #menampilkan skor akhir