# crypto_lib.py
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# =========================
#      AES (Simétrico)
# =========================

def _pad(data):
    return data + (AES.block_size - len(data) % AES.block_size) * chr(AES.block_size - len(data) % AES.block_size)

def _unpad(data):
    return data[:-ord(data[-1])]

def cifrar_aes(texto):
    key = get_random_bytes(16)    # 128 bits
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cifrado = cipher.encrypt(_pad(texto).encode())

    return {
        "cifrado": base64.b64encode(cifrado).decode(),
        "key": base64.b64encode(key).decode(),
        "iv": base64.b64encode(iv).decode()
    }


# =========================
#      RSA (Asimétrico)
# =========================

def cifrar_rsa(texto):
    key_pair = RSA.generate(2048)
    public_key = key_pair.publickey()

    encryptor = PKCS1_OAEP.new(public_key)
    cifrado = encryptor.encrypt(texto.encode())

    return {
        "cifrado": base64.b64encode(cifrado).decode(),
        "public_key": public_key.export_key().decode(),
        "private_key": key_pair.export_key().decode()
    }


# =========================
#      SHA-256 (Hash)
# =========================

def hash_sha256(texto):
    hash_object = hashlib.sha256(texto.encode())
    return hash_object.hexdigest()
