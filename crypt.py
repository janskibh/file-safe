############################ IMPORTING MODULES ################################

from cryptography.fernet import Fernet
import os
import getpass
from hashlib import scrypt
from base64 import urlsafe_b64encode

###############################################################################


########################## FERNET KEY GENERATING ##############################

password = getpass.getpass("\nPassword : ")
salt = b'5\x8b%w\x0f\xb6S\x1fC\xee\x91D\xd2#\x186'
key = scrypt(password.encode(), salt=salt, n=16384, r=8, p=1, dklen=32)
key_encoded = urlsafe_b64encode(key)

print("\nFernet key : " + key_encoded.decode() + "\n")

f = Fernet(key_encoded)

###############################################################################


############################ FILES ENUMERATION ################################

directory = os.getcwd() + "/"

files_directory = directory + "files/"

if not files_directory.endswith("files/"):
    print("wrong diretory")
    exit()

file_list = os.listdir(files_directory)

for i, file in enumerate(file_list):
    file_list[i] = files_directory + file
    print(file_list[i])

file_list.append(directory + "test_file")

##############################################################################


########################## ENCRYPTING FUNCTION ###############################

def encrypt():
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
    print("\nfiles encrypted\n")
        
##############################################################################


######################### DECRYPTING FUNCTION#################################

def decrypt():
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
    print("\nfiles decrypted\n")

##############################################################################


############## CHOOSING BETWEEN ENCRYPT AND DECRYPT FUNCTION #################

test_token = 'abc'.encode()

with open(f"{directory}test_file", "rb") as test_file:
    test_content = test_file.read()
    if test_content == test_token:
        encrypt()
    else:
        decrypt()

##############################################################################
