#!/usr/bin/env python3
import sys
import requests
import concurrent.futures
import os

def send_request(domain):
    global key
    try:
        url = f"https://www.whois.com/whois/{domain}"
        r = requests.get(url)
        if key in r.text:
            print(domain)
    except Exception as e:
        print(e)


def read_file(file_path):
    with open(file_path, 'r') as f:
        DOMAINS = f.readlines()

    for i in range(0, len(DOMAINS)):
        DOMAINS[i] = str(DOMAINS[i][:len(DOMAINS[i])-1])

    while('' in DOMAINS):
        DOMAINS.remove('')

    return DOMAINS


def start_threads(domains):
    THREADS = 20
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(send_request, domains)


def main():
    global key
    try:
        if len(sys.argv) != 3 or os.path.isfile(sys.argv[-1])==False:
            print("Usage: ./whois.py <key> <domains_file>")
            sys.exit()

        key = sys.argv[-2]
        domains = read_file(sys.argv[-1])
        start_threads(domains)
    except Exception as e:
        print(e+"\nUsage: ./whois.py <key> <domains_file>")


main()
