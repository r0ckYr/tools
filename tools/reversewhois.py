#!/usr/bin/env python3
import sys
import requests
from bs4 import BeautifulSoup
import re

def send_request(query):
    url = f"https://www.reversewhois.io/?searchterm={query}"
    resp = requests.get(url, timeout=40)
    return resp.text


def get_domains(page):
    soup = BeautifulSoup(page, 'html.parser')
    tables = str(soup.findAll('td')).split(',')
    for table in tables:
        table = table.replace('<td>','')
        table = table.replace('</td>','')
        table = table.replace(' ','')
        if '.' in table and isValidDomain(table) and '/' not in table and '[' not in table and ']' not in table:
            print(table)


def isValidDomain(str):

    regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"

    p = re.compile(regex)

    if (str == None):
        return False

    if(re.search(p, str)):
        return True
    else:
        return False



def main():
    if len(sys.argv) != 2:
        print("Usage: ./reversewhois.py <key>")
        sys.exit()
    page = send_request(sys.argv[-1])
    get_domains(page)


try:
    main()
except Exception as e:
    print("Usage: ./reversewhois.py <key>")
    print('\n'+str(e))
