from Crypto.Cipher import AES
from hashlib import sha256

def decrypt_file(file_path):

    password = input("Enter Password: ")
    key = sha256(password.encode()).digest()

    with open(file_path, "rb") as file:
        nonce = file.read(16)
        tag = file.read(16)
        ciphertext = file.read()

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    data = cipher.decrypt_and_verify(ciphertext, tag)

    output_file = file_path.replace(".enc", "")

    with open(output_file, "wb") as file:
        file.write(data)

    print("File Decrypted Successfully")