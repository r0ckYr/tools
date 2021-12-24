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
    out = ""
    lines = read_file(sys.argv[-1])
    for l in lines:
        out = out + '|' + l
    print(out[1:])


main()
