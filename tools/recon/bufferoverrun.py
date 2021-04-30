#!/usr/bin/env python3

import sys
import json
import os
import requests
import concurrent.futures
import public


def send_request(domain):
    url = f"https://dns.bufferover.run/dns?q={domain}"
    resp = requests.get(url, timeout=public.TIMEOUT)
    return get_subdomains(resp, domain)


def get_subdomains(resp, domain):
    data = json.loads(resp.text)["FDNS_A"]
    subdomains = []
    ips = []
    for d in data:
        words = d.split(',')
        for w in words:
            if validate_ip(w):
                pass
            else:
                if w not in subdomains and "."+domain in w:
                    subdomains.append(w)

    return subdomains


def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


def start_threads(domains):
    THREADS = public.THREADS
    subdomains = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        subs = list(executor.map(send_request, domains))
        executor.shutdown(wait=True)

    for i in range(0,len(subs)):
        print(str(i))
        for s in subs[i]:
            subdomains.append(s)

    return subdomains


def get_domains(domains):
   if len(domains) != 1:
       return start_threads(domains)
   else:
       return send_request(domains[0])
