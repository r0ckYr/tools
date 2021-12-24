#!/usr/bin/python3
import sys

subdomains = []
new_subdomains = []

def main():
    path = sys.argv[1]
    with open(path, 'r') as f:
        subdomains = f.readlines()


    for s in subdomains:
        new_subdomains.append(s[s.index(":") + 3:])


    with open(path, 'w') as f:
        for s in new_subdomains:
            f.write(s)


try:
    main()
except IndexError:
    print("Usage : python3 trimmer.py {file}")
except FileNotFoundError:
    print("[*]File not found")


        
