#!/usr/bin/env python3
import sys
import os

THREADS = 10

def read_file(file_path):

    with open(file_path, 'r') as f:
        LINES = f.readlines()


    for i in range(0, len(LINES)):
        LINES[i] = str(LINES[i][:len(LINES[i])-1])

    while('' in LINES):
        LINES.remove('')

    lines = []
    for d in LINES:
        if d not in lines:
            lines.append(d)

    return lines


def is_valid(s):
    chars = " ,!@#$%^&*()_-+={}[]|:;'<,>.?/"
    c = 0
    for char in chars:
        if char in s:
            c = c+1

    if c > 5:
        return False
    else:
        return True


def contains_alphabet(s):
    chars = "QWERTYUIOPASDFGHJKLZXCVBNM"
    for char in chars:
        if char in s:
            return True
    return False


def get_strings(LINES):
    add = False
    temp = ""
    for line in LINES:
        for char in line:
            if add:
                if char == '"':
                    temp = temp.replace('"', '')
                    if len(temp) > 1 and is_valid(temp) and contains_alphabet(temp):
                        print(temp)
                    temp = ""
                    add = False

                temp = temp + char
            else:
                if char=='"':
                    add=True


def main():
    if len(sys.argv) != 2 or os.path.isfile(sys.argv[-1])==False:
        print("[*]Invalid!")
        sys.exit()

    LINES = read_file(sys.argv[-1])
    get_strings(LINES)


main()
