#!/usr/bin/env python3
import sys
import requests
import concurrent.futures
import os
import socket


def is_alive(domain):
    global alive_domains
    global current
    global total_req
    spacing = " "*(80)
    try:
        domain = domain.replace("https://", '')
        r = socket.gethostbyname(domain)
        print(f"\r{domain}{spacing}")
        alive_domains.append(domain)
    except:
        try:
            domain = domain.replace("http://", '')
            r = socket.gethostbyname(domain)
            print(f"\r{domain}{spacing}")
            alive_domains.append(domain)
        except:
            pass

    current = current + 1
    printProgressBar(current, total_req, prefix = 'Progress:', suffix = 'Complete', length = 50)


def read_file(file_path):
    with open(file_path, 'r') as f:
        DOMAINS = f.readlines()

    for i in range(0, len(DOMAINS)):
        DOMAINS[i] = str(DOMAINS[i][:len(DOMAINS[i])-1])

    while('' in DOMAINS):
        DOMAINS.remove('')

    return DOMAINS


def make_list(domain, resolvers):
    domains = []
    for r in resolvers:
        domains.append(f"{r}.{domain}")

    return domains


def start_threads(domains):
    global THREADS

    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(is_alive, domains)



def start_bruteforcer(root_domains, resolvers):
    domains = []
    print("\n")
    for rd in root_domains:
        domains = make_list(rd, resolvers)
        start_threads(domains)


def print_error(e):
    print("\nUsage :./bruteforcer.py -d <domain or file>\n\n   -w : wordlist for resolvers\n   -o : write to a file\n   -t : Number of threads\n   -r : recursive\n\n"+e+'\n')
    sys.exit()


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 2, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def main():
    global alive_domains
    global THREADS
    global total_req
    global current
    current = 0
    THREADS = 10
    alive_domains = []
    root_domains = []
    resolvers = []
    domains = []

    if len(sys.argv) >= 3:
        if '-d' not in sys.argv:
            print_error("[*]Domain not specified !")

        print("[*]Starting script........")

        try:
            domains_file = sys.argv[sys.argv.index('-d')+1]
            if '-w' in sys.argv:
                rs_file = sys.argv[sys.argv.index('-w')+1]
                if os.path.isfile(rs_file) == False:
                    print_error("[*]Wordlist does not exists")
            else:
                rs_file = "/home/rocky/tools/tools/files/subdomains-top1million-5000.txt"

            if '-t' in sys.argv:
                THREADS = int(sys.argv[sys.argv.index('-t')+1])

            if '-o' in sys.argv:
                write_to = sys.argv[sys.argv.index('-o')+1]

            if os.path.isfile(domains_file):
                root_domains = read_file(domains_file)
                resolvers = read_file(rs_file)
            else:
                if '.' in domains_file:
                    root_domains.append(domains_file)
                    resolvers = read_file(rs_file)
                else:
                    print_error("[*]Not a domain !")

        except Exception as e:
            print_error(str(e))
    else:
        print_error("")

    total_req = len(resolvers)*len(root_domains)
    print(f"\n[*]Wordlist : {rs_file}   Length : {len(resolvers)}   Total : {total_req}   Threads : {THREADS}\n")
    print("[*]Starting bruteforcer.......")


    start_bruteforcer(root_domains, resolvers)


    if '-r' in sys.argv:
        start_bruteforcer(alive_domains, resolvers)

    for ad in alive_domains:
        if ad not in domains:
            domains.append(ad)

    if '-o' in sys.argv:
        with open(write_to, 'w') as f:
            for d in domains:
                f.write(d+'\n')

    print("\n")


main()
