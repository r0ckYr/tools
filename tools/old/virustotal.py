#!/usr/bin/env python3

import sys
import json 
import os 
import requests
import concurrent.futures


def get_virus_domains(domain):
    url = f"https://www.virustotal.com/vtapi/v2/domain/report?domain={domain}&apikey=8481e812a65fbcf355a05e86fb0c90ea18d5a0a0e9ddf9bc4ab4102288d07d9c"
    resp = requests.get(url)
    print_data(resp)    


def print_data(resp):
    global GET_URLS
    global SUBS
    global GET_IP
    global OUTPUT

    subdomains = json.loads(resp.text)["subdomains"]
    urls1 =  json.loads(resp.text)["undetected_urls"]
    urls2 =  json.loads(resp.text)["detected_urls"]
    resolutions =  json.loads(resp.text)["resolutions"]
    if SUBS:
        for s in subdomains:
            print(s)
    if GET_URLS:
        for u1 in urls1:
            print(u1[0])
        for u2 in urls2:
            print(u2["url"])
    if GET_IP:
        for r in resolutions:
            print(r["ip_address"])
    
    if OUTPUT:
        save_data(resp)


def save_data(resp): 
    global GET_URLS
    global SUBS
    global GET_IP
    global OUTPUT

    subdomains = json.loads(resp.text)["subdomains"]
    urls1 =  json.loads(resp.text)["undetected_urls"]
    urls2 =  json.loads(resp.text)["detected_urls"]
    resolutions =  json.loads(resp.text)["resolutions"]
    
    
    word = subdomains[0].split('.')[-2]+'.'+subdomains[0].split('.')[-1]

    if SUBS:
        with open(f"subdomains-{word}", 'w') as f:
            for s in subdomains:
                f.write(s+"\n")
    if GET_URLS:
        with open(f"urls-{word}", 'w') as f:
            for u1 in urls1:
                f.write(u1[0]+"\n")
            for u2 in urls2:
                f.write(u2["url"]+"\n")
    if GET_IP:
        with open(f"ip-{word}", 'w') as f:
            for r in resolutions:
                f.write(r["ip_address"]+"\n")


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
        executor.map(get_virus_domains, domains)
        executor.shutdown(wait=True)


def get_help():
        print('''
Usage: ./virustotal.py -d target.com
    
Basic:
    -d          : specify domain or file containing domains
    -o          : output to a file
    -h          : help menu
Advance: (when no option is specified only subdomains are fetched)
    --no-subs   : get subdomains
    --urls      : get urls
    -ip         : get ip addresses
    
    ''')
        sys.exit()


def main(): 
    global GET_URLS
    global SUBS
    global GET_IP
    global OUTPUT
    
    GET_URLS = False
    SUBS = True
    GET_IP = False
    OUTPUT = False
    
    if '-h' in sys.argv:
        get_help()
    if '-d' not in sys.argv:
        get_help()
    if '--no-subs' in sys.argv:
        SUBS = False 
    if '--urls' in sys.argv:
        GET_URLS = True
    if '-ip' in sys.argv:
        GET_IP = True
    if '-o' in sys.argv:
        OUTPUT = True
    
    if os.path.isfile(sys.argv[sys.argv.index("-d") + 1]):
        start_threads(sys.argv[sys.argv.index("-d") + 1])
    else:
        domain = sys.argv[sys.argv.index("-d") + 1] 
        get_virus_domains(domain)
    

main()


