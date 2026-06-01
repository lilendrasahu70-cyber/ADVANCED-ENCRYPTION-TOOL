import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from encrypted import encrypt_file
from decrypted import decrypt_file

root = tk.Tk()

root.title("AES Encryption Tool")
root.geometry("400x300")

# Encrypt Function
def encrypt():
    file = filedialog.askopenfilename()

    if file:
        encrypt_file(file)
        messagebox.showinfo("Success", "File Encrypted Successfully")

# Encrypt Button
encrypt_btn = tk.Button(
    root,
    text="Encrypt File",
    command=encrypt
)

encrypt_btn.pack(pady=20)

# Decrypt Function
def decrypt():

    file = filedialog.askopenfilename()

    if file:
        decrypt_file(file)
        messagebox.showinfo("Success", "File Decrypted Successfully")
# Decrypt Button
decrypt_btn = tk.Button(
    root,
    text="Decrypt File",
    command=decrypt
)

decrypt_btn.pack(pady=20)

root.mainloop()