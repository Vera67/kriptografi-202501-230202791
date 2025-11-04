# Laporan Praktikum Kriptografi
Minggu ke-: 5  
Topik: Cipher Klasik (Caesar, Vigenère, Transposisi)  
Nama: Vera Indryawanti  
NIM: 230202791  
Kelas: 5IKRB  

---

## 1. Tujuan
1. Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.  
2. Menerapkan algoritma Vigenère Cipher dengan variasi kunci.  
3. Mengimplementasikan algoritma transposisi sederhana.  
4. Menjelaskan kelemahan algoritma kriptografi klasik.

---

## 2. Dasar Teori
Kriptografi klasik merujuk pada metode enkripsi (cipher) yang digunakan sebelum era komputer digital. Algoritma ini umumnya beroperasi pada level huruf (alfabet) dan dapat dibagi menjadi dua kategori utama: cipher substitusi dan cipher transposisi. Cipher substitusi menggantikan satu unit plaintext (misalnya, satu huruf) dengan unit lain, sedangkan cipher transposisi mengacak urutan huruf dalam plaintext tanpa mengubah huruf itu sendiri.Caesar Cipher adalah salah satu contoh cipher substitusi monoalfabetik yang paling sederhana. Ia bekerja dengan menggeser setiap huruf dalam plaintext sejauh $k$ posisi dalam alfabet. Proses ini dapat direpresentasikan secara matematis menggunakan aritmetika modular: $C = (P + k) \mod 26$ untuk enkripsi, dan $P = (C - k) \mod 26$ untuk dekripsi, di mana $k$ adalah kunci (jumlah pergeseran).Vigenère Cipher adalah pengembangan dari Caesar Cipher dan merupakan contoh cipher substitusi polialfabetik. Alih-alih menggunakan satu kunci pergeseran tetap, Vigenère menggunakan kata kunci (misalnya, "KEY"). Setiap huruf dalam kata kunci menentukan pergeseran yang berbeda, yang diulang secara periodik. Jika plaintext adalah "KRIPTOGRAFI" dan kunci "KEY", maka 'K' dienkripsi dengan 'K' (shift 10), 'R' dengan 'E' (shift 4), 'I' dengan 'Y' (shift 24), 'P' dengan 'K' (shift 10 lagi), dan seterusnya. Ini membuatnya jauh lebih tahan terhadap analisis frekuensi sederhana dibandingkan Caesar Cipher.

---

## 3. Alat dan Bahan
- Python   
- Visual Studio Code   
- Git dan akun GitHub   

---

## 4. Langkah Percobaan
1. Membuat struktur folder proyek sesuai panduan:  
`praktikum/week5-cipher-klasik/`  
`├─ src/`  
`├─ screenshots/`  
`└─ laporan.md`    
2. Membuat file `src/caesar.py` dan mengimplementasikan fungsi `caesar_encrypt` dan `caesar_decrypt` sesuai kode pada "Langkah 1" modul.  
3. Membuat file `src/vigenere.py` dan mengimplementasikan fungsi `vigenere_encrypt` dan `vigenere_decrypt` sesuai kode pada "Langkah 2" modul.  
4. Membuat file `src/transpose.py` dan mengimplementasikan fungsi `transpose_encrypt` dan `transpose_decrypt` sesuai kode pada "Langkah 3" modul.  
5. Menjalankan ketiga skrip Python tersebut secara terpisah untuk menguji fungsionalitas enkripsi dan dekripsi.  
Bash  
`python src/caesar.py`  
`python src/vigenere.py`  
`python src/transpose.py`    
6. Mengambil screenshot dari setiap hasil eksekusi terminal dan menyimpannya ke dalam folder `screenshots/`.  
7. Mengisi `laporan.md` dengan merangkum teori, menyalin source code, melampirkan hasil, dan menjawab pertanyaan diskusi  
8. Melakukan commit dan push ke repositori Git dengan pesan commit yang telah ditentukan.

---

## 5. Source Code
```python
# Implementasi Caesar Cipher
def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)  

# Implementasi Vigenère Cipher
def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)  

# Implementasi Transposisi Sederhana
def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```
---

## 6. Hasil dan Pembahasan
Hasil eksekusi program :

