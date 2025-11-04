# Laporan Praktikum Kriptografi
Minggu ke-: 4 
Topik: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)  
Nama: Vera Indryawanti  
NIM: 230202791 
Kelas: 5IKRB  

---

## 1. Tujuan
1. Menyelesaikan perhitungan sederhana terkait entropi kunci.  
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers (meskipun tidak disimulasikan secara eksplisit pada contoh kode, ini adalah tujuan praktikum).  
3. Menghitung unicity distance untuk ciphertext tertentu.  
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.  
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

---

## 2. Dasar Teori
Entropi itu cara mengukur seberapa acak atau seberapa tidak terduga sebuah kunci. Gampangnya, entropi (H(K)) mengukur seberapa besar "ruang kunci" (jumlah semua kemungkinan kunci). Rumusnya $H(K) = \log_2 |K|$. Makin besar angkanya (makin tinggi entropinya), kuncinya makin kuat dan makin susah ditebak.Unicity Distance ($U$) adalah panjang ciphertext (pesan rahasia) paling pendek yang kita butuhkan supaya bisa menemukan kunci yang benar. Kalau ciphertext-nya lebih pendek dari $U$, kita mungkin dapat banyak kunci palsu yang kelihatan benar. Kalau ciphertext kita lebih panjang dari $U$, kita hampir pasti bisa menemukan satu kunci yang benar.Serangan Brute Force adalah serangan "coba-coba". Penyerang akan mencoba semua kemungkinan kunci satu per satu sampai ketemu yang benar dan pesannya bisa dibaca.

---

## 3. Alat dan Bahan
- Python   
- Visual Studio Code / editor lain  
- Git dan akun GitHub    

---

## 4. Langkah Percobaan
- Bikin folder `praktikum/week4-entropy-unicity/`.  
- Di dalamnya, bikin folder `src/` dan `screenshots/`.  
- Bikin file `laporan.md` (file ini) di folder utama.  
- Bikin file `entropy_unicity.py` di dalam folder `src/`.  
- Masukkan kode Python dari modul ke file `entropy_unicity.py`.  
- Jalankan programnya dari terminal (pakai `python src/entropy_unicity.py`).  
- Screenshot hasilnya, simpan di folder `screenshots/` dengan nama `hasil.png`.  
- Isi laporan ini (`laporan.md`) dengan teori, hasil, dan jawaban.  
- Commit semua file ke GitHub dengan pesan: `week4-entropy-unicity`.

---

## 5. Source Code
```python
#Perhitungan Entropi
import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")

#Menghitung Unicity Distance
def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))

# Analisis Brute Force
def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
```
---

## 6. Hasil dan Pembahasan  
Hasil eksekusi program :

![Hasil Eksekusi](/praktikum/week4-entropy-unicity/Screenshots/Hasil.png)



---

## 7. Jawaban Pertanyaan
1. Apa arti dari nilai entropy dalam konteks kekuatan kunci?  
Entropi itu ukuran kekuatan kunci. Makin tinggi entropinya, makin banyak jumlah kemungkinan kuncinya, dan makin acak kuncinya. Kalau entropinya 128 bit (kayak AES), artinya ada $2^{128}$ kunci yang harus dicoba. Kalau entropinya 4.7 bit (kayak Caesar), cuma ada 26 kunci. Jadi, makin tinggi entropi, makin aman dari serangan brute force.2.  
2. Mengapa unicity distance penting dalam menentukan keamanan suatu cipher?  
Unicity distance itu penting untuk tahu seberapa panjang ciphertext yang dibutuhkan biar kita yakin kuncinya cuma satu. Kalau unicity distance-nya kecil (misal 3), artinya penyerang cuma butuh 3 huruf ciphertext untuk menebak kuncinya pakai statistik bahasa. Ini menunjukkan cipher itu lemah. Kalau unicity distance-nya besar, cipher-nya lebih aman dari serangan statistik.  
3. Mengapa brute force masih menjadi ancaman meskipun algoritma sudah kuat?  
Brute force masih bahaya karena:  
- Komputer Makin Cepat: Teknologi (terutama komputer kuantum nanti) bikin komputer bisa mencoba kunci lebih cepat. Kunci yang aman hari ini (misal 112 bit) mungkin tidak aman 20 tahun lagi.  
- Kesalahan Manusia: Orang sering pakai password (kata sandi) yang gampang ditebak (seperti "123456" atau "password"). Ini sama saja memperkecil jumlah kunci yang harus dicoba (ini disebut dictionary attack, bagian dari brute force).  
- Implementasi yang Salah: Kadang algoritmanya kuat (seperti AES), tapi cara pakainya salah. Misalnya, kunci yang dipakai ulang atau kuncinya dibuat dengan cara yang gampang ditebak. Ini membuat serangan jadi lebih mudah.
---

## 8. Kesimpulan
Dari praktikum ini, kita belajar kalau kekuatan kunci bisa diukur pakai entropi. Caesar Cipher sangat lemah (entropi 4.7 bit, unicity distance 2.67) dan bisa dibobol instan. AES-128 sangat kuat (entropi 128 bit) dan tidak mungkin di-brute force dengan teknologi sekarang.

---

## 9. Daftar Pustaka


---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Vera Indryawanti <indryawantivera@gmail.com>
Date:   2025-11-04

    week4-Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force) )
```
