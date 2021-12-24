#!/usr/bin/env python3
import sys


def read_file(path):
    with open(path, 'r') as f:
        data = f.read()

    return data[:-1].split('\n')


def get_intresting(urls):
    numbers = []
    intresting = []
    sorted_numbers = []

    for url in urls:
        if '[' in url:
            data = f"{url.split()[-2]} {url.split()[-1]}"
            numbers.append(data)

    for num in numbers:
        if num not in sorted_numbers:
            sorted_numbers.append(num)

    #print
    for snum in sorted_numbers:
        c = 0
        for num in numbers:
            if snum == num:
                c = c + 1

        if c > 0 and c <=3:
            for url in urls:
                if snum in url and url not in intresting:
                    contentL = url.split()[-1].replace('[','').replace(']','')
                    spaces = ' ' * (12-len(str(contentL)))
                    url = url.replace('\n', '')
                    print(f"{contentL}{spaces}{url[:url.rindex(' ')]}")
                    intresting.append(url)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 uniqlen.py <index>")
        sys.exit()

    urls = read_file(sys.argv[-1])

    get_intresting(urls)


main()
