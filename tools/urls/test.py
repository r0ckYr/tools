#!/usr/bin/env python3
import sys
import requests
import json

def send_request(domain):
    url = f"http://index.commoncrawl.org/CC-MAIN-2018-22-index?url={domain}/*&output=json"
    resp = requests.get(url, timeout=(2,20))
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


def main():
    domain = sys.argv[-1]
    data = send_request(domain)
    print(data)


main()
