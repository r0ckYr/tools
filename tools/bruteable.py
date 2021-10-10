#!/usr/bin/env python3
import sys


def read_file(file_path):
    with open(file_path, 'r') as f:
        DOMAINS = f.readlines()

    for i in range(0, len(DOMAINS)):
        DOMAINS[i] = str(DOMAINS[i][:len(DOMAINS[i])-1])

    while('' in DOMAINS):
        DOMAINS.remove('')

    return DOMAINS


def main():
    domains_file = sys.argv[-1]
    domains = read_file(domains_file)
    for d in domains:
        if d.count('.') >= (int(sys.argv[-2])-1):
            print(d)


main()
