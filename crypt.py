from cryptography.fernet import Fernet
import os
import getpass
from hashlib import scrypt
from base64 import urlsafe_b64encode

print("\n")
'''
password = getpass.getpass("Password : ")
password_encoded = base64.b64encode(password.encode())
key = base64.urlsafe_b64encode(password_encoded)
'''

password = getpass.getpass("Password : ")
salt = b'5\x8b%w\x0f\xb6S\x1fC\xee\x91D\xd2#\x186'
key = scrypt(password.encode(), salt=salt, n=16384, r=8, p=1, dklen=32)
key_encoded = urlsafe_b64encode(key)

directory = os.getcwd() + "/files/"

print(directory)

'''
decoded_key = key.decode()

if not len(decoded_key) == 44:
    if len(decoded_key) < 44:
        while not len(decoded_key) == 44:
            decoded_key = "".join((decoded_key, "="))
    elif len(key) > 44:
        while not len(decoded_key) == 44:
            decoded_key = decoded_key[1:]
    else:
        print("Key length incorrect")
    
    key = decoded_key.encode()
'''

print("\nFernet key : " + Fernet.generate_key().decode())
print("\nFernet key : " + key_encoded.decode() + "\n")

f = Fernet(key_encoded)

if not directory.endswith("files/"):
    print("wrong diretory")
    exit()

file_list = os.listdir(directory)

for i, file in enumerate(file_list):
    file_list[i] = directory + file

print(file_list)

test_token = 'abc'.encode()

def encode():
    with open(f"{directory}test_file", 'rb') as test:
        test_content = test.read()
        if test_content == test_token:
            test.close()
            for file in file_list:
                if not file == 'crypt.py':
                    with open(file, "rb") as read_file:
                        encrypted_file = f.encrypt(read_file.read())
                        read_file.close()
                    with open(file, "wb") as write_file:
                        write_file.write(encrypted_file)
                        write_file.close()
        else:
            print('An error has occured')
            test.close()
            exit()
    print("files encrypted")
        

def decode():
    with open(f"{directory}test_file", 'rb') as test:
        if test_content == test_token:
            print("An error has occured")
            test.close()
            exit()
        else:
            decrypted_test_file = f.decrypt(test_content)
            if decrypted_test_file == test_token:
                test.close()
                for file in file_list:
                    if not file == 'crypt.py':
                        with open(file, "rb") as read_file:
                            decrypted_file = f.decrypt(read_file.read())
                            read_file.close()
                        with open(file, "wb") as write_file:
                            write_file.write(decrypted_file)
                            write_file.close()
            else:
                print("Password incorrect")
                test.close()
    print("files decrypted")

with open(f"{directory}test_file", "rb") as test_file:
    test_content = test_file.read()
    if test_content == test_token:
        encode()
    else:
        decode()
