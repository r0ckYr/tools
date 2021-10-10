#!/usr/bin/env python3

import sys
import json
import os
import requests
import concurrent.futures
import public


def send_request(domain):
    url = f"https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}"
    resp = requests.get(url, timeout=public.TIMEOUT)
    return get_subdomains(resp)


def get_subdomains(resp):
    subdomains = json.loads(resp.text)["subdomains"]
    return subdomains


def start_threads(domains):
    THREADS = public.THREADS
    subdomains = []
    subs = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        subs = list(executor.map(send_request, domains))
        executor.shutdown(wait=True)

    for i in range(0, len(subs)):
        for s in subs[i]:
            subdomains.append(s)

    return subdomains


def get_domains(domains):
    if len(domains) != 1:
        return start_threads(domains)
    else:
        return send_request(domains[0])

