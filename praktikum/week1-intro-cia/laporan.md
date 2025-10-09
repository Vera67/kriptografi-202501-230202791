# Laporan Praktikum Kriptografi
Minggu ke-: 1  
Topik: Sejarah Kriptografi & Prinsip CIA  
Nama: Vera Indryawanti  
NIM: 230202791  
Kelas: 5IKRB 

---

## 1. Tujuan
- Menjelaskan sejarah dan evolusi kriptografi dari masa klasik hingga modern.
- Menyebutkan prinsip Confidentiality, Integrity, Availability (CIA) dengan benar.
- Menyimpulkan peran kriptografi dalam sistem keamanan informasi modern.
- Menyiapkan repositori GitHub sebagai media kerja praktikum.

---

## 2. Dasar Teori
Kriptografi adalah ilmu dan seni untuk menjaga keamanan pesan. Sejarahnya terbagi menjadi era klasik dan modern. Kriptografi klasik, seperti Caesar Cipher dan Vigenère Cipher, beroperasi pada level karakter (huruf) dan sering kali mengandalkan kerahasiaan metode penyandiannya. Seiring berkembangnya teknologi komputasi, kriptografi modern lahir dengan basis matematika yang kuat. Keamanannya tidak lagi bergantung pada kerahasiaan algoritma, melainkan pada kerahasiaan kunci, sebuah prinsip yang dikenal sebagai Prinsip Kerckhoffs. Algoritma modern seperti AES (simetris) dan RSA (asimetris) menjadi fondasi keamanan digital saat ini.

Dalam keamanan informasi, tiga pilar utama dikenal sebagai CIA Triad: Confidentiality (kerahasiaan data dari akses tidak sah), Integrity (keutuhan data dari perubahan tidak sah), dan Availability (ketersediaan data saat dibutuhkan oleh pengguna yang sah). Kriptografi memainkan peran vital dalam menegakkan prinsip-prinsip ini, terutama kerahasiaan dan integritas.

---

## 3. Alat dan Bahan
- Leptop/Komputer
- Visual Studio Code
- Akun GitHub yang aktif

---

## 4. Langkah Percobaan
- Melakukan fork. 
- Mengubah nama repositori hasil fork.
- Melakukan clone repositori yang sudah diubah namanya ke komputer lokal.
- Membuat struktur folder baru di dalam repositori lokal.
- Di dalam folder tersebut, dibuat file `laporan.md` dan sebuah folder `screenshots/`.
- Menulis ringkasan mengenai sejarah kriptografi dan prinsip CIA di dalam file `laporan.md`.
- Menjawab pertanyaan quiz yang diberikan di dalam file `laporan.md`.
- Mengambil screenshot sebagai bukti penyiapan repositori dan menyimpannya di folder `screenshots/`.
- Menambahkan (add), melakukan commit (commit), dan mengirim (push) perubahan ke repositori GitHub dengan pesan commit `week1-intro-cia`.

---

## 5. Source Code
Pada praktikum minggu ini tidak ada pembuatan atau modifikasi source code program. Kegiatan berfokus pada penyiapan lingkungan kerja dan penyusunan laporan.

---

## 6. Hasil dan Pembahasan
Praktikum ini berhasil dilaksanakan dengan penyiapan repositori GitHub sebagai lingkungan kerja dan penyusunan laporan awal. Repositori berhasil di-fork, di-clone, dan disesuaikan strukturnya. Laporan yang berisi ringkasan materi dan jawaban quiz berhasil dibuat sesuai panduan.

Berikut adalah bukti screenshot dari penyiapan repositori:
![repo setup](/praktikum/week1-intro-cia/Screenshot/repo_setup.png)
![initial commit](/praktikum/week1-intro-cia/Screenshot/initial_commit.png)

---

## 7. Jawaban Pertanyaan
1. Siapa tokoh yang dianggap sebagai bapak kriptografi modern?
Claude Shannon. Melalui karyanya "Communication Theory of Secrecy Systems" (1949), ia meletakkan dasar matematis yang menjadi fondasi kriptografi modern.

2. Sebutkan algoritma kunci publik yang populer digunakan saat ini.
RSA (Rivest-Shamir-Adleman) dan ECC (Elliptic Curve Cryptography).

3. Apa perbedaan utama antara kriptografi klasik dan kriptografi modern?
Perbedaan utamanya terletak pada basis operasi dan prinsip keamanan. Kriptografi klasik berbasis linguistik (memanipulasi huruf) dan sering mengandalkan kerahasiaan algoritma. Sebaliknya, kriptografi modern berbasis matematika (memanipulasi bit) dan keamanannya bergantung penuh pada kerahasiaan kunci, bukan algoritma.
---

## 8. Kesimpulan
Praktikum ini berhasil memberikan pemahaman dasar mengenai evolusi kriptografi dari era klasik hingga kontemporer serta pengenalan prinsip fundamental keamanan informasi (CIA Triad). Selain itu, lingkungan kerja praktikum menggunakan Git dan GitHub telah berhasil disiapkan untuk mendukung kegiatan praktikum selanjutnya.

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
