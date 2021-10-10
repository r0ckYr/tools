#!/usr/bin/env python3
import sys


def read_file(path):
    with open(path, 'r') as f:
        data = f.read()

    return data[:-1].split('\n')


def extract_numbers(urls):
    numbers = []
    for url in urls:
        if '[' in url:
            numbers.append(int(url.split()[-1].replace('[', '').replace(']', '')))

    return numbers


def get_intresting(numbers, sorted_numbers, urls):
    intresting = []
    c = 0
    for num in sorted_numbers:
        c = 0
        for n in numbers:
            if num == n:
                c = c+1

        if c == 2 or c == 1:
            for url in urls:
                if f"[{str(num)}]" in url and 'http' in url and url not in intresting:
                    intresting.append(url)
                    spaces = ' ' * (12-len(str(num)))
                    print(f'{str(num)}{spaces}{url}')


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 uniqlen.py <index>")
        sys.exit()

    urls = read_file(sys.argv[-1])

    numbers = extract_numbers(urls)

    sorted_numbers = []
    for num in numbers:
        if num not in sorted_numbers:
            sorted_numbers.append(num)

    get_intresting(numbers, sorted_numbers, urls)

main()
