from Crypto.Cipher import AES
from hashlib import sha256

def encrypt_file(file_path):

    password = input("Enter Password: ")
    key = sha256(password.encode()).digest()

    cipher = AES.new(key, AES.MODE_EAX)

    with open(file_path, "rb") as file:
        data = file.read()

    ciphertext, tag = cipher.encrypt_and_digest(data)

    encrypted_file = file_path + ".enc"

    with open(encrypted_file, "wb") as file:
        file.write(cipher.nonce)
        file.write(tag)
        file.write(ciphertext)

    print("File Encrypted Successfully")