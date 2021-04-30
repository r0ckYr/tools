#!/usr/bin/env python3

import concurrent.futures
import requests
import json
import sys
import os


def crtsh(domain):
    domains = []
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    r = requests.get(url)
    resp = json.loads(r.text)

    for key in resp:
        subdomain = key["common_name"]
        if "*" not in subdomain and subdomain not in domains and subdomain != domain:
            domains.append(subdomain)

    for key in resp:
        subdomain = key["name_value"]
        if "*" not in subdomain and subdomain not in domains and subdomain != domain:
            domains.append(subdomain)

    if len(domains) > 0:
        for d in domains:
            if '\n' in d:
                temp = d.split('\n')
                domains.remove(d)
                for t in temp:
                    domains.append(t)

    for d in domains:
        if " " not in d and "," not in d:
            print(d)


def read_file(file_path):
    with open(file_path, 'r') as f:
        DOMAINS = f.readlines()

    for i in range(0, len(DOMAINS)):
        DOMAINS[i] = str(DOMAINS[i][:len(DOMAINS[i])-1])

    while('' in DOMAINS):
        DOMAINS.remove('')

    return DOMAINS


def main():
    THREADS = 4
    if os.path.isfile(sys.argv[-1]):
        domains = read_file(sys.argv[-1])
        with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
            executor.map(crtsh, domains)
    else:
        crtsh(sys.argv[-1])


main()

