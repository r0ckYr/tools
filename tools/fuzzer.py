#!/usr/bin/env python3
import concurrent.futures
import sys
import requests

def send_request(url):
    r = requests.get(url)
    print(url)


def read_file(file_path):
    with open(file_path, 'r') as f:
        DOMAINS = f.readlines()
    
    for i in range(0, len(DOMAINS)):
        DOMAINS[i] = str(DOMAINS[i][:len(DOMAINS[i])-1])
        DOMAINS[i] = DOMAINS[i]+str(sys.argv[-2])

    while('' in DOMAINS):
        DOMAINS.remove('')

    return DOMAINS


def main():
    if(len(sys.argv)!=3):
        print("Usage :./fuzzer.py <file conatining urls> <payload>")
        sys.exit()
    domains = read_file(sys.argv[-1])

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(send_request, domains)


main()
