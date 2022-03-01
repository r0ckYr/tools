#!/usr/bin/env python3
import sys
import os
import subprocess
import concurrent.futures


def get_ips(lines):
    ip_addresses = []
    for line in lines:
        if "Host:" in line and "Ports:" in line:
            ip = line.split()[3]
            if ip not in ip_addresses:
                ip_addresses.append(ip)
    return ip_addresses


def arrange_data(lines, ip_addresses):
    commands = []
    for i in range(0,len(ip_addresses)):
        ip = ip_addresses[i]
        ports = ""
        for line in lines:
            if ip in line:
                ports = ports + "," + line.split()[-1].split('/')[0]

        ports = ports[1:]
        cmd = f"sudo nmap -sC -T4 -Pn -v --open -oN nmap/nmap-{ip} -p {ports} {ip}"
        commands.append(cmd)

    return commands


def nmap(cmd):
    print(f'Executing nmap on: {cmd.split()[-1]} -p {cmd.split()[-2]}')
    run = subprocess.run(cmd, shell=True, capture_output=True, text=True)


def read_file(path):
    with open(path, "r", encoding="utf8", errors="ignore") as f:
        data = f.read()

    return data[:-1].split('\n')


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 massnmap.py <input file>")
        sys.exit()

    if not os.path.isfile(sys.argv[-1]):
        print("[*]Not a valid file")
        print("Usage: python3 massnmap.py <input file>")
        sys.exit()

    lines = read_file(sys.argv[-1])

    ip_addresses = get_ips(lines)

    commands = arrange_data(lines, ip_addresses)

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(nmap, commands)


main()
