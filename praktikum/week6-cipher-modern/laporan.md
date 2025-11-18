# Laporan Praktikum Kriptografi
Minggu ke-: 6    
Topik: Cipher Modern (DES, AES, RSA)  
Nama: Vera Indryawanti  
NIM: 230202791  
Kelas: 5IKRB  

---

## 1. Tujuan
1. Mengimplementasikan algoritma DES untuk blok data sederhana.  
2. Menerapkan algoritma AES dengan panjang kunci 128 bit.  
3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.  

---

## 2. Dasar Teori
Cipher modern merupakan algoritma kriptografi yang digunakan saat ini, menggantikan cipher klasik yang sudah tidak aman. Secara umum, cipher modern dibagi menjadi dua kategori utama:  
1. Kriptografi Simetris (Symmetric-Key): Algoritma ini menggunakan kunci yang sama untuk proses enkripsi dan dekripsi. Pengirim dan penerima harus berbagi kunci rahasia yang sama. Contohnya adalah DES (Data Encryption Standard) dan AES (Advanced Encryption Standard). DES adalah standar lama dengan kunci 56-bit yang kini dianggap tidak aman. AES adalah standar industri saat ini, mendukung kunci 128, 192, atau 256 bit, dan jauh lebih aman.  
2. Kriptografi Asimetris (Asymmetric-Key): Algoritma ini menggunakan sepasang kunci: kunci publik (public key) untuk enkripsi dan kunci privat (private key) untuk dekripsi. Kunci publik dapat didistribusikan secara bebas, sedangkan kunci privat harus dijaga kerahasiaannya oleh pemilik. Contoh paling populer adalah RSA. Keamanannya bergantung pada kesulitan matematis untuk memfaktorkan bilangan prima besar.  

---

## 3. Alat dan Bahan
- Python   
- Visual Studio Code  
- Git dan akun GitHub  

---

## 4. Langkah Percobaan
1. Membuat struktur direktori proyek sesuai panduan:  
`praktikum/week6-cipher-modern/`
`├─ src/`
`├─ screenshots/`
`└─ laporan.md`
2. Melakukan instalasi library `pycryptodome` yang diperlukan menggunakan perintah pip install `pycryptodome`.  
3. Membuat file `src/des.py` (opsional) untuk simulasi enkripsi/dekripsi DES mode ECB.  
4. Membuat file `src/aes.py` untuk implementasi enkripsi/dekripsi AES-128 menggunakan mode EAX.  
5. Membuat file `src/rsa.py` untuk implementasi pembangkitan key pair (2048 bit) serta proses enkripsi (dengan public key) dan dekripsi (dengan private key) menggunakan PKCS1_OAEP.  
6. Menjalankan ketiga skrip Python tersebut dan mengambil screenshot hasilnya.   
7. Menyimpan hasil screenshot di dalam folder `screenshots/`.  
8. Menyusun laporan ini (`laporan.md`) dan menjawab pertanyaan diskusi.    
9. Melakukan commit hasil pekerjaan ke repositori Git dengan pesan commit `week6-cipher-modern`.  

---

## 5. Source Code
Langkah 1 — Implementasi DES (Opsional, Simulasi)
```python
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)  
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)
```
---

Langkah 2 — Implementasi AES-128
```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  
cipher = AES.new(key, AES.MODE_EAX)

plaintext = b"Modern Cipher AES Example"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("Ciphertext:", ciphertext)

cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```
---

Langkah 3 — Implementasi RSA
```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Enkripsi dengan public key
cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"RSA Example"
ciphertext = cipher_rsa.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi dengan private key
decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```
---

---

## 6. Hasil dan Pembahasan
Hasil eksekusi program :

![Hasil Eksekusi](/praktikum/week6-cipher-modern/screenshots/DES.png)
![Hasil Input](/praktikum/week6-cipher-modern/screenshots/AES-128.png)
![Hasil Output](/praktikum/week6-cipher-modern/screenshots/RSA.png)


