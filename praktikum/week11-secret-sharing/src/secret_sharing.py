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