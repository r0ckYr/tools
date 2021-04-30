#!/usr/bin/env python3

import concurrent.futures
import requests
import json
import sys
import os
import public


def send_request(domain):
    domains = []
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    resp = requests.get(url, timeout=public.CRTSH_TIMEOUT)
    return get_subdomains(resp)


def get_subdomains(resp):
    data = json.loads(resp.text)
    domains = []
    for key in data:
        subdomain = key["common_name"]
        if "*" not in subdomain and subdomain not in domains and subdomain:
            domains.append(subdomain)
        subdomain = key["name_value"]
        if "*" not in subdomain and subdomain not in domains and subdomain:
            domains.append(subdomain)

    subs = split_line_break(domains)
    subdomains = []
    for d in subs:
        if " " not in d and "," not in d and d not in subdomains:
            subdomains.append(d)

    return subdomains


def split_line_break(domains):
    if len(domains) > 0:
        for d in domains:
            if '\n' in d:
                temp = d.split('\n')
                domains.remove(d)
                for t in temp:
                    domains.append(t)
    return domains


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
