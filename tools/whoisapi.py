#!/usr/bin/env python3
import sys
import os
import concurrent.futures
import requests
import json

def send_request(key):
    try:
        url = "https://reverse-whois.whoisxmlapi.com/api/v2"

        data = {
            "apiKey": "at_y7T1mkeyJtVwZjp7iDGI67PRhEDsy",
            "searchType": "current",
            "mode": "purchase",
            "searchAfter": 1644572383,
            "basicSearchTerms": {
                "include": [
                    key,
                ]
                }
            }
    except Exception as e:
        print(e)

    try:
        r = requests.post(url, json=data)
        domains = json.loads(r.text)["domainsList"]
        for domain in domains:
            print(domain)
    except Exception as e:
        print(str(e))




def start(keys):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(send_request, keys)


def read_file(path):
    with open(path, "r", encoding="utf8", errors="ignore") as f:
        data = f.read()

    return data[:-1].split("\n")


def main():
    keys = []

    if len(sys.argv) != 2:
        print("Usage: python3 whoisapi.py <input file>")
        sys.exit()

    if not os.path.isfile(sys.argv[-1]):
        keys.append(sys.argv[-1])
    else:
        keys = read_file(sys.argv[-1])

    start(keys)

main()
