#!/usr/bin/env python3
import requests
import sys
import os
import concurrent.futures
import jsbeautifier
import config

def get_file(url):
    global session
    try:
        resp = session.get(url)

        print(f"{url} ({resp.status_code}) [{len(resp.text)}]")

        #if resp.status_code == 200:
         #   url = filter_url(url)
          #  with open(url, 'w') as f:
           #     f.write(resp.text)

    except Exception as e:
        print(f"{url} : {e}")


def filter_url(url):
    if 'https' in url:
        url = url.replace('https://', '')
    elif 'http' in url:
        url = url.replace('http://', '')
    url = url.replace('/', '_')
    url = url.replace('*', '_')
    url = url.replace('%', '_')
    url = url.replace('!', '_')
    url = url.replace('?', '_')
    url = url.replace('&', '_')
    url = url.replace('"', '_')
    url = url.replace("'", '_')
    url = url.replace('~', '_')
    url = url.replace(';', '_')
    url = url.replace('\\', '_')
    url = url.replace('#', '_')
    url = url.replace('$', '_')
    url = url.replace('^', '_')
    url = url.replace('(', '_')
    url = url.replace(')', '_')
    url = url.replace('+', '_')
    url = url.replace('=', '_')
    url = url.replace('`', '_')
    url = url.replace(' ', '_')

    if len(url) > 210:
        url = url[:210]

    if not (url.endswith(".js")):
        url = url + ".js"

    return url


def start_threads(urls):
    THREADS = config.THREADS
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(get_file, urls)


def read_file(file_path):
    with open(file_path, 'r') as f:
        URLS = f.readlines()

    for i in range(0, len(URLS)):
         URLS[i] = str(URLS[i][:len(URLS[i])-1])

    while('' in URLS):
        URLS.remove('')

    urls = []
    for d in URLS:
        if d not in urls and 'googleapis' not in d:
            urls.append(d)

    return urls


def main():
    global session

    session = requests.Session()
    requests.packages.urllib3.disable_warnings()
    session.allow_redirects = False
    session.verify = False
    session.timeout = 5
    session.headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
    session.stream = True
    if len(sys.argv) < 2:
        print("\n[*]No input\n")
        sys.exit()

    urls = []
    urls_file = sys.argv[-1]
    if os.path.isfile(urls_file):
        urls = read_file(urls_file)
    else:
        if 'http' in urls_file and '.js' in urls_file and 'googleapis' not in urls_file:
            urls.append(urls_file)
        else:
            print("\n[*]Invalid path!\n")
            sys.exit()

    try:
        os.mkdir("scripts")
    except Exception as e:
        print(str(e)+'\n[*]Overwriting directory')

    os.chdir("scripts/")

    start_threads(urls)


main()
