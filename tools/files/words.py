#!/usr/bin/env python3
import sys


def read_file(path):
    with open(path ,'r') as f:
        data = f.read()

    return data[:-1].split('\n')


def main():
    path = sys.argv[-1]
    domains = read_file(path)

    for domain in domains:
        words = domain.split('.')
        for word in words:
            print(word)

main()
