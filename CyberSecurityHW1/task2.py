'''
Created on Feb 13, 2021

@author: Stephen
'''
import string
import itertools
import hashlib
import os
import math
import time

starttime = time.clock()

file = open("passwords.txt", "r")
lines = file.readlines()
    
characters = string.printable[0: 95] 

def brutehack(correcthash):    
    
    for i in range(95):
        combos = list(itertools.combinations(characters, i))
        for i in range(len(combos)):
            password =    "".join(combos[i])
            
            salt = os.urandom(32);
            encrypted = hashlib.pbkdf2_hmac("sha256", "password".encode("utf-8"), salt, 100000)
            encrypted = encrypted.hex()
            if encrypted==correcthash:
                print("The password was " + password)
                
                length = len(password)
                entropy = math.log((pow(95,length)),2)
                print("The entropy was " + entropy)
                elapsed = time.clock() - starttime
                print("Time taken to hack the password was " + elapsed)

for i in range(len(lines)):
    line = lines[i].split(": ")
    username = line[0]
    hashed = line[1]
    
    brutehack(hashed)
    