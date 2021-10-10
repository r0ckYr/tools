#!/usr/bin/env python3

import sys
import json
import os
import requests
import concurrent.futures
import public


def send_request(domain):
    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
    api_key = {"apikey" : "public.SECURITY_TRAILS_API_KEY"}
    resp = requests.get(url, headers=api_key, timeout=public.TIMEOUT)
    return get_subdomains(resp)


def get_subdomains(resp):
    subdomains = []
    data = json.loads(resp.text)["subdomains"]
    domain = json.loads(resp.text)["endpoint"].split('/')[-2]
    for d in data:
        s = f"{d}.{domain}"
        subdomains.append(s)

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
