# Laporan Praktikum Kriptografi
Minggu ke-: 7  
Topik: Diffie-Hellman Key Exchange 
Nama: Vera Indryawanti    
NIM: 230202791    
Kelas: 5IKRB    

---

## 1. Tujuan
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.  
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.  
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).  

---

## 2. Dasar Teori
Diffie-Hellman (DH) Key Exchange adalah sebuah protokol kriptografi yang memungkinkan dua pihak (umumnya disebut Alice dan Bob) untuk bersama-sama membuat dan menyepakati sebuah kunci rahasia (shared secret) melalui saluran komunikasi publik yang tidak aman. Keindahan protokol ini adalah kunci rahasia tersebut tidak pernah dikirimkan secara eksplisit melalui saluran.  
Mekanisme ini bergantung pada matematika modular dan properti logaritma diskrit (discrete logarithm).  
1. Alice dan Bob menyepakati dua parameter publik: bilangan prima besar p dan sebuah generator (atau basis) g.  
2. Alice memilih sebuah bilangan rahasia privat a dan menghitung kunci publik A = g^a \pmod{p}.  
3. Bob memilih sebuah bilangan rahasia privat b dan menghitung kunci publik B = g^b \pmod{p}.  
4. Alice dan Bob saling bertukar kunci publik mereka (Alice mengirim A ke Bob, Bob mengirim B ke Alice).  
5. Alice menghitung kunci bersama: K = B^a \pmod{p}.  
6. Bob menghitung kunci bersama: K = A^b \pmod{p}.  
Secara matematis, kedua hasil perhitungan akan sama:K = (g^b)^a \pmod{p} = g^{ba} \pmod{p}K = (g^a)^b \pmod{p} = g^{ab} \pmod{p}Pihak ketiga (Eve) yang menyadap komunikasi hanya akan melihat p,  g ,  A , dan  B . Untuk menemukan  K , Eve harus terlebih dahulu menemukan  a  atau  b . Menemukan  a  dari  A, g, p  (masalah logaritma diskrit) dianggap sangat sulit secara komputasi jika  p  berukuran sangat besar.
---

## 3. Alat dan Bahan
- Python   
- Visual Studio Code    
- Git dan akun GitHub  

---

## 4. Langkah Percobaan
1. Membuat struktur folder `praktikum/week7-diffie-hellman/` yang berisi `sub-folder src/`,` screenshots/`, dan file `laporan.md`.  
2. Membuat file baru dengan nama `diffie_hellman.py` di dalam folder `src/`.  
3. Menulis kode program untuk simulasi dasar Diffie-Hellman (sesuai Langkah 1 pada modul) ke dalam file `diffie_hellman.py`.  
4. Menjalankan program dan mengamati bahwa `shared_secret_A` dan `shared_secret_B` memiliki nilai yang sama.  
5. Memodifikasi file `diffie_hellman.py` untuk menambahkan simulasi serangan Man-in-the-Middle (MITM) (sesuai arahan Langkah 2 pada modul).  
6. Menjalankan program yang telah dimodifikasi, mengamati hasilnya, dan mengambil `screenshot` untuk dilampirkan.  
7. Menyalin source code final ke dalam laporan ini.  
8. Menjawab pertanyaan diskusi pada modul di dalam `laporan.md`.  
9. Menyelesaikan laporan dan melakukan commit ke Git dengan pesan `week7-diffie-hellman`.  

---

## 5. Source Code
```python
import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)
```

---

## 6. Hasil dan Pembahasan  
Hasil eksekusi program :

![Hasil Eksekusi](/praktikum/week7-diffie-hellman/screenshots/hasil.png)  

---

