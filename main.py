from encrypted import encrypt_file
from decrypted import decrypt_file

choice = input("1 Encrypt\n2 Decrypt\nChoose: ")

if choice == "1":

    file = input("Enter File Path: ")

    encrypt_file(file)

elif choice == "2":

    file = input("Encrypted File Path: ")

    decrypt_file(file)