---

## 7. Jawaban Pertanyaan  
1. Apa perbedaan mendasar antara DES, AES, dan RSA dalam hal kunci dan keamanan?  
Jenis Kunci:  
    - DES & AES: Kriptografi simetris. Keduanya menggunakan satu kunci yang sama (kunci rahasia) untuk enkripsi dan dekripsi.  
    - RSA: Kriptografi *asimetris*. Menggunakan dua kunci yang berbeda namun terkait secara matematis: kunci publik (untuk enkripsi) dan kunci privat (untuk dekripsi).  
Keamanan & Panjang Kunci:  
    - DES: Panjang kunci 64 bit (hanya 56 bit yang efektif). Saat ini dianggap tidak aman karena kuncinya terlalu pendek dan dapat dibobol dengan *brute-force* dalam waktu singkat.  
    - AES: Standar modern. Mendukung kunci 128, 192, atau 256 bit. Dianggap sangat aman dan efisien.  
    - RSA: Keamanan didasarkan pada kesulitan memfaktorkan bilangan prima besar. Panjang kunci biasanya jauh lebih besar (misal 2048 bit atau 4096 bit) untuk mencapai tingkat keamanan yang sebanding dengan AES.  

2. Mengapa AES lebih banyak digunakan dibanding DES di era modern?
Alasan utamanya adalah keamanan. Kunci 56-bit DES terlalu kecil untuk komputasi modern. Sebuah serangan *brute-force* (mencoba setiap kemungkinan kunci) dapat memecahkan DES dalam hitungan jam atau hari. Sebaliknya, AES-128 (kunci 128-bit) secara komputasi tidak mungkin di-*brute-force* dengan teknologi saat ini. Selain itu, AES juga dirancang agar lebih efisien dan cepat, baik dalam implementasi perangkat lunak maupun perangkat keras, dibandingkan dengan 3DES (varian DES yang lebih aman namun lambat).  

3. Mengapa RSA dikategorikan sebagai algoritma asimetris, dan bagaimana proses pembangkitan kuncinya?
Kategori Asimetris: RSA dikategorikan asimetris karena menggunakan dua kunci yang berbeda. Satu kunci (publik) digunakan untuk mengunci (enkripsi), dan satu kunci lain (privat) digunakan untuk membuka (dekripsi). Kunci privat tidak dapat (atau sangat sulit secara komputasi) ditebak meskipun kunci publiknya diketahui.    
Proses Pembangkitan Kunci (Sederhana):  
    1. Pilih dua bilangan prima acak yang sangat besar, sebut saja p dan q.  
    2. Hitung modulus n = p \times q. Nilai n ini akan digunakan untuk kunci publik dan privat.  
    3. Hitung *totient* Euler: \phi(n) = (p-1) \times (q-1).  
    4. Pilih sebuah bilangan bulat e (eksponen publik), yang biasanya 65537.  
    5. Hitung eksponen privat d sedemikian rupa sehingga (d \times e) \mod \phi(n) = 1. ( d adalah invers modular dari e ).  
    6. Kunci Publik adalah pasangan (e, n).  
    7. Kunci Privat adalah pasangan (d, n).    
---

## 8. Kesimpulan  
Praktikum ini telah berhasil mengimplementasikan tiga algoritma cipher modern (DES, AES, dan RSA) menggunakan library `pycryptodome` di Python. Melalui percobaan, dapat dipahami perbedaan fundamental antara kriptografi simetris (AES/DES) yang menggunakan satu kunci rahasia, dan kriptografi asimetris (RSA) yang menggunakan pasangan kunci publik-privat. Implementasi AES-128 dan RSA-2048 menunjukkan cara mengamankan data sesuai standar modern.  

---

## 9. Daftar Pustaka


---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Vera Indryawanti <indryawantivera@gmail.com>
Date:   2025-11-18

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
