#!/usr/bin/env python3
import sys
import os
from fingerprints import *
import requests
import concurrent.futures
import dns.resolver
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

def enumCNAME(domain):
    cname = ""

    domain_without_protocal = domain.replace("http://", "")
    domain_without_protocal = domain_without_protocal.replace("https://", "")

    try:
        result = dns.resolver.resolve(domain_without_protocal, 'CNAME')
        for cnameeval in result:
            cname = cnameeval.target.to_text()
    except Exception:
        pass

    return cname


def confirm_vulnerable(domain, service_cname_list):
    confirm = False

    enumeratedCNAME = enumCNAME(domain)
    if enumeratedCNAME == "":  # Because URL such as https://githublol.github.io (which doesn't exist) will have CNAME==""
        confirm = "NotSure"

    else:
        for service_cname in service_cname_list:
            if service_cname in enumeratedCNAME:
                confirm = True

    return confirm, enumeratedCNAME


def testTarget(url):
    not_success = True
    global TIMEOUT

    try:
        response = requests.get(url, headers=headers, timeout=TIMEOUT, verify=False, allow_redirects=False)
        targetResponse = response.text
    except:
        pass

    for fingerprint in fingerprints_list:
        error = fingerprint[3]

        if error.lower() in targetResponse.lower():
            if error.lower() == "":
                pass

            else:
                service_cname_list = fingerprint[2]
                confirm, enumeratedCNAME = confirm_vulnerable(url, service_cname_list)
                if confirm == True:
                    print(f"{fingerprint[1]} ===> : [Service: {fingerprint[0]}] [CNAME: {enumeratedCNAME}] : {url}")
                    not_success = False

                elif confirm == "NotSure" and fingerprint[0] not in ["CargoCollective", "Akamai"]:
                    #CargoCollective & Akamai fingerprints can leads to False +ve
                    #If script is unable to confirm detection using CNAME, then we will ignore that detection

                    print(f"[+] {fingerprint[1]} ===> : [Service: {fingerprint[0]}] [CNAME: 404, UnableToVerify-CouldBeFalsePositive] : {url}")
                    not_success = False

#    if not_success:
 #       print(f"{Fore.WHITE}[-] Not Vulnerable  : {Fore.GREEN}{url}{Fore.WHITE}")


def start(domains):
    global THREADS
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(testTarget, domains)


def read_file(path):
    with open(path, "r", encoding="utf8", errors="ignore") as f:
        data = f.read()

    return data[:-1].split("\n")


def main():
    global THREADS
    global TIMEOUT

    THREADS = 50
    TIMEOUT = 5

    if len(sys.argv) != 2:
        print("Usage: python3 takeover.py <input file>")
        sys.exit()

    if not os.path.isfile(sys.argv[-1]):
        print("[*]Not a valid file")
        print("Usage: python3 takeover.py <input file>")
        sys.exit()

    lines = read_file(sys.argv[-1])
    start(lines)


main()
