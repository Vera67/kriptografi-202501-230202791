# Laporan Praktikum Kriptografi
Minggu ke-: 10  
Topik: Public Key Infrastructure (PKI & Certificate Authority)   
Nama: Vera Indryawanti    
NIM: 230202791    
Kelas: 5IKRB    

---

## 1. Tujuan
1. Membuat sertifikat digital sederhana.   
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.    
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).   

---

## 2. Dasar Teori
Public Key Infrastructure (PKI) adalah seperangkat peran, kebijakan, perangkat keras, perangkat lunak, dan prosedur yang diperlukan untuk membuat, mengelola, mendistribusikan, menggunakan, menyimpan, dan mencabut sertifikat digital dan mengelola enkripsi kunci publik. Tujuan utama PKI adalah untuk memfasilitasi transfer informasi elektronik yang aman untuk berbagai aktivitas jaringan seperti e-commerce, perbankan internet, dan email rahasia.  

Certificate Authority (CA) adalah entitas tepercaya (pihak ketiga) yang menerbitkan sertifikat digital. CA bertindak sebagai penjamin identitas pemilik sertifikat. Sertifikat digital standar yang digunakan adalah format X.509, yang berisi informasi tentang pemilik (Subject), penerbit (Issuer), kunci publik (Public Key), masa berlaku, dan tanda tangan digital dari CA itu sendiri.   

Dalam komunikasi aman seperti HTTPS, sertifikat digital berfungsi untuk memverifikasi bahwa server yang diakses adalah asli dan bukan penipu (impostor), serta menyediakan kunci publik untuk memulai enkripsi sesi (TLS handshake).  

---

## 3. Alat dan Bahan
- Python  
- Visual Studio Code    
- Git dan akun GitHub   
- Library Python: cryptography  

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code


```python
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# 1. Generate key pair (Private & Public Key)
key = rsa.generate_private_key(
    public_exponent=65537, 
    key_size=2048
)

# 2. Buat subject & issuer 
# Karena ini self-signed, Subject dan Issuer adalah sama
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

# 3. Buat sertifikat dengan Builder
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365)) # Berlaku 1 tahun
    .sign(key, hashes.SHA256())
)

# 4. Simpan sertifikat ke file .pem
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat: cert.pem")
```


---

## 6. Hasil dan Pembahasan 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](/praktikum/week10-pki/screenshots/hasil.png)

---

## 7. Jawaban Pertanyaan
1. Apa fungsi utama Certificate Authority (CA)? Fungsi utama CA adalah sebagai pihak ketiga yang tepercaya (Trusted Third Party) yang bertugas memverifikasi identitas pemohon sertifikat dan menerbitkan sertifikat digital. CA menjamin bahwa public key yang terdapat dalam sertifikat benar-benar milik entitas (orang/organisasi/domain) yang tercantum di dalamnya, sehingga mencegah penipuan identitas.  

2. Mengapa self-signed certificate tidak cukup untuk sistem produksi? Self-signed certificate tidak memiliki rantai kepercayaan (chain of trust) ke CA publik yang dikenal. Akibatnya:  
- Browser dan sistem operasi akan menolak koneksi atau memberikan peringatan keamanan merah (Warning: Potential Security Risk) karena penerbit sertifikat tidak dikenali.  
- Tidak ada validasi pihak ketiga, sehingga siapa saja (termasuk penyerang) bisa membuat self-signed certificate atas nama "https://www.google.com/search?q=google.com" atau bank. Tanpa CA tepercaya, pengguna tidak bisa membedakan mana situs asli dan mana tiruan.  

3. Bagaimana PKI mencegah serangan MITM dalam komunikasi TLS/HTTPS? PKI mencegah Man-in-the-Middle (MITM) melalui mekanisme validasi sertifikat:  
- Saat klien (browser) terhubung ke server, server mengirimkan sertifikat digitalnya.  
- Browser mengecek tanda tangan digital pada sertifikat tersebut menggunakan public key milik CA yang sudah tertanam di browser.  
- Jika tanda tangan valid, browser yakin bahwa sertifikat itu asli diterbitkan oleh CA.  
- Browser kemudian mencocokkan domain di URL dengan domain di sertifikat.  
- Jika ada penyerang MITM di tengah jalur mencoba mencegat dan memberikan sertifikat palsu (baik self-signed atau sertifikat curian yang tidak cocok domainnya), browser akan mendeteksi ketidakcocokan tanda tangan atau domain, dan memutus koneksi atau memperingatkan pengguna.  
---

## 8. Kesimpulan
1. Pembuatan sertifikat digital dapat dilakukan secara programatis menggunakan library kriptografi (seperti Python cryptography), yang menghasilkan file berisi kunci publik dan identitas yang ditandatangani.  
2. PKI adalah fondasi keamanan internet modern yang bergantung pada kepercayaan terhadap Certificate Authority (CA).  
3. Sertifikat Self-signed berguna untuk lingkungan pengembangan (development) atau jaringan internal tertutup, namun tidak aman untuk lingkungan produksi publik karena ketiadaan validasi dari pihak ketiga tepercaya.  

---

## 9. Daftar Pustaka


---

## 10. Commit Log

```
commit abc12345
Author: Vera Indryawanti <indryawantivera@gmail.com>
Date:   2025-09-20

    week10-public Key Infrastructure (PKI & Certificate Authority)
```
