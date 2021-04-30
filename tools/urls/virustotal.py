#!/usr/bin/env python3

import sys
import json
import os
import requests
import concurrent.futures


def send_request(domain):
    url = f"https://www.virustotal.com/vtapi/v2/domain/report?domain={domain}&apikey=8481e812a65fbcf355a05e86fb0c90ea18d5a0a0e9ddf9bc4ab4102288d07d9c"
    resp = requests.get(url, timeout=(2,10))
    return get_urls_list(resp)


def get_urls_list(resp):
    urls = []
    urls1 = json.loads(resp.text)["undetected_urls"]
    urls2 = json.loads(resp.text)["detected_urls"]

    for u1 in urls1:
        urls.append(u1[0])
    for u2 in urls2:
        urls.append(u2["url"])

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
