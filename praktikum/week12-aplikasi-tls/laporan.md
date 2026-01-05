# Laporan Praktikum Kriptografi
Minggu ke-: 12    
Topik: Aplikasi TLS & E-commerce    
Nama: Vera Indryawanti    
NIM: 230202791   
Kelas: 5IKRB    

---

## 1. Tujuan
1. Menganalisis penggunaan kriptografi pada email dan SSL/TLS.  
2. Menjelaskan enkripsi dalam transaksi e-commerce.   
3. Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.

---

## 2. Dasar Teori
Transport Layer Security (TLS) dan pendahulunya, Secure Sockets Layer (SSL), adalah protokol kriptografi yang dirancang untuk memberikan keamanan komunikasi melalui jaringan komputer. Konsep dasar dari TLS melibatkan tiga aspek keamanan utama: kerahasiaan (confidentiality) melalui enkripsi simetris, integritas (integrity) melalui kode otentikasi pesan, dan otentikasi (authentication) menggunakan sertifikat digital .  
Sertifikat Digital adalah komponen krusial dalam TLS yang dikeluarkan oleh Certificate Authority (CA). Sertifikat ini berfungsi memverifikasi identitas pemilik website (misalnya, membuktikan bahwa server Tokopedia benar-benar milik Tokopedia) dan mendistribusikan kunci publik (public key) untuk memulai pertukaran kunci sesi yang aman.  
Dalam konteks E-commerce, penerapan TLS (ditandai dengan HTTPS) sangat vital untuk melindungi data sensitif pengguna, seperti password, nomor kartu kredit, dan data pribadi lainnya dari serangan seperti Man-in-the-Middle (MitM) atau sniffing saat data transit di internet.  

---

## 3. Alat dan Bahan
- Python
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan  

---

## 4. Langkah Percobaan
1. Persiapan Lingkungan: Membuat struktur folder `praktikum/week12-aplikasi-tls/` beserta subfolder `screenshots/`.    
2. Analisis Sertifikat: Membuka website e-commerce menggunakan browser, menekan ikon gembok (lock) di address bar, dan melihat detail sertifikat ("Connection is secure" > "Certificate is valid").  
3. Pencatatan Data: Mencatat Issuer CA, masa berlaku, dan algoritma enkripsi (RSA/ECDSA).  
4. Studi Kasus: Menganalisis bagaimana alur login dan pembayaran dilindungi oleh HTTPS.  
5. Analisis Etika: Melakukan studi literatur singkat mengenai isu privasi email karyawan dan regulasi pemerintah.  

---

## 5. Panduan Langkah demi Langkah
A. Analisis SSL/TLS pada Website E-commerce  
Berikut adalah hasil tangkapan layar dan analisis sertifikat dari dua website e-commerce berbeda.  
1. Website: Tokopedia (Ganti placeholder di atas dengan screenshot tab "Details" sertifikat di browser)  
- Issuer: Google Trust Services (atau DigiCert, tergantung update terbaru).   
- Algoritma: Menggunakan enkripsi asimetris (biasanya RSA atau ECC) untuk pertukaran kunci, dan AES untuk enkripsi data sesi.  
- Pembahasan: Penggunaan sertifikat valid memastikan bahwa browser pengguna berkomunikasi langsung dengan server Tokopedia asli. Jika sertifikat kadaluarsa atau self-signed, browser akan memblokir akses dengan peringatan keamanan.

2. Website: Shopee (Ganti placeholder di atas dengan screenshot tab "Details" sertifikat di browser)  
- Issuer: Sectigo / DigiCert.  
- Masa Berlaku: Biasanya 3 bulan hingga 1 tahun (perbaruan otomatis sering dilakukan untuk keamanan).  
- Pembahasan: Kedua website ini menggunakan HTTPS secara penuh (Always-on SSL). Perbedaan dengan HTTP biasa adalah data yang dikirim di HTTP berupa plain text (mudah dibaca peretas), sedangkan HTTPS mengenkripsi data tersebut sehingga tidak terbaca meskipun disadap.  

