from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return cipher.iv + ct_bytes

def aes_decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    ct = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()

# Example usage
key = get_random_bytes(16)  # AES-128 bit key
plaintext = "Hello, World!"
ciphertext = aes_encrypt(plaintext, key)
print(f"Encrypted: {ciphertext}")
decrypted = aes_decrypt(ciphertext, key)
print(f"Decrypted: {decrypted}")
