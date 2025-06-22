import hashlib
from Crypto.Util.Padding import pad, unpad

def derive_key(password: str, key_length: int = 32) -> bytes:
    """
    Derives a key from the given password using SHA-256 hashing.
    AES-256 requires a 32-byte key.
    """
    return hashlib.sha256(password.encode()).digest()[:key_length]

def pad(data, block_size=16):
    padding_len = block_size - len(data) % block_size
    padding = bytes([padding_len] * padding_len)
    return data + padding

def unpad(data):
    padding_len = data[-1]
    if padding_len > 16:
        raise ValueError("Invalid padding")
    return data[:-padding_len]


