#!/bin/bash

massdns -r ~/tools/tools/files/resolvers.txt -t A -o S -w massdns.out $1
cat massdns.out | awk '{print $1}' | sed 's/.$//' | sort -u > alive.txt
cat massdns.out | awk '{print $3}' | sort -u | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" > ips-online.txt
