#!/usr/bin/env python3
import sys
import os
import requests
import concurrent.futures
import urllib3

def send_request(domain):
    global header
    global proxy

    try:
        r = requests.get(domain, verify=False, timeout=10, headers=header, allow_redirects=False)
        #r = requests.get(domain, verify=False, timeout=10, headers=header, proxies=proxy, allow_redirects=False)
    except Exception as e:
        pass

    if 'test123' in r.text:
        for key in r.headers:
            if 'cache' in key.lower():
                print(f"{domain} {[r.status_code]}")
                break


def start(domains):
    global threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(send_request, domains)


def read_file(path):
    with open(path, "r", encoding="utf8", errors="ignore") as f:
        data = f.read()

    return data[:-1].split("\n")


def main():
    global header
    global threads
    global proxy

    threads = 200
    proxy = {'http': '127.0.0.1:8080', 'https': '127.0.0.1:8080'}
    header = {'X-Forwarded-Host': 'test123'}
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    if len(sys.argv) != 2:
        print("Usage: python3 cache.py <input file>")
        sys.exit()

    if not os.path.isfile(sys.argv[-1]):
        print("[*]Not a valid file")
        print("Usage: python3 cache.py <input file>")
        sys.exit()

    domains = read_file(sys.argv[-1])
    start(domains)

main()
