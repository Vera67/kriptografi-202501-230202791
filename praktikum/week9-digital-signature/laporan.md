# Laporan Praktikum Kriptografi
Minggu ke-: 9    
Topik: Digital Signature (RSA/DSA)    
Nama: Vera Indryawanti    
NIM: 230202791    
Kelas: 5IKRB    

---

## 1. Tujuan
1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.    
2. Memverifikasi keaslian tanda tangan digital.    
3. Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.   

---

## 2. Dasar Teori
Tanda Tangan Digital (Digital Signature) adalah skema matematis yang digunakan untuk membuktikan keaslian pesan atau dokumen digital. Skema ini memberikan jaminan bahwa pesan tersebut benar-benar berasal dari pengirim yang diklaim (otentikasi), pesan tidak diubah selama transit (integritas), dan pengirim tidak dapat menyangkal telah mengirim pesan tersebut (non-repudiation).  

Dalam algoritma asimetris seperti RSA (Rivest-Shamir-Adleman), proses penandatanganan bekerja berkebalikan dengan enkripsi. Pengirim membuat tanda tangan menggunakan Private Key miliknya pada hash dari pesan tersebut. Penerima kemudian memverifikasi tanda tangan tersebut menggunakan Public Key pengirim. Jika verifikasi berhasil, berarti pesan tersebut valid dan belum dimodifikasi.  

Biasanya, pesan tidak ditandatangani secara langsung karena ukurannya yang besar. Sebaliknya, fungsi hash (seperti SHA-256) digunakan untuk membuat ringkasan pesan (digest), dan digest inilah yang dienkripsi dengan private key untuk membentuk tanda tangan digital.

---

## 3. Alat dan Bahan
- Python   
- Visual Studio Code / editor lain  
- Git dan akun GitHub   

---

## 4. Langkah Percobaan
1. Persiapan Folder: Membuat struktur folder kerja: `praktikum/week9-digital-signature/` yang berisi folder `src, screenshots`, dan file `laporan.md`.  
2. Instalasi Library: Menginstal library yang dibutuhkan melalui terminal:  
- `Bash`  
- `pip install pycryptodome`  
3. Pembuatan Program: Membuat file `signature.py` di dalam folder `src/`.  
4. Implementasi Kode: Menulis kode program untuk:  
- Membangkitkan pasangan kunci RSA (2048 bit).  
- Melakukan hashing pada pesan menggunakan SHA-256.  
- Membuat tanda tangan digital menggunakan Private Key.  
- Memverifikasi tanda tangan menggunakan Public Key.  
- Menguji verifikasi pada pesan yang telah dimodifikasi (pesan palsu).  
5. Eksekusi Program: Menjalankan program dengan perintah `python src/signature.py` dan mendokumentasikan hasilnya.  
---

## 5. Source Code

```python
# Generate Key dan Buat Tanda Tangan
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Buat tanda tangan dengan private key
signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())

# Verifikasi Tanda Tangan
try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")

# Uji Modifikasi Pesan

# Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")
```

---

## 6. Hasil dan Pembahasan
Hasil eksekusi program :

![Hasil Eksekusi](/praktikum/week9-digital-signature/screenshots/Hasil.png)

---

## 7. Jawaban Pertanyaan
1. Apa perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA?  
Enkripsi RSA: Menggunakan Public Key penerima untuk mengenkripsi pesan (menjaga kerahasiaan/confidentiality), dan hanya Private Key penerima yang bisa membukanya.Tanda Tangan Digital RSA: Menggunakan Private Key pengirim untuk menandatangani hash pesan (menjaga otentikasi dan integritas), dan Public Key pengirim digunakan oleh siapa saja untuk memverifikasi keasliannya.

2. Mengapa tanda tangan digital menjamin integritas dan otentikasi pesan?  
- Integritas: Karena tanda tangan dibuat berdasarkan hash dari pesan. Jika satu karakter saja dalam pesan berubah, nilai hash akan berubah drastis, sehingga verifikasi tanda tangan akan gagal.  
- Otentikasi: Karena tanda tangan hanya bisa dibuat menggunakan Private Key. Asalkan Private Key dijaga kerahasiaannya oleh pemilik, maka siapa pun yang berhasil memverifikasi tanda tangan tersebut bisa yakin bahwa pesan itu benar-benar berasal dari pemilik kunci tersebut.  

3. Bagaimana peran Certificate Authority (CA) dalam sistem tanda tangan digital modern?   
CA berperan sebagai pihak ketiga yang terpercaya (Trusted Third Party). Masalah utama dalam kriptografi kunci publik adalah memvalidasi bahwa "Public Key A" benar-benar milik "Orang A". CA menerbitkan sertifikat digital yang mengikat identitas seseorang/organisasi dengan Public Key mereka. Tanpa CA, serangan Man-in-the-Middle lebih mudah terjadi karena penyerang bisa mengaku sebagai orang lain dengan memberikan Public Key palsu.  
---

## 8. Kesimpulan
Kesimpulannya adalah bahwa algoritma RSA dan fungsi hash SHA-256 dapat diimplementasikan menggunakan library `pycryptodome` untuk membuat sistem Tanda Tangan Digital. Sistem ini terbukti mampu mendeteksi perubahan sekecil apapun pada pesan (menjamin integritas) dan memastikan pesan berasal dari pengirim yang sah (otentikasi).  
---

## 9. Daftar Pustaka


---

## 10. Commit Log

```
commit abc12345
Author: Vera Indryawanti <indryawantivera@gmail.com>
Date:   2025-09-20

    week9-digital-signature
```
