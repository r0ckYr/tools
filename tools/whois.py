#!/usr/bin/env python3
import sys
import requests
import concurrent.futures
import os
import time

def send_request(domain):
    global keys
    global logs
    try:
        url = f"https://www.whois.com/whois/{domain}"
        r = requests.get(url)
        for key in keys:
            if key in r.text:
                print(domain)
        if len(r.text) < 60000:
            logs.append(domain)
    except Exception as e:
        pass


def read_file(file_path):
    with open(file_path, 'r') as f:
        DOMAINS = f.readlines()

    for i in range(0, len(DOMAINS)):
        DOMAINS[i] = str(DOMAINS[i][:len(DOMAINS[i])-1])

    while('' in DOMAINS):
        DOMAINS.remove('')

    return DOMAINS


def start_threads(domains):
    global logs
    THREADS = 20
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(send_request, domains)

    with open('errors', 'w') as f:
        for l in logs:
            f.write(l+'\n')


def main():
    global keys
    global logs
    keys = []
    logs = []
    try:
        if len(sys.argv) != 3 or os.path.isfile(sys.argv[-1])==False:
            print("Usage: ./whois.py <key> <domains_file>")
            sys.exit()

        if '|' in sys.argv[-2]:
            keys = sys.argv[-2].split('|')
        else:
            keys.append(sys.argv[-2])
        domains = read_file(sys.argv[-1])
        start_threads(domains)
    except Exception as e:
        print(e+"\nUsage: ./whois.py <key> <domains_file>")


main()
