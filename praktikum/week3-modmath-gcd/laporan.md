# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)  
Nama: Vera Indryawanti  
NIM: 230202791  
Kelas: 5IKRB  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menyelesaikan operasi aritmetika modular.  
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).  
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.  

---

## 2. Dasar Teori
**Aritmetika Modular** adalah sistem aritmetika bilangan bulat di mana operasi dilakukan pada modulus $n$, sehingga hasilnya selalu berada dalam himpunan $\{0, 1, \dots, n-1\}$. Konsep ini esensial karena memungkinkan perhitungan tetap dalam ruang terbatas, yang merupakan fondasi matematis bagi banyak sistem kriptografi, terutama **eksponensiasi modular** $\left(a^x \bmod n\right)$ yang efisien.

**Greatest Common Divisor (GCD)** dari dua bilangan $a$ dan $b$ adalah bilangan bulat terbesar yang membagi keduanya. GCD dihitung secara efisien menggunakan **Algoritma Euclidean**. Perluasan algoritma ini, **Extended Euclidean Algorithm (EEA)**, digunakan untuk mencari **invers modular** $a^{-1} \bmod n$. Invers modular hanya ada jika $\text{gcd}(a, n) = 1$, yang merupakan syarat vital dalam proses dekripsi algoritma kunci publik seperti RSA.

**Logaritma Diskrit** mencari eksponen $x$ dalam persamaan $a^x \equiv b \pmod n$. Sementara $b$ mudah dihitung, mencari $x$ untuk modulus $n$ yang besar adalah masalah yang sulit secara komputasi (memiliki kompleksitas eksponensial), yang menjadi pilar keamanan bagi protokol seperti Diffie-Hellman.

---

## 3. Alat dan Bahan
- Python  
- Visual Studio Code  
- Git dan akun GitHub   

---

## 4. Langkah Percobaan
1.  Membuat struktur folder `praktikum/week3-modmath-gcd/src/` dan file `modular_math.py`.
2.  Mengimplementasikan fungsi Aritmetika Modular (`mod_add`, `mod_sub`, `mod_mul`, `mod_exp`).
3.  Mengimplementasikan **Algoritma Euclidean** untuk GCD (`gcd`).
4.  Mengimplementasikan **Extended Euclidean Algorithm** (`egcd`) dan fungsi **invers modular** (`modinv`).
5.  Mengimplementasikan simulasi **Logaritma Diskrit** sederhana (`discrete_log`).
6.  Menjalankan program (`python src/modular_math.py`) untuk menguji semua fungsi yang diimplementasikan.
7.  Merekam hasil eksekusi dalam folder `screenshots/`.

---

## 5. Source Code
```python
#Aritmetika Modular
def mod_add(a, b, n): return (a + b) % n
def mod_sub(a, b, n): return (a - b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(base, exp, n): return pow(base, exp, n)  # eksponensiasi modular

print("7 + 5 mod 12 =", mod_add(7, 5, 12))
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
print("7^128 mod 13 =", mod_exp(7, 128, 13))

#GCD & Algoritma Euclidean
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("gcd(54, 24) =", gcd(54, 24))

#Extended Euclidean Algorithm
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

print("Invers 3 mod 11 =", modinv(3, 11))  # hasil: 4

#Logaritma Diskrit (Discrete Log)
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))  # hasil: 4
```
---

## 6. Hasil dan Pembahasan
Hasil eksekusi program :

![Hasil Eksekusi](/praktikum/week3-modmath-gcd/screenshot/hasil.png)


---

## 7. Jawaban Pertanyaan
Pertanyaan 1: Apa peran aritmetika modular dalam kriptografi modern?Aritmetika modular adalah landasan matematis dari kriptografi modern. Peran utamanya adalah:Menciptakan Fungsi One-Way: Ia memungkinkan perhitungan ke satu arah (seperti eksponensiasi modular) dilakukan dengan mudah, tetapi sulit dibalikkan (seperti Logaritma Diskrit), yang menjadi dasar keamanan algoritma kunci publik (RSA, Diffie-Hellman).Membatasi Ruang Kerja: Operasi modular memastikan bahwa hasil perhitungan kriptografi tetap berada dalam domain bilangan bulat terhingga $\{0, \dots, n-1\}$, menjadikannya terkelola dan menghasilkan ciphertext dengan panjang yang terdefinisi.
Pertanyaan 2: Mengapa invers modular penting dalam algoritma kunci publik (misalnya RSA)?Invers modular (kunci privat $d$) sangat penting karena merupakan operasi pembatal (inverse operation) untuk kunci publik ($e$).Dalam RSA, dekripsi harus membatalkan efek enkripsi. Kunci privat $d$ dihitung sebagai invers perkalian modular dari kunci publik $e$ modulo $\phi(n)$.Jika $d$ tidak ada (yaitu, $\text{gcd}(e, \phi(n)) \neq 1$), maka pesan yang dienkripsi tidak akan pernah bisa didekripsi kembali ke pesan aslinya, sehingga sistem kriptografi tersebut gagal.
Pertanyaan 3: Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar?Tantangan utamanya adalah kompleksitas komputasi yang eksponensial.Mencari eksponen $x$ dalam $a^x \equiv b \pmod n$ memerlukan waktu yang sangat lama (intractable) jika modulus $n$ cukup besar (misalnya 2048-bit), bahkan dengan algoritma canggih seperti Number Field Sieve (NFS).Kesulitan komputasi inilah yang membentuk masalah Logaritma Diskrit yang sulit dan menjadi dasar keamanan banyak sistem kriptografi modern (Diffie-Hellman, ECC).

---

## 8. Kesimpulan
Praktikum ini berhasil mengimplementasikan operasi dasar number theory yang menjadi fondasi kriptografi: aritmetika modular, Algoritma Euclidean, Extended Euclidean Algorithm, dan simulasi Logaritma Diskrit. Kunci keberhasilan terletak pada pemahaman bahwa GCD dan invers modular sangat vital untuk memastikan reversibilitas (dekripsi) dalam skema kunci publik, sementara kesulitan Logaritma Diskrit menjamin keamanan sistem tersebut dari serangan brute force pada modulus besar.

---

## 9. Daftar Pustaka

---

## 10. Commit Log
```
commit abc12345
Author: Vera Indryawanti <indryawantivera@gmail.com>
Date:   2025-10-18

    week3-modmath-gcd
```
