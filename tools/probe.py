#!/usr/bin/env python3
import sys
import concurrent.futures
import socket

def send_request(host):
    global s
    try:
        s.connect((host, 443))
        print(f"https://{host}")
    except:
        try:
            s.connect((host, 8443))
            print(f"https://{host}")
        except:
            try:
                s.connect((host, 80))
                print(f"http://{host}")
            except:
                try:
                    s.connect((host, 8080))
                    print(f"http://{host}")
                except:
                    pass


def start_threads(domains):
    global THREADS
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(send_request, domains)
        executor.shutdown(wait=True)


def read_file(path):
    with open(path, 'r') as f:
        data = f.read()

    return data[:-1].split('\n')


def main():
    global THREADS
    global s

    THREADS = 20
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    domains_file = sys.argv[-1]
    domains = read_file(domains_file)

    start_threads(domains)


main()
