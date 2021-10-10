#!/usr/bin/env python3
import sys
import os

def read_file(path):
    with open(path, 'r') as f:
        data = f.read()

    return data[:-1].split('\n')


def main():
    file_path = sys.argv[-1]
    if len(sys.argv) != 2:
        print("[*]Usage: python3 removeroot.py <file>")
        sys.exit()
    if not os.path.isfile(file_path):
        print("[*]Invalid file")
        sys.exit()

    domains = read_file(file_path)

    for d in domains:
        if d.count('.') == 1:
            continue
        print(d)


main()