## 7. Jawaban Pertanyaan
1. Mengapa Diffie-Hellman memungkinkan pertukaran kunci di saluran publik?Protokol ini aman di saluran publik karena didasarkan pada asimetri kompleksitas komputasi.  
- Mudah: Melakukan eksponensiasi modular (menghitung g^a\pmod{p}) sangat mudah dan cepat bagi komputer.  
- Sulit: Melakukan kebalikannya, yaitu menemukan a jika diketahui g, p, dan A (di mana A = g^a\pmod{p}), adalah masalah Logaritma Diskrit (Discrete Logarithm Problem).Penyadap (Eve) di saluran publik hanya melihat g, p, A, dan B. Untuk mendapatkan kunci rahasia K = g^{ab}\pmod{p}, Eve harus terlebih dahulu menemukan a (dari A) atau b (dari B). Untuk bilangan prima p yang sangat besar (ratusan atau ribuan digit), masalah ini dianggap tidak mungkin dipecahkan (computationaly infeasible) dengan teknologi komputasi saat ini. Sementara itu, Alice dan Bob dapat dengan mudah menghitung K menggunakan kunci privat mereka masing-masing (B^a dan A^b).  
2. Apa kelemahan utama protokol Diffie-Hellman murni?    
Kelemahan utamanya adalah kurangnya autentikasi (lack of authentication). Protokol DH murni tidak memiliki mekanisme bawaan untuk memverifikasi identitas pengirim kunci publik. Alice, ketika menerima kunci publik B, tidak memiliki jaminan bahwa B tersebut benar-benar berasal dari Bob. Ia hanya tahu ia berbagi rahasia dengan siapapun yang mengirim B. Kelemahan inilah yang dieksploitasi oleh serangan Man-in-the-Middle (MITM).
3. Bagaimana cara mencegah serangan MITM pada protokol ini?Serangan MITM dapat dicegah dengan menambahkan lapisan autentikasi untuk memverifikasi kepemilikan kunci publik. Artinya, Alice harus bisa yakin bahwa kunci publik B yang ia terima benar-benar milik Bob, dan sebaliknya. Cara umumnya adalah:  
- Tanda Tangan Digital (Digital Signatures): Alice dan Bob masing-masing menandatangani kunci publik DH mereka (A dan B) menggunakan kunci privat dari pasangan kunci asimetris lain (misalnya, RSA atau ECDSA) yang sudah mereka miliki sebelumnya. Saat bertukar, mereka saling memverifikasi tanda tangan tersebut menggunakan kunci publik RSA/ECDSA pasangannya.  
- Public Key Infrastructure (PKI): Ini adalah pendekatan yang lebih terstruktur. Pihak ketiga yang tepercaya, yang disebut Certificate Authority (CA), akan menerbitkan sertifikat digital. Sertifikat ini mengikat secara kriptografis sebuah identitas (misalnya, "Bob") ke sebuah kunci publik. Ketika Bob mengirimkan kunci publik B ke Alice, ia menyertakan sertifikatnya. Alice kemudian memverifikasi sertifikat tersebut ke CA. Jika valid, Alice yakin bahwa B memang milik Bob. Ini adalah mekanisme yang digunakan dalam protokol seperti HTTPS (TLS/SSL).  
---

## 8. Kesimpulan
Praktikum ini berhasil mensimulasikan protokol Diffie-Hellman Key Exchange. Percobaan pertama menunjukkan keberhasilan dua pihak (Alice dan Bob) dalam menetapkan sebuah kunci rahasia yang identik melalui saluran publik, berkat properti logaritma diskrit.
Percobaan kedua (simulasi MITM) berhasil mengekspos kelemahan fundamental dari protokol DH murni, yaitu ketiadaan autentikasi. Seorang penyerang (Eve) dapat menyadap dan memanipulasi pertukaran, sehingga Alice dan Bob akhirnya membuat kunci rahasia yang berbeda, di mana kedua kunci tersebut diketahui oleh Eve. Hal ini membuktikan bahwa Diffie-Hellman harus diimplementasikan bersama dengan mekanisme autentikasi (seperti tanda tangan digital atau PKI) agar aman dalam penggunaan praktis.  

---

## 9. Daftar Pustaka

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Vera Indryawanti<indryawantivera@gmail.com>
Date:   2025-11-18

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
