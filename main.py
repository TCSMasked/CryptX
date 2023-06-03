from cryptography.fernet import Fernet
import os

def encrypt_file(file_path):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"Encryption successful! Encrypted file created: {encrypted_file_path}")


def decrypt_file(file_path):
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    key = Fernet.generate_key()
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    decrypted_file_path = file_path.replace('.encrypted', '.decrypted')
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    print(f"Decryption successful! Decrypted file created: {decrypted_file_path}")

def launch_module():
    choice = input("Please choose a module:\n1. Encryption\n2. Decryption\n")
    if choice == '1':
        file_path = input("Enter the path of the file to encrypt: ")
        if os.path.exists(file_path):
            encrypt_file(file_path)
        else:
            print("File not found!")
    elif choice == '2':
        file_path = input("Enter the path of the file to decrypt: ")
        if os.path.exists(file_path) and file_path.endswith('.encrypted'):
            decrypt_file(file_path)
        else:
            print("Encrypted file not found!")
    else:
        print("Invalid choice!")

launch_module()