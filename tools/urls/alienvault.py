#!/usr/bin/env python3

import sys
import json
import os
import requests
import concurrent.futures


def send_request(domain):
    url = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/url_list"
    api_key = {"X-OTX-API-KEY": "16b594d32bc00b10a1a893a99beb2a9fb80caefe27e01796998c10790a4a29eb"}
    resp = requests.get(url, headers=api_key, timeout=(2,5))
    return get_urls_list(resp)


def get_urls_list(resp):
    urls = []
    data = json.loads(resp.text)["url_list"]
    for d in data:
        if d["url"] not in urls:
            urls.append(d["url"])
    return urls


def start_threads(domains):
    THREADS = 4
    urls = []
    subs = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        subs = list(executor.map(send_request, domains))

    for i in range(0, len(subs)):
        for s in subs[i]:
            urls.append(s)

    return urls


def get_urls(domains):
    if len(domains) != 1:
        return start_threads(domains)
    else:
        return send_request(domains[0])
