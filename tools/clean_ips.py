#!/usr/bin/env python3
import os
import sys
from ipaddress import ip_network, ip_address
import requests

def clean(ips):
    ipvs4 = "https://www.cloudflare.com/ips-v4"
    ipvs6 = "https://www.cloudflare.com/ips-v6"
    try:
        ipranges = requests.get(ipvs4).text.split("\n")[:-1]
        ipranges += requests.get(ipvs6).text.split("\n")[:-1]
    except:
        ipranges = ["173.245.48.0/20","103.21.244.0/22","103.22.200.0/22","103.31.4.0/22","141.101.64.0/18","108.162.192.0/18","190.93.240.0/20","188.114.96.0/20","197.234.240.0/22","198.41.128.0/17","162.158.0.0/15","104.16.0.0/13","104.24.0.0/14","172.64.0.0/13","131.0.72.0/22","2400:cb00::/32","2606:4700::/32","2803:f800::/32","2405:b500::/32","2405:8100::/32","2a06:98c0::/29","2c0f:f248::/32"]

    nets = []
    for iprange in ipranges:
        nets.append(ip_network(iprange))
    valid_ips = []
    for ip in ips:
        if ip == "":  # skip empty line
            continue
        valid = True
        for net in nets:
            try:
                if ip_address(ip) in net:
                    valid = False
                    break
            except:
                break
            if valid:
                print(ip)


def read_file(path):
    with open(path, 'r') as f:
        data = f.read()

    return data[:-1].split('\n')


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 clean_ips.py <ip addresses file>")
        sys.exit()

    if not os.path.isfile(sys.argv[-1]):
        print("[*]Not a valid file")
        print("Usage: python3 clean_ips.py <ip addresses file>")
        sys.exit()

    ip_addresses = read_file(sys.argv[-1])

    clean(ip_addresses)


main()
