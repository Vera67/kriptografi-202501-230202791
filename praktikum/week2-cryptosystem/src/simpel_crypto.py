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