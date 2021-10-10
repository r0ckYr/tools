#!/usr/bin/env python3

import sys
import json
import os
import requests
import concurrent.futures
import public


def send_request(domain):
    url = f"https://api.certspotter.com/v1/issuances?domain={domain}&include_subdomains=true&expand=dns_names"
    api_key = {"Authorization": "Bearer {public.CERTSPOTTER_TOKEN}"}
    resp = requests.get(url, headers=api_key, timeout=public.TIMEOUT)
    return get_subdomains(resp)


def get_subdomains(resp):
    subdomains = []
    data = resp.text.split(',')
    for i in range(1,len(data)):
        d = data[i]

        sub = get_list(d).replace('"', '')

        if sub != None and sub != '':
            if '*' in sub:
                sub = sub.replace('*.', '')

            if ',' in sub:
                subs = sub.split(',')
                for s in subs:
                    subdomains.append()
            else:
                subdomains.append(sub)

    return subdomains


def get_list(string):
    temp = ""
    add = False
    for s in string:
        if s == '[':
            add = True
            continue
        if s == ']':
            return temp
        if add:
            temp = temp+s
    return temp

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
