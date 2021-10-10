#!/usr/bin/env python3
import socket
import sys
import concurrent.futures

def get_ip_addresses(domain):
    global ip_addresses
    global ip_domain
    try:
        ip = socket.gethostbyname(domain)
        ip_domain[domain] = ip
        if ip not in ip_addresses:
            ip_addresses.append(ip)
            print(ip)
    except:
        pass


def read_file(file_path):
    with open(file_path, 'r') as f:
        DOMAINS = f.readlines()

    for i in range(0, len(DOMAINS)):
        DOMAINS[i] = str(DOMAINS[i][:len(DOMAINS[i])-1])

    while('' in DOMAINS):
        DOMAINS.remove('')

    return DOMAINS


def main():
    global ip_addresses
    global ip_domain
    ip_domain = {}
    ip_addresses = []
    domains = read_file(sys.argv[-1])
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(get_ip_addresses, domains)

    with open('domain-ip', 'w') as f:
        for d in ip_domain:
            f.write(d+":"+ip_domain[d]+"\n")

main()
