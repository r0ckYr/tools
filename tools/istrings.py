#!/usr/bin/env python3
import sys


def read_file(file_path):
    DOMAINS = []
    with open(file_path, 'r') as f:
        while(f.readline()):
            DOMAINS.append(f.readline()[:-1].replace('"', ''))


    return DOMAINS


def get_intresting(words):
    for word in words:
        if '!' in word or '/' in word or '<' in word or '>' in word:
            continue
        if len(word) > 9 and len(word) < 50:
            print(word)


def main():
    words = read_file(sys.argv[-1])
    get_intresting(words)


main()
