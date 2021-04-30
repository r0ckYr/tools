#!/usr/bin/env python3
import sys
import os


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


def save_to_file(name, lines):
    with open(name, 'w') as f:
        for l in lines:
            f.write(l+'\n')


def split_lines(lines):
    NUMBER_FO_FILES = 4
    length = len(lines)//NUMBER_FO_FILES
    count = 0
    name = 1
    arr = []
    for i in range(0,len(lines)):
        arr.append(lines[i])
        count=count+1
        if count==length and name < NUMBER_FO_FILES:
            save_to_file(str(name), arr)
            count = 0
            arr = []
            name = name+1
        elif count==length and name == NUMBER_FO_FILES:
            for j in range(i+1,len(lines)):
                arr.append(lines[j])

            save_to_file(str(name), arr)
            break
    with open("files", 'w') as f:
        for i in range(1,name+1):
            f.write(str(i)+'\n')


def main():
    if os.path.isfile(sys.argv[-1]):
        lines = read_file(sys.argv[-1])
    else:
        print("[*]Not a file")
        sys.exit()

    split_lines(lines)




main()
