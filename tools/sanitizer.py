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
    root_domains = read_file(sys.argv[-2])
    files = read_file(sys.argv[-1])

    for f in files:
        for d in root_domains:
            if "."+d in f or '/'+d in f:
                print(f)
                break


try:
    main()
except:
    print("Usage: ./sanitizer.py <root domains> <domains>")
