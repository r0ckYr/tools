#!/usr/bin/env python3
import sys
import os


def get_ips(lines):
    ip_addresses = []
    for line in lines:
        if "Host:" in line and "Ports:" in line:
            ip = line.split()[3]
            if ip not in ip_addresses:
                ip_addresses.append(ip)
    return ip_addresses


def arrange_data(lines, ip_addresses):
    for i in range(0,len(ip_addresses)):
        ip = ip_addresses[i]
        c = 0
        ports = []
        for line in lines:
            if ip in line:
                c = c + 1
                ports.append(line.split()[-1].split('/')[0])
                if c > 15:
                    break
        if c > 0 and c <=15:
            print(f"---({ip})---")
            spaces = ' '*(len(str(i))+2)
            for port in ports:
                print("-"+port)
            print('')
            print('')



def read_file(path):
    with open(path, "r", encoding="utf8", errors="ignore") as f:
        data = f.read()

    return data[:-1].split('\n')


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 ports.py <input file>")
        sys.exit()

    if not os.path.isfile(sys.argv[-1]):
        print("[*]Not a valid file")
        print("Usage: python3 ports.py <input file>")
        sys.exit()

    lines = read_file(sys.argv[-1])

    ip_addresses = get_ips(lines)


    arrange_data(lines, ip_addresses)

main()
