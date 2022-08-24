#!/usr/bin/env python3
import sys
import os
import subprocess
import requests
import urllib3
import concurrent.futures

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_result(url):
    global temp_file
    r = None

    try:
        r = requests.get(url, verify=False, timeout=10, allow_redirects=False)
    except Exception as w:
        pass

    if(r):
        if os.path.exists(temp_file):
            os.remove(temp_file)
        with open(temp_file, 'w') as f:
            f.write(r.text)
        cmd = f"confused {temp_file} | grep -vaE 'repositories|@|\[W\]' | sed '/^[[:space:]]*$/d'"
        try:
            run = subprocess.run(cmd, shell=True, text=True, capture_output=True)
            result =  run.stdout+run.stderr
            if(len(result)>0):
                print(url+"\n    "+str(result)+"\n")
        except Exception as e:
            pass


def read_file(path):
    with open(path, "r", encoding="utf8", errors="ignore") as f:
        data = f.read()

    return data[:-1].split("\n")


def main():
    global temp_file
    temp_file = 'package.json'

    if len(sys.argv) != 2:
        print("Usage: python3 confusion.py <input file>")
        sys.exit()

    if not os.path.isfile(sys.argv[-1]):
        print("[*]Not a valid file")
        print("Usage: python3 confusion.py <input file>")
        sys.exit()

    lines = read_file(sys.argv[-1])

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(get_result, lines)


main()
