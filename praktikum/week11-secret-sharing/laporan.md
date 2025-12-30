# Laporan Praktikum Kriptografi
Minggu ke-: 11  
Topik: Secret Sharing (Shamir’s Secret Sharing)    
Nama: Vera Indryawanti  
NIM: 230202791  
Kelas: 5IKRB  

---

## 1. Tujuan
1. Menjelaskan konsep **Shamir Secret Sharing** (SSS).  
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.  
3. Menganalisis keamanan skema distribusi rahasia.  

---

## 2. Dasar Teori
Shamir's Secret Sharing (SSS) adalah algoritma kriptografi yang dibuat oleh Adi Shamir. Konsep utamanya adalah membagi sebuah "rahasia" (secret) menjadi beberapa bagian unik yang disebut shares. Rahasia tersebut hanya dapat direkonstruksi jika sejumlah minimum shares (disebut threshold atau k) digabungkan kembali. Jika jumlah shares kurang dari k, maka tidak ada informasi apa pun tentang rahasia yang bisa didapatkan.Secara matematis, SSS didasarkan pada interpolasi polinomial Lagrange. Sebuah rahasia S disembunyikan sebagai koefisien konstanta a_0 dalam sebuah polinomial derajat k-1:f(x) = a_0 + a_1x + a_2x^2 + ... + a_{k-1}x^{k-1} (mod p). Di mana p adalah bilangan prima yang lebih besar dari rahasia dan jumlah partisipan (n). Setiap partisipan diberikan pasangan titik (x, f(x)). Untuk merekonstruksi polinomial dan menemukan $a_0$, diperlukan minimal k titik.Keamanan skema ini bersifat information-theoretic secure, artinya musuh yang memiliki daya komputasi tak terbatas pun tidak dapat memecahkan rahasia jika mereka memiliki kurang dari k bagian share.  

---

## 3. Alat dan Bahan
- Python   
- Visual Studio Code / editor lain  
- Git dan akun GitHub   

---

## 4. Langkah Percobaan
1. Membuat struktur folder `praktikum/week11-secret-sharing/src/` dan `screenshots/`.
2. Menginstall library yang diperlukan dengan menjalankan perintah di terminal: `pip install secretsharing`.
3. Membuat file bernama `secret_sharing.py` di dalam folder `src/`.
4. Menulis kode program untuk membagi rahasia (splitting) dan menggabungkan kembali (recovering) menggunakan library `secretsharing` sesuai panduan modul.
5. Menjalankan program dengan perintah: `python src/secret_sharing.py`
6. Mengambil screenshot hasil output terminal untuk dokumentasi.

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

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
