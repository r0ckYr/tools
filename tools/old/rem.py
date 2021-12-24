#!/usr/bin/env python3
import sys
import os

if os.path.isfile(sys.argv[-1]):
    with open(sys.argv[-1], 'r') as f:
        while(f.readline() != ''):
            line = f.readline()
            if '/' not in line and len(line) > 20:
                continue
            print(line, end='')

else:
    print("not a file")
