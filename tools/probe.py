#!/usr/bin/env python3
import requests
import sys
import concurrent.futures


def send_request(url):
    try:
        r = requests.head(url, timeout=1)
        print(url)
    except Excption as e:
        pass


def start_threads(urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(send_request, urls)


def read_file(file_path):
    with open(file_path, 'r') as f:
        DOMAINS = f.readlines()

    domains = []

    for i in range(0, len(DOMAINS)):
        DOMAINS[i] = str(DOMAINS[i][:len(DOMAINS[i])-1])

    while('' in DOMAINS):
        DOMAINS.remove('')

    for d in DOMAINS:
        if d not in domains:
            domains.append(d)

    DOMAINS = domains
    domains = []

    return DOMAINS


def main():
    filename = sys.argv[-1]
    domains = read_file(filename)
    urls = []
    for d in domains:
        urls.append("https://"+d)
        urls.append("http://"+d)
    start_threads(urls)


main()
