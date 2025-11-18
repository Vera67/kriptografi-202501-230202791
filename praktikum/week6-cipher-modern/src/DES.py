from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Kunci harus 8 byte (64 bit)
key = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_ECB)

# Plaintext harus kelipatan 8 byte untuk ECB
plaintext = b"ABCDEFGH" 
ciphertext = cipher.encrypt(plaintext)
print("--- DES (ECB) ---")
print("Ciphertext:", ciphertext)

# Dekripsi
decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)
print("Decrypted (decoded):", decrypted.decode())
print("\n")