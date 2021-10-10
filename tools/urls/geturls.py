#!/usr/bin/env python3

#standard packages
import sys
import os
import concurrent.futures
import re
#added packages
import alienvault
import virustotal
import commoncrawl
import waybackmachine

def get_urls(source):
    global domains
    global urls
    try:
        subs = eval(f"{source}.get_urls({domains})")
    except Exception as e:
        pass

    for s in subs:
        if s not in urls and s is not None:
            urls.append(s)
            print(s)


def start_threads():
    THREADS = 4
    SOURCES = ["alienvault", "virustotal", "commoncrawl", "waybackmachine"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(get_urls, SOURCES)


def read_file(file_path):
    with open(file_path, 'r') as f:
        DOMAINS = f.readlines()

    for i in range(0, len(DOMAINS)):
        DOMAINS[i] = str(DOMAINS[i][:len(DOMAINS[i])-1])

    while('' in DOMAINS):
        DOMAINS.remove('')

    domains = []
    for d in DOMAINS:
        if d not in domains:
            domains.append(d)

    return domains


def main():
    #get domains to search
    global domains
    global urls
    urls = []
    domains_file = sys.argv[-1]
    domains = []
    if os.path.isfile(domains_file):
        domains = read_file(domains_file)
    else:
        if '.' in domains_file:
            domains.append(domains_file)
        else:
            print("[*]Not a valid domain")

    #start searching for urls
    start_threads()


#sart point
main()



