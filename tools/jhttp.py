#!/usr/bin/env python3
import sys
import os


def joinhttp(domains, words):
    for word in words:
        for domain in domains:
            print(domain+word)


def read_file(path):
    with open(path, "r", encoding="utf8", errors="ignore") as f:
        data = f.read()

    return data[:-1].split("\n")


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 jhttp.py <words file> <input file>")
        sys.exit()

    if not os.path.isfile(sys.argv[-1]) or not os.path.isfile(sys.argv[-2]):
        print("[*]Not a valid file")
        print("Usage: python3 jhttp.py <words file> <input file>")
        sys.exit()

    lines = read_file(sys.argv[-1])
    words = read_file(sys.argv[-2])

    joinhttp(lines, words)


main()
