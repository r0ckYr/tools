#!/usr/bin/env python3
import sys
import os


def get_intresting(domains):
    global subs
    subs = []
    for domain in domains:
        #remove root domains
        if domain.count('.') < 2:
            continue

        #check in domain is alreads in subs
        words = domain.split('.')
        dom = f"{words[-3]}.{words[-2]}.{words[-1]}"
        if dom in subs:
            continue

        #check if domain has third-level-domains
        if domain.count('.') > 2:
            print_domain(dom)


def print_domain(sub):
    global subs
    print(sub)
    subs.append(sub)


def read_file(file_path):
    with open(file_path, 'r') as f:
        DOMAINS = f.read()

    return DOMAINS[:-1].split('\n')


def main():
    domains_file = sys.argv[-1]
    domains = []
    if os.path.isfile(domains_file):
        domains = read_file(domains_file)
    else:
        print("[*]Not a file !")
        sys.exit()

    get_intresting(domains)


main()
