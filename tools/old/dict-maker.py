#!/usr/bin/env python3

import sys

def extract_words(line):
    words = line.split('/')
    words2 = []
    exclude = ['com', 'net', 'org']
    for w in words:
        if 'http' not in w and w !='':
            if '.' in w:
                words3 = w.split('.')
                for w3 in words3:
                    if w3 != '' and w3 not in exclude:
                        words2.append(w3)
            else:
                words2.append(w)

    return words2



def main():
    urls = []
    words = []
    words2 = []
    try:
        file_path = sys.argv[-1]
    except:
        print("Usage : python3 dict-maker.py <file containing urls>")
        return

    with open(file_path, 'r') as f:
        while(f.readline() != ''):
            l = f.readline()
            if l!='':
                urls.append(l[0:-1])
    
    for u in urls:
        words1 = extract_words(u)
        for w1 in words1:
            words2.append(w1)

    for w2 in words2:
        if w2 not in words:
            words.append(w2)

    for w in words:
        print(w)

    new_file = file_path.replace('.txt','')+'-dict.txt'
    if '-w' in sys.argv:
        with open(new_file, 'w') as f:
            for w in words:
                f.write(w+'\n')

    print(f"Total words :{len(words)}")



main()
