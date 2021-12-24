#!/usr/bin/env python3
import os
import sys

def read_file(path):
    with open(path, 'r', encoding="utf-8", errors="ignore") as f:
        data = f.read()

    return data[:-1].split('\n')


def convert(lines):
    for line in lines:
        if "Host" in line and "Ports" in line:
            out_string = str(line.split()[3]) + ':' + str(line.split()[6].split('/')[0])
            print(out_string)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 masscan2httpx.py <masscan file>")
        sys.exit()

    if not os.path.isfile(sys.argv[-1]):
        print("[*]Not a valid file")
        sys.exit()

    lines = read_file(sys.argv[-1])

    convert(lines)



main()
