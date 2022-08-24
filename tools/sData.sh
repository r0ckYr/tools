#!/usr/bin/bash

cat out/index | grep $1
echo ''
echo 'IPS:----------------------------------------'
echo ''
cat resp | grep $1 | awk '{print $2}' | tr -d '[]' | xargs -I{} sh -c "cat http-result | grep {}"
echo ''
echo 'FUZZED:-------------------------------------'
echo ''
cat httpd | grep -a $1 | xargs -I{} sh -c "echo '    {}'"
