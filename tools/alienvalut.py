#!/usr/bin/env python3

import sys
import json
import os
import requests
import concurrent.futures


def get_alienvault_domains(domain):
    url = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns"
    resp = requests.get(url)
    print_data(resp)


def print_data(resp):
    global SUBS
    global GET_IP
    global OUTPUT

    resolutions = []
    subdomains = []
    s2 = []
    r2 = []
    data =  json.loads(resp.text)["passive_dns"]
    for d in data:
        subdomains.append(d["hostname"])
        resolutions.append(d["address"])

    if SUBS:
        for s in subdomains:
            if s not in s2:
                s2.append(s)
    if GET_IP:
        for r in resolutions:
            if r not in r2:
                if validate_ip(r):
                    r2.append(r)
                else:
                    if r not in s2:
                        s2.append(r)

    for s in s2:
        print(s)

    for r in r2:
        print(r)

    if OUTPUT:
        save_data(s2, r2)


def save_data(subdomains, resolutions):
    global SUBS
    global OUTPUT

    word = subdomains[0].split('.')[-2]+'.'+subdomains[0].split('.')[-1]

    if SUBS:
        with open(f"subdomains-{word}", 'w') as f:
            for s in subdomains:
                f.write(s+"\n")
    if GET_IP:
        with open(f"ip-{word}", 'w') as f:
            for r in resolutions:
                f.write(r+"\n")


def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


def read_file(file_path):
    with open(file_path, 'r') as f:
        DOMAINS = f.readlines()

    for i in range(0, len(DOMAINS)):
        DOMAINS[i] = str(DOMAINS[i][:len(DOMAINS[i])-1])

    while('' in DOMAINS):
        DOMAINS.remove('')

    return DOMAINS


def start_threads(domains_file):
    THREADS = 4
    domains = read_file(domains_file)
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(get_alienvault_domains, domains)
        executor.shutdown(wait=True)


def get_help():
        print('''
Usage: ./alienvault.py -d target.com

Basic:
    -d          : specify domain or file containing domains
    -o          : output to a file
    -h          : help menu
Advance: (when no option is specified only subdomains are fetched)
    --no-subs   : get subdomains
    -ip         : get ip addresses

    ''')
        sys.exit()


def main():
    global SUBS
    global OUTPUT
    global GET_IP

    SUBS = True
    GET_IP = False
    OUTPUT = False

    if '-h' in sys.argv:
        get_help()
    if '-d' not in sys.argv:
        get_help()
    if '--no-subs' in sys.argv:
        SUBS = False
    if '-ip' in sys.argv:
        GET_IP = True
    if '-o' in sys.argv:
        OUTPUT = True

    if os.path.isfile(sys.argv[sys.argv.index("-d") + 1]):
        start_threads(sys.argv[sys.argv.index("-d") + 1])
    else:
        domain = sys.argv[sys.argv.index("-d") + 1]
        get_alienvault_domains(domain)


main()


