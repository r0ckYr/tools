#!/usr/bin/env python3
import sys
import os
import requests
import concurrent.futures
import urllib3


def send_request(url):
    try:
        resp = requests.get(url, timeout=10, verify=False, allow_redirects=False)
        if resp.status_code != 404:
            print(f"{url} [{len(resp.text)}] ({resp.status_code})")
    except Exception as e:
        pass


def read_file(path):
    data = ""
    with open(path , 'r') as f:
        data = f.read()

    return data[:-1].split('\n')


def start_threads(urls):
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(send_request, urls)


def main():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url = sys.argv[-1]
    words = read_file(sys.argv[-2])

    urls = []
    for w in words:
        urls.append(url+w)

    start_threads(urls)


main()
