def caesar_encrypt(plaintext, shift):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) + shift - shift_base) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# Example usage
plaintext = "Hello, World!"
shift = 3
ciphertext = caesar_encrypt(plaintext, shift)
print(f"Encrypted: {ciphertext}")
decrypted = caesar_decrypt(ciphertext, shift)
print(f"Decrypted: {decrypted}")
