#!/usr/bin/env python3
import sys
import os


def read_file(file_path):
    data = ""
    with open(file_path, 'r', encoding="utf8", errors='ignore') as f:
        data = f.read()

    return data[:-1].split('\n')


def save_to_file(name, lines):
    with open(name, 'w', encoding="utf8", errors='ignore') as f:
        for l in lines:
            f.write(l+'\n')


def split_lines(lines):
    NUMBER_FO_FILES = int(sys.argv[-2])
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
    if len(sys.argv) == 3:
        if os.path.isfile(sys.argv[-1]):
            lines = read_file(sys.argv[-1])
        else:
            print("[*]Not a file")
            sys.exit()

        split_lines(lines)

    else:
        print("Usage: ./splitter.py <number of files> <file>\nExample: ./splitter.py 4 domains.txt")
        sys.exit()


main()
