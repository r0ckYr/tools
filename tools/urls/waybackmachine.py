#!/usr/bin/env python3

import sys
import json
import os
import requests
import concurrent.futures


def send_request(domain):
    url = f"http://web.archive.org/cdx/search/cdx?url={domain}/*&output=json&collapse=urlkey"
    resp = requests.get(url, timeout=(2,60))
    return get_urls_list(resp)


def get_urls_list(resp):
    data = json.loads(resp.text)
    urls = []

    for d in data:
        if d[2] != "original":
            urls.append(d[2])

    return urls


def start_threads(domains):
    THREADS = 4
    subdomains = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        subs = list(executor.map(send_request, domains))
        executor.shutdown(wait=True)

    for i in range(0,len(subs)):
        print(str(i))
        for s in subs[i]:
            subdomains.append(s)

    return subdomains


def get_urls(domains):
   if len(domains) != 1:
       return start_threads(domains)
   else:
       return send_request(domains[0])
