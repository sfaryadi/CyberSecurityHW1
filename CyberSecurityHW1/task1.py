'''
Created on Feb 13, 2021

@author: Stephen
'''
import getpass
import hashlib
import os
import math


file = open("passwords.txt","a+")

username = input("Please enter a username: ")
password = getpass.getpass("Enter Password")

length = len(password)
entropy = math.log((pow(95,length)),2)

print("The entropy of that password is:")
print(entropy)


salt = os.urandom(32);
encrypted = hashlib.pbkdf2_hmac("sha256", "password".encode("utf-8"), salt, 100000)
encrypted = encrypted.hex()

file.write("\n" + username + ": " + encrypted)
file.close