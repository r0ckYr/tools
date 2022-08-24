#!/usr/bin/env python3
import os
import sys
import json

def main():
    if len(sys.argv) != 1:
        print("Usage: python3 tls-filter.py <json file>")
        sys.exit()

    for line in sys.stdin:
        try:
            line = json.loads(line.strip())
            host = line["host"]
            try:
                cname = line["certificateChain"][0]["subjectCN"]
            except:
                cname = ""
            try:
                subject = line["certificateChain"][0]["subject"]
            except:
                subject = ""

            print(f'{host}, {cname}, {subject}')

        except Exception as e:
            print(str(e))


main()
