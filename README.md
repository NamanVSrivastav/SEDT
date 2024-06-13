# SEDT
Simple Encryption/Decryption Tool
# Basic Encryption Tool
this encryption tool project:
## Developed a User-Friendly Encryption Tool:
Designed and implemented a GUI application using Python's Tkinter library, providing users with a simple interface to encrypt and decrypt messages using Caesar Cipher and AES algorithms.
## Implemented Secure Encryption Algorithms:
Successfully coded and integrated both Caesar Cipher and AES encryption methods, enhancing understanding of cryptographic principles and secure data handling.
## Ensured Robust Functionality and Usability:
Conducted thorough testing and validation to ensure reliable performance, effectively converting plaintext to ciphertext and vice versa, while maintaining data integrity and security.
These points emphasize your technical skills, project development experience, and your ability to create practical, user-oriented software solutions.

## Overview

This project is a user-friendly encryption tool implemented in Python. It allows users to encrypt and decrypt messages using two different algorithms: Caesar Cipher and AES (Advanced Encryption Standard). The tool includes a graphical user interface (GUI) built with Tkinter for ease of use.

## Features

- **Caesar Cipher:** A simple substitution cipher where each letter in the plaintext is shifted by a fixed number of positions.
- **AES Encryption:** A more complex and secure encryption algorithm using the PyCryptodome library.
- **User-Friendly GUI:** A Tkinter-based interface that allows users to easily input text, choose encryption methods, and view results.

## Requirements

- Python 3.x
- `pycryptodome` library
- `tkinter` (usually included with Python installations)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/basic-encryption-tool.git
   cd basic-encryption-tool
2.install the basic library 
  pip install pycryptodome
## Usage
1.Run the encryption tool:
  python encryption_tool.py
2.Use the GUI to:
   Select the encryption method (Caesar Cipher or AES).
   Enter the text to be encrypted or decrypted.
   For Caesar Cipher, provide the shift value.
   For AES, provide a key (16, 24, or 32 bytes).
   Click "Encrypt" or "Decrypt" to see the result.
## Code Overview
## Caesar Cipher Functions
   caesar_encrypt(plaintext, shift): Encrypts the plaintext using the Caesar Cipher method.
   caesar_decrypt(ciphertext, shift): Decrypts the ciphertext using the Caesar Cipher method.
## AES Functions
   aes_encrypt(plaintext, key): Encrypts the plaintext using AES encryption.
   aes_decrypt(ciphertext, key): Decrypts the ciphertext using AES decryption.
## GUI Implementation
   EncryptionApp: A class that creates the Tkinter-based GUI for the encryption tool. It handles user inputs, displays results, and integrates the encryption and decryption functions.
## Closing Remarks

This Basic Encryption Tool project serves as an educational and practical application of fundamental cryptographic principles. By implementing both the Caesar Cipher and AES algorithms, and integrating them into an intuitive Tkinter-based GUI, the project provides a comprehensive learning experience. Whether you are new to cybersecurity or looking to deepen your understanding, this tool offers a valuable hands-on approach to exploring encryption and decryption processes. We welcome contributions and feedback to enhance and expand this project further.


