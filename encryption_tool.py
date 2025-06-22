from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os

class EncryptionTool:
    def __init__(self, password):
        self.key = SHA256.new(password.encode()).digest()

    def encrypt_file(self, input_file, output_file):
        cipher = AES.new(self.key, AES.MODE_CBC)
        with open(input_file, 'rb') as f:
            plaintext = f.read()
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
        with open(output_file, 'wb') as f:
            f.write(cipher.iv + ciphertext)

    def decrypt_file(self, input_file, output_file=None):
        with open(input_file, 'rb') as f:
            iv = f.read(16)
            ciphertext = f.read()
        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

        # Auto-generate output file with .dec extension if not given
        if output_file is None:
            output_file = input_file + '.dec'

        with open(output_file, 'wb') as f:
            f.write(plaintext)
        
        return output_file
