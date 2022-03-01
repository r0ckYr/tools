#!/usr/bin/env python3
import sys
import os


def get_uniq(lines):
    patterns = []
    for line in lines:
        p = str(line.split()[0])
        if p not in patterns:
            patterns.append(p)

    for p in patterns:
        c = 0
        for line in lines:
            if p in line:
                c = c+1
            if c == 4:
                break
        if c <4:
            for line in lines:
                if p in line:
                    print(line)




def read_file(path):
    with open(path, "r", encoding="latin-1", errors="ignore") as f:
        data = f.read()

    return data[:-1].split("\n")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 uniq2.py <input file/'-'(stdin)>")
        sys.exit()

    if not os.path.isfile(sys.argv[-1]) and sys.argv[-1] != '-':
        print("[*]Not a valid file")
        print("Usage: python3 uniq2.py <input file/'-'(stdin)>")
        sys.exit()

    if sys.argv[-1] == '-':
        lines = sys.stdin.read()[:-1].split('\n')
    else:
        lines = read_file(sys.argv[-1])

    get_uniq(lines)

main()
