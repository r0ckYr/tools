#!/usr/bin/env python3
import sys
import os


def read_file(file_path):
    with open(file_path, 'r') as f:
        DOMAINS = f.readlines()

    for i in range(0, len(DOMAINS)):
        DOMAINS[i] = str(DOMAINS[i][:len(DOMAINS[i])-1])

    while('' in DOMAINS):
        DOMAINS.remove('')

    return DOMAINS


def main():
    if len(sys.argv) < 3:
        print("\nUsage: python3 <output file> <input file>\n")
        sys.exit()

    if not os.path.isfile(sys.argv[-1]):
        print(f"\n[*]Not a file: {sys.argv[-1]}\n")
        sys.exit()

    domains = read_file(sys.argv[-1])
    wordlist = []
    words = []
    for d in domains:
        words = d.split(".")
        for w in words:
            if w not in wordlist:
                wordlist.append(w)

    with open(sys.argv[-2], 'w') as f:
        for w in wordlist:
            print(w)
            f.write(w+"\n")



main()
