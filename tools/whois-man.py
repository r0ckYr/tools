#!/usr/bin/env python3
import sys
import subprocess
import time
import keyboard
import os

def get_whois(host):
    cmd = f"whois {host} | grep -iE 'Organizatio|Email'"
    try:
        run = subprocess.run(cmd, shell=True, text=True, capture_output=True)
        whois =  run.stdout+run.stderr
        return str(whois)
    except Exception as e:
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
        output = get_whois(domain)
        v = False
        for key in keys:
            if key in output:
                valid.append(domain)
                v = True
                break
        if v==True:
            continue

        print(output)
        print('\n------------------------\n')
        while True:
            if keyboard.is_pressed('a'):
                clear()
                valid.append(domain)
                break
            if keyboard.is_pressed('d'):
                clear()
                break
            if keyboard.is_pressed('r'):
                clear()
                get_whois(domain)
                print('\n------------------------\n')


    print('\n[*]Done\n')
    print("[*]Press 'q' to exit")

    while True:
        if keyboard.is_pressed('q'):
            clear()
            break


def main():
    global valid
    valid = []
    if len(sys.argv) != 3:
        print("Usage: python3 whois.py <key> <root domains file>")
        sys.exit()

    domains = read_file(sys.argv[-1])
    key = sys.argv[-2]
    keys = []
    if '|' in key:
        keys = key.split('|')
    else:
        keys.append(key)
    print(key)
    print(keys)
    start(domains, keys)
    file_name = 'valid'
    if os.path.isfile(file_name):
        file_name = 'valid_' + sys.argv[-1]


    with open(file_name, 'w') as f:
        for domain in valid:
            f.write(domain+'\n')


main()
