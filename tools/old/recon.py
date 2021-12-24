#!/usr/bin/env python3

import subprocess
import concurrent.futures
import time
import sys
import os
import socket
import requests
import json
import requests

start = time.perf_counter()

def crtsh(domain):

    domains = []
    d2 = []
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    r = requests.get(url)
    resp = json.loads(r.text)

    for key in resp:
        subdomain = key["name_value"]
        if "*" not in subdomain and subdomain not in domains and subdomain != domain:
            domains.append(subdomain)

    for d in domains:
        if d not in d2:
            d2.append(d)

    domains = d2
    if len(domains) > 0:
        with open(f"{domain}.txt", 'w') as f:
            for d in domains:
                if '\n' in d:
                    temp = d.split('\n')
                    domains.remove(d)
                    for t in temp:
                        domains.append(t)
                print(d)
                f.write(d+'\n')



def read_file(file_path):
    with open(file_path, 'r') as f:
        DOMAINS = f.readlines()

    for i in range(0, len(DOMAINS)):
        DOMAINS[i] = str(DOMAINS[i][:len(DOMAINS[i])-1])

    while('' in DOMAINS):
        DOMAINS.remove('')

    return DOMAINS


def start_threads(domains, level):
    if level == 1:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            executor.map(crtsh, domains)
            executor.shutdown(wait=True)

    elif level == 2:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(crtsh, domains)
            executor.shutdown(wait=True)

    elif level == 3:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(resolv_ip, domains)
            executor.shutdown(wait=True)


def level1_recon():
    FILE = sys.argv[len(sys.argv)-1]
    domains = read_file(FILE)
    start_threads(domains, 1)
    subprocess.call(['/bin/bash', '-i', '-c', 'cleanup'])
    print("[*]Level 1 recon done ..........................................................")
    print("[*]Waiting for sublister,subfinder and shuffledns..........................................")


def third_level_recon():
    if os.path.isfile("subfinder/all.txt") and os.path.isfile("sublister/all.txt") and os.path.isfile("shuffledns/all.txt"):
        subfinder_domains = []
        sublister_domains = []
        print("[*]Starting level 2 recon...................................................")
        subfinder_domains = read_file("subfinder/third-level-all.txt")
        sublister_domains = read_file("sublister/third-level-all.txt")
        ROOT_DOMAINS_FILE = "third-level-all.txt"
        shuffledns_domains = read_file("shuffledns/third-level-all.txt")
        root_domains = read_file(ROOT_DOMAINS_FILE)
        domains = []

        for sld in sublister_domains:
            if sld not in domains:
                domains.append(sld)

        for sfd in subfinder_domains:
            if sfd not in domains:
                domains.append(sfd)

        for rd in root_domains:
            if rd not in domains:
                domains.append(sfd)

        for sdd in shuffledns_domains:
            if sdd not in domains:
                domains.append(sdd)

        print(f"[*]Total third level domains : {len(domains)}")
        os.system("mkdir third_level_domains")
        os.chdir("third_level_domains")
        start_threads(domains, 2)
        subprocess.call(['/bin/bash', '-i', '-c', 'cleanup'])
        os.chdir("../")
        print("[*]Third Level recon done ...................................................")
    else:
        time.sleep(3)
        third_level_recon()


def resolv_ip(domain):
    global ip_addresses
    global ip_domain
    try:
        ip = socket.gethostbyname(domain)
        print(f"{domain}  {ip}")
        ip_domain[domain] = ip
        ip_addresses.append(ip)
    except:
        pass


def get_ip_addresses(domain_file):
    global ip_addresses
    global ip_domain
    ip_domain = {}
    ip_addresses = []
    print("scan started")
    domains = read_file(domain_file)
    start_threads(domains, 3)
    ip2 = []
    for ip in ip_addresses:
        if ip not in ip2:
            ip2.append(ip)

    ip_address = ip2
    with open(f"final/ip-addresses-final.txt", 'w') as f:
        for ip in ip_addresses:
            f.write(ip+'\n')

    with open(f"final/ip-domain.txt", 'w') as f:
        for key in ip_domain:
            f.write(key+"  "+ip_domain[key]+"\n")



def start_port_scan():
    os.system("mkdir nmap")
    cmd = "sudo nmap -Pn -v -T4 -iL active-domains.txt -oN nmap/port-scan"
    subprocess.call(['/bin/bash', '-i', '-c', cmd])


def take_screenshots():
    subprocess.call(['/bin/bash', '-i', '-c', 'aqua final/active-final.txt'])


def waback():
    subprocess.call(['/bin/bash', '-i', '-c', 'waybackall final/active-final.txt | tee -a final/wayback-final.txt'])


def main():
    if len(sys.argv) > 2:
        if '-d' in sys.argv:
            level1_recon()
        if '-3' in sys.argv:
            third_level_recon()
        if '-ip' in sys.argv:
            get_ip_addresses(sys.argv[-1])

    else:
        level1_recon()
        third_level_recon()
        subprocess.call(['/bin/bash', '-i', '-c', 'finalize'])
        get_ip_addresses("final/final.txt")

        finish = time.perf_counter()
        print(f"[*]Finished in {round(finish-start, 2)} second(s)")

        print("\nTotal hosts:")
        c = os.system("wc -l final/final.txt")


        #port scanning
        do = input("Start port scan[Y/N] :")
        if do.lower()=="y":
            start_port_scan()

        #screenshot
        do = input("Take screen shots[Y/N] :")
        if do.lower()=="y":
            take_screenshots()

        #waybackurls
        do = input("Get waybackurls[Y/N] :")
        if do.lower()=="y":
            wayback()


        os.chdir("final/")
        os.system("wc -l *")


    finish = time.perf_counter()
    print(f"[*]Finished in {round(finish-start, 2)} second(s)")


try:
    main()
except KeyboardInterrupt:
    print("\nBye\n")

