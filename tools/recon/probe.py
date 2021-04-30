#!/usr/bin/env python3
import requests
import sys
import concurrent.futures


def send_request(url):
    try:
        r = requests.head(url, timeout=1)
        return url
    except Exception as e:
        return None


def start_threads(domains):
    THREADS = 4
    urls = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        results = list(executor.map(send_request, domains))
        executor.shutdown(wait=True)

    for r in results:
        if r is not None:
            urls.append(r)

    return urls


def get_alive(domains):
    urls = []
    for d in domains:
        urls.append("https://"+d)
        urls.append("http://"+d)
    return start_threads(urls)