B. Studi Kasus Keamanan Transaksi  
Dalam proses login dan pembayaran, e-commerce menggunakan TLS untuk membungkus paket data HTTP.  
- Ancaman: Tanpa TLS, serangan Man-in-the-Middle (MitM) sangat mudah dilakukan, terutama jika pengguna menggunakan Wi-Fi publik. Penyerang dapat menyisipkan diri di antara pengguna dan server untuk mencuri session cookie atau password.  
- Mitigasi: Dengan TLS, server dan klien melakukan handshake di awal. Sekalipun penyerang menyadap data, mereka hanya melihat karakter acak (ciphertext) yang tidak bisa didekripsi tanpa kunci sesi yang hanya diketahui oleh pengguna dan server.  

C. Analisis Etika & Privasi  
- Isu Email Karyawan: Terdapat dilema etika mengenai apakah perusahaan berhak mendekripsi email karyawan (misalnya menggunakan SSL Inspection/Proxy).  
- Perspektif Perusahaan: Perlu dilakukan untuk audit keamanan (mencegah kebocoran data rahasia perusahaan/DLP) dan kepatuhan hukum.  
- Perspektif Privasi: Karyawan memiliki hak privasi dasar. Pemantauan tanpa persetujuan atau pemberitahuan transparan dianggap pelanggaran etika berat.  
- Solusi Etis: Kebijakan harus tertulis jelas dalam kontrak kerja bahwa email kantor hanya untuk keperluan kerja dan dapat diaudit.  

D. Isu Pemerintah (Government Backdoor): Pemerintah sering meminta "kunci belakang" (backdoor) pada aplikasi pesan terenkripsi (seperti WhatsApp) dengan alasan keamanan nasional (terorisme). Namun, secara teknis dan etis, menciptakan backdoor akan melemahkan sistem enkripsi secara keseluruhan, yang justru membahayakan privasi seluruh warga negara dari pihak jahat lainnya.  

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Input](/kriptografi-202501-230202791/praktikum/week12-aplikasi-tls/screenshots/lazada.png)
![Hasil Input](/kriptografi-202501-230202791/praktikum/week12-aplikasi-tls/screenshots/shopee.png)
![Hasil Input](/kriptografi-202501-230202791/praktikum/week12-aplikasi-tls/screenshots/tokopedia.png)
)

---

## 7. Jawaban Pertanyaan
1. Apa perbedaan utama antara HTTP dan HTTPS?   
HTTP (Hypertext Transfer Protocol) mengirimkan data dalam format teks biasa (plain text) melalui port 80, sehingga tidak aman karena data dapat dibaca oleh siapa saja yang menyadap jaringan. HTTPS (HTTP Secure) adalah versi HTTP yang dilapisi protokol SSL/TLS (biasanya port 443), yang mengenkripsi seluruh komunikasi data sehingga menjamin kerahasiaan dan integritas data.  

2. Mengapa sertifikat digital menjadi penting dalam komunikasi TLS?   
Sertifikat digital berfungsi sebagai "KTP" atau identitas digital yang terverifikasi. Tanpa sertifikat yang divalidasi oleh Certificate Authority (CA) terpercaya, pengguna tidak bisa membedakan apakah mereka sedang berkomunikasi dengan server asli (misal: bank) atau server palsu milik peretas. Sertifikat mencegah serangan penyamaran (spoofing).  

3. Bagaimana kriptografi mendukung privasi dalam komunikasi digital, tetapi sekaligus menimbulkan tantangan hukum dan etika?  
Kriptografi (khususnya End-to-End Encryption) memastikan hanya pengirim dan penerima yang bisa membaca pesan, melindungi privasi pengguna dari pengawasan massal atau peretas. Namun, ini menimbulkan tantangan hukum ("Going Dark") di mana penegak hukum kesulitan mendapatkan bukti digital dari percakapan kriminal atau teroris karena penyedia layanan pun tidak bisa mendekripsi pesan tersebut.  
---

## 8. Kesimpulan
Berdasarkan analisis yang dilakukan, penerapan SSL/TLS pada e-commerce dan email adalah standar wajib untuk menjamin keamanan transaksi dan data pengguna. HTTPS mencegah pencurian data melalui enkripsi dan memverifikasi identitas situs melalui sertifikat digital. Namun, kekuatan enkripsi ini memunculkan dilema etika baru antara hak privasi individu dan kebutuhan pengawasan untuk keamanan organisasi atau negara.  

---

## 9. Daftar Pustaka


---

## 10. Commit Log

```
commit abc12345
Author: Vera Indryawanti <indryawantivera@gmail.com>
Date:   2025-09-20

    week12-Aplikasi TLS & E-commerce
```
