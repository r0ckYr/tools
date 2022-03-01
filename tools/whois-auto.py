#!/usr/bin/env python3
import sys
import subprocess
import time
import os

def get_whois(host):
    cmd = f"whois {host} | grep -iE 'Organizatio|Email'"
    try:
        run = subprocess.run(cmd, shell=True, text=True, capture_output=True)
        whois =  run.stdout+run.stderr
        return str(whois)
    except Exception as e:
        print(e)
        return str(e)


def read_file(path):
    with open(path, 'r') as f:
        data = f.read()

    return data[:-1].split('\n')

def clear():
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')


def start(domains, keys):
    global valid
    for domain in domains:
        print(domain+'\n')
        time.sleep(1)
        output = get_whois(domain)
        for key in keys:
            if key in output:
                valid.append(domain)
                print('added\n---\n')
                break


def main():
    global valid
    valid = []
    if len(sys.argv) != 3:
        print("Usage: python3 whois.py <key> <root domains file>")
        sys.exit()
    keys = []
    domains = read_file(sys.argv[-1])
    key = sys.argv[-2]
    print("key: "+key)
    if '|' in key:
        keys = key.split('|')
    else:
        keys.append(key)
    print("keys: "+str(keys)+"\n\n")
    start(domains, keys)
    file_name = 'valid'
    if os.path.isfile(file_name):
        file_name = 'valid_' + sys.argv[-1]


    with open(file_name, 'w') as f:
        for domain in valid:
            f.write(domain+'\n')


main()
