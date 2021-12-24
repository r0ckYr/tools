#!/usr/bin/env python3
import socket
import sys
import os
import time

def make_connection():
    # make socket object
    global s
    host = sys.argv[-2].split(':')[0]
    port = int(sys.argv[-2].split(':')[1])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #connect to the server
    try:
        s.connect((host, port))
    except socket.error:
        time.sleep(3)
        make_connection()


def send_data(data):
    global s
    s.send(str(len(data.encode())).encode())
    time.sleep(3)
    s.send(data.encode())
    s.close()


def read_file(file_path):
    with open(file_path, 'r') as f:
        DOMAINS = f.readlines()

    for i in range(0, len(DOMAINS)):
        DOMAINS[i] = str(DOMAINS[i][:len(DOMAINS[i])-1])

    while('' in DOMAINS):
        DOMAINS.remove('')

    domains = []
    for d in DOMAINS:
        if d not in domains:
            domains.append(d)

    return domains


def main():
    domains = read_file(sys.argv[-1])
    data = ""
    for d in domains:
        data = data + d +','
    make_connection()
    send_data(data[:len(data)-1])


try:
    main()
except:
    main()
