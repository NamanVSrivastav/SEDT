import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Caesar Cipher functions
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

# AES functions
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

# GUI
class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Encryption Tool")

        self.method_label = tk.Label(root, text="Select Method:")
        self.method_label.pack()

        self.method_var = tk.StringVar(value="Caesar")
        self.caesar_radio = tk.Radiobutton(root, text="Caesar Cipher", variable=self.method_var, value="Caesar")
        self.aes_radio = tk.Radiobutton(root, text="AES", variable=self.method_var, value="AES")
        self.caesar_radio.pack()
        self.aes_radio.pack()

        self.text_label = tk.Label(root, text="Enter Text:")
        self.text_label.pack()

        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.pack()

        self.shift_label = tk.Label(root, text="Enter Shift (Caesar Cipher):")
        self.shift_label.pack()

        self.shift_entry = tk.Entry(root, width=5)
        self.shift_entry.pack()

        self.key_label = tk.Label(root, text="Enter Key (AES):")
        self.key_label.pack()

        self.key_entry = tk.Entry(root, width=32)
        self.key_entry.pack()

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt)
        self.decrypt_button.pack()

        self.result_label = tk.Label(root, text="Result:")
        self.result_label.pack()

        self.result_text = tk.Text(root, height=5, width=50)
        self.result_text.pack()

    def encrypt(self):
        method = self.method_var.get()
        text = self.text_entry.get()
        if method == "Caesar":
            try:
                shift = int(self.shift_entry.get())
                result = caesar_encrypt(text, shift)
            except ValueError:
                messagebox.showerror("Error", "Shift must be an integer.")
                return
        elif method == "AES":
            key = self.key_entry.get().encode()
            if len(key) not in [16, 24, 32]:
                messagebox.showerror("Error", "Key must be 16, 24, or 32 bytes long.")
                return
            result = aes_encrypt(text, key)
            result = result.hex()  # Display as hex for readability
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

    def decrypt(self):
        method = self.method_var.get()
        text = self.text_entry.get()
        if method == "Caesar":
            try:
                shift = int(self.shift_entry.get())
                result = caesar_decrypt(text, shift)
            except ValueError:
                messagebox.showerror("Error", "Shift must be an integer.")
                return
        elif method == "AES":
            key = self.key_entry.get().encode()
            if len(key) not in [16, 24, 32]:
                messagebox.showerror("Error", "Key must be 16, 24, or 32 bytes long.")
                return
            try:
                ciphertext = bytes.fromhex(text)
                result = aes_decrypt(ciphertext, key)
            except ValueError:
                messagebox.showerror("Error", "Invalid ciphertext format.")
                return
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()
