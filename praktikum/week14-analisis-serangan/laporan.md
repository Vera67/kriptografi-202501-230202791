# Laporan Praktikum Kriptografi
Minggu ke-: 14    
Topik: Analisis Serangan Kriptografi (Studi Kasus: Brute Force pada MD5)  
Nama: Vera Indryawanti    
NIM: 230202791    
Kelas: 5IKRB    

---

## 1. Tujuan
1. Mengidentifikasi jenis serangan pada sistem informasi nyata.  
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.  
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.

---

## 2. Dasar Teori
Fungsi Hash dan MD5 Fungsi hash kriptografi adalah algoritma yang mengubah data input menjadi string byte dengan panjang tetap. MD5 (Message-Digest Algorithm 5) adalah fungsi hash yang banyak digunakan di masa lalu yang menghasilkan nilai hash 128-bit. Namun, saat ini MD5 dianggap tidak aman karena kerentanannya terhadap serangan collision (bentrokan) dan kecepatannya yang memungkinkan serangan brute force dilakukan dengan sangat cepat menggunakan perangkat keras modern.  

Serangan Brute Force dan Dictionary Attack Brute force adalah metode serangan di mana penyerang mencoba semua kemungkinan kombinasi kunci atau password hingga menemukan yang cocok. Dictionary attack adalah variasi yang lebih efisien di mana penyerang menggunakan daftar kata-kata umum (kamus) untuk menebak password. Jika sistem menyimpan password hanya dalam bentuk hash MD5 tanpa salt (data acak tambahan), penyerang dapat menggunakan Rainbow Table atau dictionary attack untuk membalikkan hash tersebut menjadi plaintext.  

Solusi: Salt dan Algoritma Modern Untuk memitigasi serangan ini, penggunaan Salt (nilai acak unik untuk setiap pengguna) sangat penting agar dua password yang sama memiliki hash yang berbeda. Selain itu, penggunaan algoritma yang lebih lambat dan kuat seperti SHA-256, bcrypt, atau Argon2 sangat disarankan.  

---

## 3. Alat dan Bahan
- Python   
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan   

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Panduan Langkah demi Langkah


---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
