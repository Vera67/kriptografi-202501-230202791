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