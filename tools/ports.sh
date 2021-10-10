#!/bin/bash

for i in $(cat ip_addresses)
do
    echo "--------------------------------------("$i")----------------------------------------"
    cat masscan-all-ports | grep $i | awk '{print $NF}' | awk -F'/' '{print $1}' | sort -u
    echo ''
done
