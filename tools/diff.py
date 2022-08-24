#!/usr/bin/env python3
import sys
import os

def diff(list1, list2):
    for l1 in list1:
        if l1 not in list2:
            print('> '+l1)

    for l2 in list2:
        if l2 not in list1:
            print('< '+l2)


def read_file(path):
    data = ""
    with open(path, 'r', errors="ignore") as f:
        data = f.read()

    return data[:-1].split('\n')


def main():
    list1 = []
    list2 = []

    list1 = read_file(sys.argv[-1])
    list2 = read_file(sys.argv[-2])

    diff(list1, list2)


main()
