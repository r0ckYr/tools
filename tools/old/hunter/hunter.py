#!/usr/bin/env python3
import sys
import requests
import os
import concurrent.futures
import config
import subprocess
from bs4 import BeautifulSoup
import urllib3

def send_request(domain):
    session = requests.Session()
    session.max_redirects = 30
    session.headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
    requests.packages.urllib3.disable_warnings()
    try:
        r = session.get(domain, timeout=(15,60), verify=False)
        return r
    except Exception as e:
        if 'Max retries exceeded with url' in str(e) or 'Read timed out' in str(e):
            try:
                r = requests.get(domain, timeout=(15,60), verify=False)
                return r
            except:
                pass
        print(f"{domain} : {e}")
        with open('errors', 'a') as f:
            f.write(domain+'\n')
        return None


def get_title(resp):
    soup = BeautifulSoup(resp.text, 'html.parser')
    for title in soup.find_all('title'):
        return title.get_text()


def save_response(resp, domain):
    #index file
    global js_files
    with open('index', 'a') as f:
        title = get_title(resp)
        if title:
            title = title.replace('\n', ' ')
            f.write(f"{domain} {title} ({str(resp.status_code)}) [{len(resp.text)}]\n")
        else:
            f.write(f"{domain} ({resp.status_code}) [{len(resp.text)}]\n")

    #js files
    with open('jsfiles', 'a') as f:
        scripts = get_js_files(resp, domain)
        for s in scripts:
            if s not in js_files and '.js' in s:
                js_files.append(s)
                f.write(s+'\n')

    #html
    if 'https' in domain:
        domain = domain.replace('https://', '')
    else:
        domain = domain.replace('http://', '')
        if os.path.isfile(f'text/{domain}'):
            domain = domain + ":80"

    domain = domain.replace('/', '')
    with open(f'text/{domain}', 'w') as f:
        f.write(resp.text)

    with open(f'headers/{domain}', 'w') as f:
        for h in resp.headers:
            f.write(f"{h}: {resp.headers[h]}\n")


def get_js_files(resp, url):
    script_files = []
    soup = BeautifulSoup(resp.text, 'html.parser')
    for script in soup.find_all('script'):
        name = script.attrs.get('src')
        if name is not None:
            if 'http' in name:
                script_files.append(name)
            else:
                if name[0] == '/':
                    name = name[1:]
                    if name[0] == '/':
                        name = name[1:]

                script_files.append(url+'/'+name)
    return script_files


def read_file(file_path):
    with open(file_path, 'r') as f:
        DOMAINS = f.read()

    return DOMAINS[:-1].split('\n')


def start_threads(domains):
    THREADS = config.THREADS
    if '-t' in sys.argv:
        index = sys.argv.index('-t')+1
        THREADS = int(sys.argv[index])
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(start, domains)
        executor.shutdown(wait=True)


def start(domain):
    try:
        resp = send_request(domain)
        if resp is not None:
            save_response(resp, domain)
    except Exception as e:
        print(e)


def main():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    DOMAINS = []
    domains_file = sys.argv[-1]
    global js_files
    js_files = []

    if len(sys.argv) < 2:
        sys.exit()
    if os.path.isfile(domains_file):
        DOMAINS = read_file(sys.argv[-1])
    else:
        if "." in domains_file:
            DOMAINS.append(domains_file)
        else:
            print("[*]Invalid domain or file!")
            sys.exit()

    try:
        os.mkdir("out")
        os.chdir("out/")
        os.mkdir("text")
        os.mkdir("headers")
    except Exception as e:
        print(f"\n{e}\n[*]please remove the directory!")
        sys.exit()
    start_threads(DOMAINS)


try:
    main()
except Exception as e:
    print(e)
