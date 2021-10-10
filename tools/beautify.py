#!/usr/bin/env python3
import jsbeautifier
import sys
import os

data = ""
if len(sys.argv) != 2:
    print("give a file")
    sys.exit()
fil = sys.argv[-1]
with open(fil, 'r') as f:
    data = f.read()

text = jsbeautifier.beautify(data)

if not fil.endswith('.js'):
    os.remove(fil)
    fil = fil.replace('.txt', '')
    if not fil.endswith('.js'):
        fil = fil + '.js'

print(fil)
with open(fil, 'w') as f:
    f.write(text)

