#!/usr/bin/env python3
import socket
import sys
import os
import time

def connect():
    global conn
    global s

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setblocking(1)
    host = "0.0.0.0"
    port = int(sys.argv[-1])
    s.bind((host,port))
    s.listen(1)
    conn, addr = s.accept()


def recv_data():
    global conn
    global s
    size = int(conn.recv(1024).decode())
    domains = conn.recv(size).decode().split(',')

    conn.close()
    s.close()

    for d in domains:
        print(d)


def main():
    connect()
    recv_data()

try:
    main()
except:
    main()
