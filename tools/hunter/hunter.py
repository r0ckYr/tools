#!/usr/bin/env python3
import sys
import requests
import os
import re
import concurrent.futures
import subprocess
from bs4 import BeautifulSoup
import urllib3
import socket
from fingerprints import *


def send_request(domain):
    global session
    global REDIRECT
    global TIMEOUT
    try:
        if ':' in domain:
            host = domain[:int(domain.index(':'))]
        else:
            host = domain
        socket.gethostbyname_ex(host)
    except Exception as e:
        return None

    try:
        domain = "https://"+domain
        r = session.get(domain, allow_redirects=REDIRECT, timeout=TIMEOUT)
        print(domain)
        return r
    except Exception as e:
        domain = domain.replace('https://', '')
        try:
            domain = "http://"+domain
            r = session.get(domain, allow_redirects=REDIRECT, timeout=TIMEOUT)
            print(domain)
            return r
        except:
            pass

        with open('errors', 'a') as f:
            f.write(domain+'\n')
        return None


def get_title(resp):
    soup = BeautifulSoup(resp.text, 'html.parser')
    for title in soup.find_all('title'):
        return title.get_text()


def save_response(resp):
    #index file
    global js_files
    global SAVE

    if resp.history:
        domain = resp.history[0].url[:-1]
    else:
        domain = resp.url[:-1]

    with open('index', 'a') as f:
        title = get_title(resp)
        if title is not None:
            title = title.replace('\n', ' ')
            f.write(f"{domain} {title} ({str(resp.status_code)}) [{len(resp.text)}]\n")
        else:
            f.write(f"{domain} ({resp.status_code}) [{len(resp.text)}]\n")

    #js files
    with open('jsfiles', 'a') as f:
        scripts = get_js_files(resp, domain)
        for script in scripts:
            if script not in js_files and '.js' in script:
                js_files.append(script)
                f.write(script+'\n')

    #html
    if SAVE:
        if 'https' in domain:
            domain = domain.replace('https://', '')
        else:
            domain = domain.replace('http://', '')
            if os.path.isfile(f'text/{domain}'):
                if ':' not in domain:
                    domain = domain + ":80"

        domain = domain.replace('/', '')
        with open(f'text/{domain}', 'w') as f:
            f.write(resp.text)

        with open(f'headers/{domain}', 'w') as f:
            for h in resp.headers:
                f.write(f"{h}: {resp.headers[h]}\n")

def add_takeover(resp):
    if resp.history:
        domain = resp.history[0].url[:-1]
    else:
        domain = resp.url[:-1]
    with open("vulns/takeover", 'a') as f:
        f.write(domain+'\n')


def isValidDomain(sub):
    regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"

    p = re.compile(regex)
    if '.' not in sub:
        return False

    if (sub == None):
        return False

    if '.js' in sub:
        return False

    if(re.search(p, sub)):
        return True
    else:
        return False


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
                        if name[0] == '/':
                            name = name[1:]
                script_files.append(url+'/'+name)

    return script_files


def read_file(file_path):
    with open(file_path, 'r') as f:
        DOMAINS = f.read()

    return DOMAINS[:-1].split('\n')


def start_threads(domains):
    global THREADS
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(start, domains)
        executor.shutdown(wait=True)


def start(domain):
    global TAKEOVERS
    try:
        resp = send_request(domain)
        if resp is not None:
            if resp.status_code == 404 and TAKEOVERS:
                if check_sto(resp.text):
                    add_takeover(resp)
            save_response(resp)
    except Exception as e:
        print(e)


def usage():
    print("Usage: python3 hunter.py -t 20 -timeout 10 domains.txt")
    print('''
arguments:
    -h             Prints help information
    -t             Number of threads (default 20)
    -p             ports range (eg., 80,8443,443,8080)
    -timeout       Timeout in seconds (default 10)
    --no-redirect  Don't allow redirects (default true)
    --no-save      Don't save response (defatult true)
    --takeovers    Checks for subdomain takeovers (default false)
          ''')
    sys.exit()


def parse_arguments():
    global THREADS
    global TIMEOUT
    global PORTS
    global REDIRECT
    global SAVE
    global TAKEOVERS

    if '-t' in sys.argv:
        try:
            THREADS = int(sys.argv[sys.argv.index('-t')+1])
        except:
            print('\n[*]Invalid value for threads !')
            usage()

    if '-timeout' in sys.argv:
        try:
            TIMEOUT = int(sys.argv[sys.argv.index('-timeout')+1])
        except:
            print('\n[*]Invalid value for timeout !')
            usage()


    if '-p' in sys.argv:
        PORTS = sys.argv[sys.argv.index('-p')+1].split(',')
        try:
            for i in range(0,len(PORTS)):
                PORTS[i] = int(PORTS[i])
        except:
            print('\n[*]Please specify ports correctly !')
            usage()

    if '--no-save' in sys.argv:
        SAVE = False

    if '--no-redirect' in sys.argv:
        REDIRECT = False

    if '--takeovers' in sys.argv:
        TAKEOVERS = True



def check_sto(data):
    if data == "" or data is None:
        return False

    for fingerprint in fingerprints_list:
        error = fingerprint[3]
        if error.lower() in data.lower():
            return True

    return False


def test():
    global session
    global THREADS
    global TIMEOUT
    global PORTS
    global REDIRECT
    global js_files
    global SAVE
    print(str(THREADS) + ' ' + str(TIMEOUT) + ' ' + str(PORTS) + ' ' + str(REDIRECT) + ' ' + str(SAVE))
    print(sys.argv)


def add_ports(DOMAINS):
    global PORTS
    domains = []

    for domain in DOMAINS:
        domains.append(domain)
        for port in PORTS:
            if port == 443 or port == 80:
                continue
            domains.append(domain+':'+str(port))

    return domains


def main():
    global session
    global THREADS
    global TIMEOUT
    global PORTS
    global REDIRECT
    global js_files
    global SAVE
    global TAKEOVERS

    if '-h' in sys.argv:
        usage()

    REDIRECT = True
    TIMEOUT = 5
    THREADS = 20
    PORTS = []
    SAVE= True
    DOMAINS = []
    domains_file = sys.argv[-1]
    js_files = []
    TAKEOVERS = False

    if len(sys.argv) < 2:
        usage()

    if os.path.isfile(domains_file):
        DOMAINS = read_file(sys.argv[-1])
    else:
        if "." in domains_file:
            DOMAINS.append(domains_file)
        else:
            print("[*]Invalid domain or file!")
            usage()

    #parse arguments
    parse_arguments()


    #foramt url for http/https
    for i in range(len(DOMAINS)):
        DOMAINS[i] = DOMAINS[i].replace("https://", '')
        DOMAINS[i] = DOMAINS[i].replace("http://", '')

    if len(PORTS) != 0:
        DOMAINS = add_ports(DOMAINS)

    #requests object
    session = requests.Session()
    session.max_redirects = 30
    session.headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
    session.verify = False
    session.timeout = TIMEOUT
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    try:
        os.mkdir("out")
        os.chdir("out/")
        if SAVE:
            os.mkdir("text")
            os.mkdir("headers")
            os.mkdir("vulns")
    except Exception as e:
        print(f"\n{e}\n[*]please remove the directory!")
        sys.exit()

    start_threads(DOMAINS)


try:
    main()
except Exception as e:
    Gprint(e)
