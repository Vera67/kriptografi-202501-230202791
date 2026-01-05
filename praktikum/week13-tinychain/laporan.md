# Laporan Praktikum Kriptografi
Minggu ke-: 13  
Topik: TinyChain – Proof of Work (PoW)  
Nama: Vera Indryawanti    
NIM: 230202791    
Kelas: 5IKRB    

---

## 1. Tujuan
1. Menjelaskan peran hash function dalam struktur data blockchain.  
2. Melakukan simulasi sederhana mekanisme konsensus Proof of Work (PoW).   
3. Menganalisis aspek keamanan pada cryptocurrency yang berbasis kriptografi.  

---

## 2. Dasar Teori
Blockchain dan Fungsi Hash Blockchain adalah struktur data yang terdiri dari serangkaian blok yang saling terhubung secara kriptografis. Inti dari koneksi ini adalah penggunaan fungsi hash (seperti SHA-256). Setiap blok menyimpan hash dari blok sebelumnya (previous_hash). Sifat fungsi hash yang deterministik namun tidak dapat dibalik (one-way function) dan sensitif terhadap perubahan (avalanche effect) menjamin integritas data. Jika satu bit data dalam blok diubah, hash blok tersebut akan berubah total, yang mengakibatkan ketidakcocokan pada blok-blok berikutnya, sehingga rantai menjadi tidak valid.

Proof of Work (PoW) Proof of Work adalah mekanisme konsensus yang digunakan untuk mencegah penyalahgunaan sistem (seperti spam atau serangan Sybil) dan mengamankan jaringan. Dalam PoW, "penambang" (miner) harus memecahkan teka-teki matematika yang sulit—dalam hal ini, mencari nilai nonce (number used once). Tujuannya adalah agar hash dari blok yang dihasilkan memenuhi kriteria kesulitan tertentu (misalnya, hash harus diawali dengan empat angka nol). Proses ini membutuhkan daya komputasi (usaha), sehingga memanipulasi blockchain menjadi sangat mahal dan sulit dilakukan.  

---

## 3. Alat dan Bahan
- Python  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan 

---

## 4. Langkah Percobaan
1. Membuat struktur folder proyek: `praktikum/week13-tinychain/` yang berisi folder `src/`, `screenshots/`, dan file `laporan.md`.  
2. Membuat file program utama bernama `tinychain.py` di dalam folder `src/`.  
3. Mengimplementasikan Class Block yang mencakup inisialisasi blok, penghitungan hash menggunakan SHA-256, dan fungsi `mine_block` untuk simulasi Proof of Work.  
4. Mengimplementasikan Class Blockchain untuk mengelola rantai blok, membuat Genesis Block, dan menambahkan blok baru.  
5. Menguji program dengan menambahkan beberapa transaksi dan melihat proses mining (pencarian nonce) pada terminal.  
6. Mendokumentasikan hasil eksekusi program ke dalam folder `screenshots`/.  

---

## 5. Source Code


```python
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Menggabungkan seluruh atribut blok menjadi string tunggal untuk di-hash
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        # Loop terus berjalan sampai hash yang dihasilkan diawali dengan jumlah '0' sesuai difficulty
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4 # Tingkat kesulitan mining

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        # Proses mining terjadi di sini (PoW)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# Uji coba blockchain
if __name__ == "__main__":
    my_chain = Blockchain()
    
    print("Mining block 1...")
    my_chain.add_block(Block(1, "", "Transaksi A -> B: 10 Coin"))
    
    print("Mining block 2...")
    my_chain.add_block(Block(2, "", "Transaksi B -> C: 5 Coin"))
    
    # Verifikasi data blok terakhir
    print("\nDetail Blok Terakhir:")
    print(f"Index: {my_chain.chain[-1].index}")
    print(f"Hash: {my_chain.chain[-1].hash}")
    print(f"Prev Hash: {my_chain.chain[-1].previous_hash}")
    print(f"Nonce: {my_chain.chain[-1].nonce}")
```


---

## 6. Hasil dan Pembahasan   

Hasil eksekusi program :

![Hasil Eksekusi](/kriptografi-202501-230202791/praktikum/week13-tinychain/screenshots/hasil.png)



---

## 7. Jawaban Pertanyaan
1. Mengapa fungsi hash sangat penting dalam blockchain?   
Fungsi hash bertindak sebagai "sidik jari digital" yang unik untuk setiap blok. Ia memiliki dua peran vital:  
- Integritas Data: Perubahan sekecil apapun pada data transaksi akan mengubah hash blok secara drastis.  
- Chaining (Pengaitan): Hash blok saat ini bergantung pada hash blok sebelumnya. Ini menciptakan rantai di mana jika seseorang ingin memalsukan blok di masa lalu, ia harus menghitung ulang hash untuk semua blok setelahnya, yang secara komputasi sangat sulit.  

2. Bagaimana Proof of Work mencegah double spending?   
Double spending adalah risiko mata uang digital digunakan dua kali. PoW mencegah ini dengan membuat penambahan blok baru menjadi "mahal" (butuh listrik dan waktu). Untuk melakukan double spending, penyerang harus membatalkan transaksi yang sudah dikonfirmasi dengan cara membuat rantai blok alternatif yang lebih panjang dari rantai asli. Karena setiap blok butuh work (usaha komputasi) untuk dibuat, penyerang harus memiliki kecepatan komputasi (hashrate) lebih dari 50% dari total jaringan (51% attack) untuk mengalahkan rantai yang valid, yang mana sangat sulit dan tidak ekonomis.    

3. Apa kelemahan dari PoW dalam hal efisiensi energi?   
Kelemahan utama PoW adalah konsumsi energi yang masif. Setiap penambang di seluruh dunia berlomba memecahkan teka-teki matematika yang sama secara terus-menerus. Hanya satu pemenang yang bloknya diterima, sementara usaha komputasi (dan listrik) yang dikeluarkan oleh penambang lain terbuang sia-sia. Hal ini menyebabkan jejak karbon yang tinggi pada cryptocurrency berbasis PoW seperti Bitcoin.  
---

## 8. Kesimpulan
Simulasi "TinyChain" menunjukkan prinsip dasar bagaimana blockchain bekerja mengamankan data. Hash function memastikan setiap blok terkait erat dengan blok sebelumnya, sementara Proof of Work (PoW) memberikan mekanisme keamanan melalui kesulitan komputasi (difficulty). Meskipun PoW sangat aman dan terdesentralisasi, mekanisme ini menuntut sumber daya komputasi yang besar.  

---

## 9. Daftar Pustaka


---

## 10. Commit Log

```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week13-TinyChain – Proof of Work (PoW)
```
