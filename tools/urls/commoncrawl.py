#!/usr/bin/env python3

import sys
import json
import os
import requests
import concurrent.futures



def send_request(domain):
    url = f"http://index.commoncrawl.org/CC-MAIN-2018-22-index?url={domain}/*&output=json"
    resp = requests.get(url, timeout=(2,10))
    return get_urls_list(resp)


def get_urls_list(resp):
    data = resp.text.split('\n')
    urls = []
    for d in data:
        try:
            urls.append(json.loads(d)["url"])
        except:
            pass
    return urls


def start_threads(domains):
    THREADS = 4
    urls = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        subs = list(executor.map(send_request, domains))
        executor.shutdown(wait=True)

    for i in range(0,len(subs)):
        print(str(i))
        for s in subs[i]:
            urls.append(s)

    return urls


def get_urls(domains):
    if len(domains) != 1:
        return start_threads(domains)
    else:
        return send_request(domains[0])
