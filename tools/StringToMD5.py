#!/usr/bin/env python3
import sys
import hashlib


try:
    text = sys.argv[1]
except IndexError:
    print("Usage : python3 StringToMD5.py <text>")
    sys.exit()


hash_object = hashlib.md5(text.encode())

md5_hash = hash_object.hexdigest()


print(f"hash : {md5_hash}")
