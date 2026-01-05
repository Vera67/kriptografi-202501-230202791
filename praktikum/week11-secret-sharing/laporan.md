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


```python
import random
from typing import List, Tuple

# Fungsi untuk menghitung Modular Inverse (penting untuk pembagian dalam modulo)
def inverse(a, p):
    return pow(a, p - 2, p)

# 1. Implementasi Pembagian Rahasia (Split)
def split_secret(secret: int, k: int, n: int, p: int) -> List[Tuple[int, int]]:
    """
    secret: rahasia dalam angka
    k: threshold (minimal share)
    n: total shares yang dibuat
    p: bilangan prima (harus lebih besar dari secret dan n)
    """
    if k > n:
        raise ValueError("Threshold tidak boleh lebih besar dari total n")
    
    # Membuat koefisien polinomial secara acak: f(x) = secret + a1*x + a2*x^2 + ...
    # a0 adalah secret itu sendiri
    coefficients = [secret] + [random.randint(0, p - 1) for _ in range(k - 1)]
    
    def f(x):
        result = 0
        for i, coeff in enumerate(coefficients):
            result = (result + coeff * pow(x, i, p)) % p
        return result
    
    # Membuat n buah koordinat (x, f(x)) sebagai shares
    return [(i, f(i)) for i in range(1, n + 1)]

# 2. Implementasi Rekonstruksi Rahasia (Recover menggunakan Lagrange Interpolation)
def recover_secret(shares: List[Tuple[int, int]], p: int) -> int:
    """
    shares: daftar koordinat (x, y)
    p: bilangan prima yang sama saat split
    """
    secret = 0
    k = len(shares)
    
    for i in range(k):
        xi, yi = shares[i]
        num = 1
        den = 1
        for j in range(k):
            if i == j:
                continue
            xj, yj = shares[j]
            # Rumus Lagrange L_i(0) = PROD( -xj / (xi - xj) )
            num = (num * -xj) % p
            den = (den * (xi - xj)) % p
        
        # S_i = yi * L_i(0)
        term = (yi * num * inverse(den, p)) % p
        secret = (secret + term) % p
        
    return (secret + p) % p

# --- Main Program ---
if __name__ == "__main__":
    # Parameter: Bilangan prima besar (Mersenne Prime 2^13 - 1 sebagai contoh sederhana)
    P = 2**31 - 1 
    SECRET = 20251117  # Rahasia berupa angka (Contoh: NIM atau PIN)
    K = 3 # Minimal 3 orang
    N = 5 # Dibagi ke 5 orang

    print(f"Rahasia Asli: {SECRET}")
    
    # Langkah 1: Splitting
    shares = split_secret(SECRET, K, N, P)
    print("\nShares yang dihasilkan:")
    for s in shares:
        print(f"Partisipan {s[0]}: {s[1]}")

    # Langkah 2: Rekonstruksi (Gunakan 3 shares acak)
    subset_shares = shares[:3] 
    recovered = recover_secret(subset_shares, P)
    
    print("\n--- Hasil Uji ---")
    print(f"Menggunakan {len(subset_shares)} shares.")
    print(f"Rahasia yang dipulihkan: {recovered}")
    
    if recovered == SECRET:
        print("Status: BERHASIL (Rahasia Cocok)")
    else:
        print("Status: GAGAL")
```


---

## 6. Hasil dan Pembahasan
 
Hasil eksekusi program :

![Hasil Eksekusi](/kriptografi-202501-230202791/praktikum/week11-secret-sharing/screenshots/hasil.png)


---

## 7. Jawaban Pertanyaan
1. Apa keuntungan utama Shamir Secret Sharing dibanding membagikan salinan kunci secara langsung?  
- Keamanan Terdistribusi: Jika kunci dibagikan secara langsung (dikopi), pencurian dari satu pihak saja sudah cukup untuk membocorkan rahasia. Dengan SSS, peretas harus meretas minimal k pihak untuk mendapatkan rahasia.  
- Reliabilitas: Jika satu pemegang share kehilangan kuncinya atau berhalangan, rahasia masih bisa dipulihkan oleh pemegang share lainnya selama jumlah totalnya > k.  
2. Apa peran threshold (k) dalam keamanan secret sharing?  
- Threshold (k) adalah penentu tingkat kesulitan untuk merekonstruksi rahasia. Semakin tinggi nilai k (mendekati n), semakin aman rahasia tersebut karena membutuhkan persetujuan lebih banyak pihak. Namun, jika k terlalu tinggi, risiko kehilangan akses (availability risk) juga meningkat jika banyak pemegang share yang kehilangan bagiannya.  
3. Berikan satu contoh skenario nyata di mana SSS sangat bermanfaat.  
- Manajemen Private Key Dompet Kripto (Cold Storage): Sebuah perusahaan exchange aset digital dapat membagi private key dompet utama mereka menjadi 5 bagian, dan memberikannya kepada 5 eksekutif berbeda. Untuk melakukan transaksi besar, minimal 3 dari 5 eksekutif harus hadir dan menggabungkan bagian mereka. Ini mencegah satu orang jahat (atau satu perangkat yang diretas) mencuri seluruh dana.   

---

## 8. Kesimpulan
Berdasarkan praktikum ini, dapat disimpulkan bahwa Shamir's Secret Sharing merupakan metode yang efektif untuk mendistribusikan rahasia tanpa titik kegagalan tunggal (single point of failure). Skema ini menyeimbangkan antara keamanan (melalui threshold) dan ketersediaan data (redundansi shares). Simulasi menggunakan Python menunjukkan bahwa rahasia dapat dipulihkan secara utuh hanya jika jumlah shares yang digabungkan memenuhi syarat minimal k.

---

## 9. Daftar Pustaka

---

## 10. Commit Log

```
commit abc12345
Author: Vera Indryawanti <indryawantivera@gmail.com>
Date:   2025-09-20

    week11-Secret Sharing (Shamir’s Secret Sharing)
```
