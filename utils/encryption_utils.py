# utils/encryption_utils.py
from cryptography.fernet import Fernet

def generate_key():
    """Generates a unique encryption key and returns it."""
    key = Fernet.generate_key()
    print("Store this key securely:", key.decode())
    return key.decode()

def encrypt_value(value, key):
    """Encrypts a value using the provided key."""
    fernet = Fernet(key.encode())
    encrypted_value = fernet.encrypt(value.encode()).decode()
    return encrypted_value

def decrypt_value(encrypted_value, key):
    """Decrypts a value using the provided key."""
    fernet = Fernet(key.encode())
    decrypted_value = fernet.decrypt(encrypted_value.encode()).decode()
    return decrypted_value
