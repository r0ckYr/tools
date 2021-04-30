#!/usr/bin/env python3
import socket
import sys
import os
import concurrent.futures
import time

def is_alive(domain):
    try:
        socket.gethostbyname(domain)
        print(domain)
        return domain
    except:
        pass


def start_threads(domains):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        subs = list(executor.map(is_alive, domains))
        executor.shutdown(wait=True)


def read_file(file_path):
    with open(file_path, 'r') as f:
        DOMAINS = f.readlines()

    for i in range(0, len(DOMAINS)):
        DOMAINS[i] = str(DOMAINS[i][:len(DOMAINS[i])-1])

    while('' in DOMAINS):
        DOMAINS.remove('')

    return DOMAINS


def make_list(domains, words):
    subdomains = []
    for w in words:
        for d in domains:
            s = w+'.'+d
            if s not in subdomains:
                subdomains.append(s)

    return subdomains


def main():
    start = time.perf_counter()
    domains_file = sys.argv[-1]
    domains = []
    doms = []
    words_file = "/home/rocky/tools/SecLists/Discovery/DNS/deepmagic.com-prefixes-top500.txt"
    words = read_file(words_file)
    if len(sys.argv) != 2:
        print("[*]Invalid!")
        sys.exit()

    if os.path.isfile(domains_file):
        domains = read_file(domains_file)
    else:
        domains.append(domains_file)

    doms = make_list(domains, words)

    start_threads(doms)

    finish = time.perf_counter()
    print("\n"+str(finish-start))


main()
