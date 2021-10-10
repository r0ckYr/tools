#!/usr/bin/env python3

#standard packages
import sys
import os
import concurrent.futures
import re
#added packages
import alienvault
import hackertarget
import crtsh
import threatcrowd
import virustotal
import bufferoverrun
import securitytrails
import certspotter
import public


def get_domains(source):
    global domains
    global subdomains
    try:
        subs = eval(f"{source}.get_domains({domains})")
    except Exception as e:
        #print(source+": "+str(e))
        pass
    try:
        for s in subs:
            if s not in subdomains and isValidDomain(s) and is_useful(s) and s is not None:
                subdomains.append(s)
                print(s)
    except Exception as e:
        pass


def is_useful(sub):
    global domains
    for domain in domains:
        if sub.endswith("."+domain):
            return True
    return False


def isValidDomain(sub):
    regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"

    p = re.compile(regex)
    if '.' not in sub:
        return False

    if (sub == None):
        return False

    if(re.search(p, sub)):
        return True
    else:
        return False


def start_threads():
    THREADS = public.THREADS
    SOURCES = ["alienvault", "hackertarget", "crtsh", "threatcrowd", "virustotal", "bufferoverrun", "securitytrails", "certspotter"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(get_domains, SOURCES)
        executor.shutdown(wait=True)


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


def get_thirdlevel_domains(domains):
    subs = []
    for d in domains:
        s = d.split('.')
        if len(s) > 2:
            domain = f"{s[-3]}.{s[-2]}.{s[-1]}"
            if domain not in subs:
                subs.append(domain)

    return subs


def main():
    #get domains to search
    global domains
    global subdomains
    subdomains = []
    domains_file = sys.argv[-1]
    domains = []
    third_level_domains = []
    if os.path.isfile(domains_file):
        domains = read_file(domains_file)
    else:
        if '.' in domains_file:
            domains.append(domains_file)
        else:
            print(domains_file)
            print("[*]dNot a valid domain")

    #start searching for domains
    start_threads()
    #searching for third-level-domains
    if '-r' in sys.argv:
        print("third level scan")
        third_level_domains = get_thirdlevel_domains(subdomains)
        for d in third_level_domains:
            domains = d
            start_threads()




#sart point
try:
    main()
except Exception as e:
    pass




