# Nama file: src/secret_sharing.py
# Pembuat: Vera Indryawanti
# Topik: Implementasi Shamir's Secret Sharing

from secretsharing import SecretSharer

def main():
    print("=" * 60)
    print("SIMULASI SHAMIR'S SECRET SHARING (SSS)")
    print("=" * 60)

    # ---------------------------------------------------------
    # 1. KONFIGURASI DAN INPUT
    # ---------------------------------------------------------
    # Rahasia yang akan diamankan
    my_secret = "KriptografiUPB2025"
    
    # n = Total partisipan yang menerima potongan rahasia
    n = 5 
    
    # k = Threshold (Jumlah minimal bagian untuk memulihkan rahasia)
    k = 3 

    print(f"[INPUT] Rahasia Asli  : {my_secret}")
    print(f"[SETUP] Total Share (n): {n}")
    print(f"[SETUP] Threshold (k)  : {k}")
    print("-" * 60)

    # ---------------------------------------------------------
    # 2. PROSES PEMBAGIAN (SPLITTING)
    # ---------------------------------------------------------
    # Format share biasanya: "urutan-hexstring"
    shares = SecretSharer.split_secret(my_secret, k, n)

    print("[PROSES] Membagi rahasia menjadi kepingan (shares)...")
    for i, share in enumerate(shares):
        print(f"  > Share ke-{i+1}: {share}")
    
    print("-" * 60)

    # ---------------------------------------------------------
    # 3. SKENARIO SUKSES (Rekonstruksi dengan Jumlah Share >= k)
    # ---------------------------------------------------------
    print(f"[SKENARIO 1] Mencoba memulihkan dengan {k} share (CUKUP)")
    
    # Mengambil k bagian pertama (misal: share 1, 2, dan 3)
    shares_to_recover = shares[0:k]
    print(f"  > Share yang digunakan: {shares_to_recover}")
    
    recovered_secret = SecretSharer.recover_secret(shares_to_recover)
    print(f"  > Hasil Rekonstruksi: {recovered_secret}")
    
    if recovered_secret == my_secret:
        print("  >> STATUS: BERHASIL MEMULIHKAN RAHASIA! ✅")
    else:
        print("  >> STATUS: GAGAL! ❌")

    print("-" * 60)

    # ---------------------------------------------------------
    # 4. SKENARIO GAGAL (Rekonstruksi dengan Jumlah Share < k)
    # ---------------------------------------------------------
    # Ini penting untuk membuktikan keamanan algoritma
    k_minus_1 = k - 1
    print(f"[SKENARIO 2] Mencoba memulihkan dengan {k_minus_1} share (TIDAK CUKUP)")
    
    # Mengambil kurang dari k bagian
    insufficient_shares = shares[0:k_minus_1]
    print(f"  > Share yang digunakan: {insufficient_shares}")
    
    # Algoritma akan mencoba merekonstruksi, tetapi hasilnya akan salah/tidak terbaca
    try:
        failed_recovery = SecretSharer.recover_secret(insufficient_shares)
        # Seringkali library akan tetap menghasilkan output string, tapi isinya sampah
        print(f"  > Hasil Rekonstruksi: {failed_recovery}")
        
        if failed_recovery != my_secret:
            print("  >> STATUS: RAHASIA TIDAK TERBUKA (AMAN) 🔒")
    except Exception as e:
        print(f"  >> ERROR: {e}")

    print("=" * 60)

if __name__ == "__main__":
    main()