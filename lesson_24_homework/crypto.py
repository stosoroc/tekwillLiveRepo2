import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def generate_key(password):
    salt = b'salt_'  # Salt poate fi orice valoare de 8 octeți.
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

def encrypt_file(file_name, key):
    with open(file_name, "rb") as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    print(encrypted_data)

    with open(file_name, "wb") as f:
        f.write(encrypted_data)

def decrypt_file(file_name, key):
    with open(file_name, "rb") as f:
        encrypted_data = f.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_name, "wb") as f:
        f.write(decrypted_data)

password = input("Enter password: ").encode()
key = generate_key(password)
print(key)
encrypt_file("apikey.json", key)
#decrypt_file("text.txt", key)
