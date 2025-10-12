# Laporan Praktikum Kriptografi
Minggu ke-: 2 
Topik: Cryptosystem (Komponen, Enkripsi & Dekripsi, Simetris & Asimetris)  
Nama: Vera Indryawanti  
NIM: 230202791  
Kelas: 5IKRB  

---

## 1. Tujuan
- Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
- Menggambarkan proses enkripsi dan dekripsi sederhana.
- Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).

---

## 2. Dasar Teori
Sebuah kriptosistem adalah serangkaian prosedur dan komponen yang digunakan untuk melakukan enkripsi dan dekripsi. Terdapat lima komponen utama: plaintext (pesan asli), ciphertext (pesan tersandi), algoritma enkripsi, algoritma dekripsi, dan kunci. Algoritma adalah metode matematis yang digunakan untuk transformasi, sedangkan kunci adalah parameter rahasia yang mengontrol output dari algoritma. Keamanan sebuah kriptosistem modern bergantung sepenuhnya pada kerahasiaan kuncinya, bukan algoritmanya.

Kriptosistem secara umum terbagi menjadi dua kategori utama. Pertama, kriptografi simetris, di mana kunci yang sama digunakan untuk proses enkripsi dan dekripsi. Kategori kedua adalah kriptografi asimetris (atau kunci publik), yang menggunakan sepasang kunci: satu kunci publik untuk enkripsi dan satu kunci privat yang berbeda untuk dekripsi.

---

## 3. Alat dan Bahan
1. Python 3.11
2. Visual Studio Code
3. GitHub
4. Alat pembuatan diagram (Draw.io)

---

## 4. Langkah Percobaan
1. Membuat diagram/skema alur kerja kriptosistem dasar yang menggambarkan proses enkripsi dan dekripsi, lalu menyimpannya sebagai `screenshots/diagram_kriptosistem.png`.
2. Membuat file Python bernama `simple_crypto.py` di dalam folder `praktikum/week2-cryptosystem/src/`.
3. Menyalin dan menulis kode program dari modul praktikum untuk mengimplementasikan Caesar Cipher sederhana.
4. Mengubah variabel `message` di dalam program menjadi <nim><nama> (<2310112345><Vera Indryawanti>).
5. Menjalankan program dari terminal dengan perintah `python src/simple_crypto.py`.
6. Mengambil screenshot hasil eksekusi program dan menyimpannya sebagai `screenshots/hasil_eksekusi.png`.
7. Menyusun laporan `laporan.md` yang berisi semua komponen, dari tujuan hingga jawaban diskusi.
8. Melakukan commit dan push ke repositori GitHub dengan pesan `week2-cryptosystem`.

---

## 5. Source Code
```python
def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        # Kondisi untuk mengenkripsi huruf
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        # Kondisi baru untuk mengenkripsi angka
        elif char.isdigit():
            new_digit = (int(char) + key) % 10
            result += str(new_digit)
        # Karakter lain (seperti <, >, spasi) tidak diubah
        else:
            result += char
    return result

def decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        # Kondisi untuk mendekripsi huruf
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        # Kondisi baru untuk mendekripsi angka
        elif char.isdigit():
            new_digit = (int(char) - key) % 10
            result += str(new_digit)
        # Karakter lain tidak diubah
        else:
            result += char
    return result

if __name__ == "__main__":
    message = "<230202791><Vera Indryawanti>"
    key = 5

    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)
```

---

## 6. Hasil dan Pembahasan 
Percobaan pada minggu ini berhasil dilakukan. Diagram kriptosistem berhasil dibuat untuk memvisualisasikan alur kerja enkripsi dan dekripsi. Program simulasi Caesar Cipher juga berhasil diimplementasikan dan dijalankan.

Program mengenkripsi pesan 2310112345 Vera Indryawanti dengan kunci 5. Karakter angka dan alfabet bergeser 5 posisi. Proses dekripsi berhasil mengembalikan ciphertext menjadi plaintext semula, yang menunjukkan bahwa fungsi enkripsi dan dekripsi bekerja sesuai ekspektasi.

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](/praktikum/week2-cryptosystem/Screenshot/hasil_eksekusi.png)
![Diagram Kriptosistem](/praktikum/week2-cryptosystem/Screenshot/diagram_kriptosistem.png)

---

## 7. Jawaban Pertanyaan
1. Sebutkan komponen utama dalam sebuah kriptosistem.
Komponen utamanya ada lima:
- Plaintext: Pesan asli yang dapat dibaca.
- Ciphertext: Pesan tersandi hasil enkripsi.
- Algoritma Enkripsi: Aturan untuk mengubah plaintext menjadi ciphertext.
- Algoritma Dekripsi: Aturan untuk mengubah ciphertext kembali menjadi plaintext.
- Kunci: Parameter yang digunakan oleh algoritma untuk proses enkripsi dan dekripsi.

2. Apa kelebihan dan kelemahan sistem simetris dibandingkan asimetris?
Sistem Simetris:
- Kelebihan: Proses enkripsi/dekripsi sangat cepat dan efisien secara komputasi. Cocok untuk mengenkripsi data dalam jumlah besar.
- Kelemahan: Masalah distribusi kunci. Kunci rahasia harus dibagikan antara pengirim dan penerima melalui saluran yang aman terlebih dahulu.
Sistem Asimetris:
- Kelebihan: Memecahkan masalah distribusi kunci. Kunci publik dapat dibagikan secara bebas tanpa memerlukan saluran aman.
- Kelemahan: Prosesnya jauh lebih lambat dan membutuhkan sumber daya komputasi yang lebih besar dibandingkan sistem simetris.

3. Mengapa distribusi kunci menjadi masalah utama dalam kriptografi simetris?
Karena kunci yang sama digunakan untuk enkripsi dan dekripsi, maka kunci tersebut harus dirahasiakan dan hanya diketahui oleh pihak-pihak yang berkomunikasi. Masalahnya adalah bagaimana cara mengirimkan kunci rahasia ini kepada penerima secara aman? Jika kunci dikirim melalui saluran yang tidak aman, pihak ketiga dapat menyadap kunci tersebut dan membahayakan seluruh komunikasi selanjutnya. Ini menciptakan dilema "ayam dan telur": untuk berkomunikasi secara aman, kita butuh kunci aman, tetapi untuk mengirim kunci aman, kita butuh saluran komunikasi yang aman.
---

## 8. Kesimpulan
Praktikum ini berhasil menunjukkan komponen-komponen dasar dari sebuah kriptosistem serta alur kerja enkripsi dan dekripsi melalui implementasi Caesar Cipher. Perbedaan fundamental antara kriptografi simetris dan asimetris, terutama terkait kecepatan dan manajemen kunci, juga telah dipahami dengan baik. Sistem simetris unggul dalam kecepatan, namun memiliki tantangan besar dalam distribusi kunci yang aman.

---

## 9. Daftar Pustaka


---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Vera Indryawanti <indryawantivera@gmail.com>
Date:   2025-10-12

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