![Hasil caesar](/praktikum/week5-cipher-klasik/screenshots/hasil_caesar.png)
![Hasil vigenere](/praktikum/week5-cipher-klasik/screenshots/hasil_vigenere.png)
![Hasil transpose](/praktikum/week5-cipher-klasik/screenshots/hasil_transpose.png)

---

## 7. Jawaban Pertanyaan
1. Apa kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher?  
- Kelemahan Caesar Cipher: Kelemahan utamanya adalah ruang kunci yang sangat kecil (hanya ada 25 kemungkinan kunci pergeseran yang valid). Hal ini membuatnya sangat rentan terhadap serangan brute force, di mana penyerang dapat mencoba semua 25 kunci dalam waktu singkat. Selain itu, ia mempertahankan frekuensi statistik plaintext, sehingga mudah diserang dengan analisis frekuensi.  
- Kelemahan Vigenère Cipher: Meskipun jauh lebih kuat dari Caesar, kelemahan utamanya adalah sifat periodik dari kuncinya. Jika penyerang dapat menebak panjang kuncinya (misalnya, melalui Analisis Kasiski atau Indeks Koinsidensi), mereka dapat memecah ciphertext menjadi beberapa bagian, di mana setiap bagian pada dasarnya adalah Caesar Cipher yang dapat diserang secara individual dengan analisis frekuensi.

2. Mengapa cipher klasik mudah diserang dengan analisis frekuensi?  
Cipher klasik, terutama cipher substitusi monoalfabetik seperti Caesar, mudah diserang dengan analisis frekuensi karena mereka gagal menyembunyikan properti statistik dari bahasa plaintext. Dalam bahasa Inggris (atau Indonesia), huruf tertentu (seperti E, T, A, I, N) muncul jauh lebih sering daripada huruf lain (J, Q, Z, X). Cipher substitusi monoalfabetik hanya memetakan satu huruf ke huruf lain secara konsisten (misalnya, E selalu menjadi H). Penyerang dapat menghitung frekuensi huruf dalam ciphertext dan memetakannya kembali ke frekuensi bahasa aslinya untuk menebak kunci atau plaintext.

3. Bandingkan kelebihan dan kelemahan cipher substitusi vs transposisi.  
Perbandingan antara cipher substitusi dan transposisi terletak pada cara mereka mengolah plaintext:  
- Cipher Substitusi memiliki kelebihan dalam menciptakan konfusi (confusion). Metode ini mengganti unit plaintext (huruf) dengan unit lain, sehingga hubungan langsung antara plaintext dan ciphertext menjadi kabur dan huruf-hurufnya diubah menjadi sesuatu yang berbeda. Namun, kelemahannya (terutama untuk substitusi monoalfabetik) adalah ia mempertahankan statistik bahasa asli. Pola frekuensi huruf tetap ada, sehingga rentan terhadap analisis frekuensi.  
- Cipher Transposisi memiliki kelebihan dalam menciptakan difusi (diffusion). Metode ini menyebarkan statistik plaintext ke area yang lebih luas di ciphertext dengan cara mengacak urutan huruf, bukan mengubahnya. Ini efektif merusak pola kata lokal (misalnya, "RAHASIA" bisa menjadi "R...A...H..."). Kelemahannya adalah ia tidak mengubah frekuensi huruf sama sekali; frekuensi huruf di ciphertext identik dengan di plaintext. Hal ini membuatnya rentan terhadap serangan anagramming (penyusunan ulang huruf) jika metode transposisinya diketahui.
---

## 8. Kesimpulan
Praktikum ini berhasil mengimplementasikan tiga algoritma kriptografi klasik: Caesar Cipher, Vigenère Cipher, dan Transposition Cipher. Melalui implementasi, dapat dipahami perbedaan fundamental antara cipher substitusi (mengganti huruf) dan cipher transposisi (mengacak urutan). Meskipun Vigenère (polialfabetik) lebih aman daripada Caesar (monoalfabetik), semua cipher klasik terbukti memiliki kelemahan inheren terhadap analisis statistik (seperti analisis frekuensi atau Kasiski) dan tidak lagi dianggap aman untuk komunikasi modern.

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

    week5-cCipher Klasik (Caesar, Vigenère, Transposisi) )
```
