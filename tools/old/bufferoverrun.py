#!/usr/bin/env python3

import sys
import json 
import os 
import requests
import concurrent.futures



def get_bufferoverrun_domains(domain):
    url = f"https://dns.bufferover.run/dns?q={domain}"
    resp = requests.get(url)
    print_data(resp)


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


def print_data(resp):
    global SUBS
    global GET_IP
    global OUTPUT

    data = json.loads(resp.text)["FDNS_A"]
    subdomains = []
    ips =[]

    for d in data:
        words = d.split(',')
        for w in words:
            if validate_ip(w):
                if w not in ips:
                    ips.append(w)
            else:
                if w not in subdomains:
                    subdomains.append(w)
    
    if SUBS:
        for subdomain in subdomains:
            print(subdomain) 
    if GET_IP:
        for ip in ips:
            print(ip)

    if OUTPUT:
        save_data(resp)
    

def save_data(resp): 
    global SUBS
    global OUTPUT
    global GET_IP

    data = json.loads(resp.text)["FDNS_A"]
    subdomains = []
    ips =[]

    for d in data:
        words = d.split(',')
        for w in words:
            if validate_ip(w):
                if w not in ips:
                    ips.append(w)
            else:
                if w not in subdomains:
                    subdomains.append(w)
    word = subdomains[0].split('.')[-2]+'.'+subdomains[0].split('.')[-1]
    if SUBS:
        with open(f"subdomains-{word}", 'w') as f:
            for subdomain in subdomains:
                f.write(subdomain+"\n") 
    if GET_IP:
        with open(f"ips-{word}", 'w') as f:
            for ip in ips:
                f.write(ip+"\n")


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
        executor.map(get_bufferoverrun_domains, domains)
        executor.shutdown(wait=True)


def get_help():
        print('''
Usage: ./bufferoverrun.py -d target.com
    
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
        get_bufferoverrun_domains(domain)
    

main()


