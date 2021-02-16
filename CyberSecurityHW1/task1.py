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
entropy = math.log((pow(94,length)),2)

print("The entropy of that password is:")
print(entropy)

#I used 94 as the number of possible symbols because I wanted to account for the fact that the password could use any combination of characters

salt = os.urandom(32);
encrypted = hashlib.pbkdf2_hmac("sha256", b"password", b"salt", 100000)
encrypted = encrypted.hex()

file.write("\n" + username + ": " + encrypted)
file.close