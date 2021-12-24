#!/usr/bin/env python3
import os
import sys
from ipaddress import ip_network, ip_address
import socket

def resolve(ipranges):
    for iprange in ipranges:
        for ip in ip_network(iprange).hosts():
            try:
                print(socket.gethostbyname(str(ip)))
            except Exception as e:
                pass


def read_file(path):
    with open(path, 'r') as f:
        data = f.read()

    return data[:-1].split('\n')


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 resolve.py <cidr file>")
        sys.exit()

    if not os.path.isfile(sys.argv[-1]):
        print("[*]Not a valid file")
        print("Usage: python3 resolve.py <cidr file>")
        sys.exit()

    cidrs = read_file(sys.argv[-1])

    resolve(cidrs)


main()
