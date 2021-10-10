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
    cat $1 | awk '{print $NF"    "$1}' | grep http | tr -d '[]' | sort -n | vi -
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
	cd '/home/rocky/tools/Burp/Burp Suite Professional Edition v2021.8.3'
	java -noverify -javaagent:Dr.FarFar.jar -jar burpsuite_pro_v2021.8.3.jar & exit
}
getroot(){
	cat $1 | rev | cut -d "." -f 1,2 | rev | sort -u | tee -a root-$1
}
getintresting(){
	words=("uat" "test" "prod" "admin" "stag" "jenkins" "jankins" "jire" "jira" "smal" "auth" "outh")
	for i in "${words[@]}"
	do
		cat $1 | grep $i
	done | sort -u | tee -a potential-$1
}
server(){
    python3 -m http.server $1
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
    cat $1 | xargs -n1 -I{} sh -c "cat $2 | grep {} | shuffledns -d {} -r ~/tools/tools/files/resolvers.txt -silent" | tee -a $3
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
	sudo nmap -T4 -Pn -v -sC $1
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
    cat $1 | xargs -n1 -P2 -I{} sh -c "amass enum -passive -nolocaldb -nocolor -config ~/tools/amass/config.ini -d {}" | anew domains

    #findomain
	cat $1 | xargs -n1 -P4 -I{} findomain -q -t {} | anew domains

    #clean domains
    sanitizer.py $1 domains | sort -u > t
    rm domains
    mv t domains

    #get third-level-domains
    3levels.py domains > third-level-domains

    #recon on third-level-domains
    cat third-level-domains | xargs -n1 -P10 -I{} recon.py {} | anew domains
	cat third-level-domains | xargs -n1 -P10 -I{} findomain -q -t {} | anew domains
    cat third-level-domains | xargs -n1 -P10 -I{} subfinder -silent -d {} | anew domains
    cat third-level-domains | xargs -n1 -P2 -I{} sh -c "amass enum -passive -nolocaldb -nocolor -config ~/tools/amass/config.ini -d {}" | anew domains
    
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
    grep -Hnr -E 'AIza[0-9A-Za-z_-]{35}|AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}|EAACEdEose0cBA[0-9A-Za-z]+'
}
rlist(){
    cat $1 | xargs -n1 -P4 -I{} recon.py {}
}
am(){
    cat $1 | xargs -n1 -P3 -I{} amass enum -passive -nocolor -nolocaldb -config ~/tools/amass/config.ini -d {}
}
takeover(){
    cd ~/tools/SubOver/
    SubOver -t 100 -l $1
    cd -
}
param(){
    arjun -u $1 -w ~/tools/tools/files/parameters.txt $2 $3 
}
fuzz(){
    for i in $(cat $1)
    do
        python3 ~/tools/dirsearch/dirsearch.py -u $i -w /home/rocky/tools/tools/files/dict.txt -t 200 --no-color -q -H 'X-Forwarded-For: 127.0.0.1' --skip-on-status 429 -r -R 3
    done | tee -a directories
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
    #clean domains
    sanitizer.py root domains | sort -u > t
    rm domains
    mv t domains

    #get bruteable domains
    bruteable.py 4 domains | rev | cut -d '.' -f1,2,3,4 | rev | sort -u > to-brute #bruteforce these later
    
    #get alive
    cat domains | dnsx -resp -o resp -silent
    cat resp | awk '{print $1}' | sort -u > dns
    cat resp | awk '{print $2}' | tr -d '[]' | sort -u > ip_addresses

    #get active domains
    cat domains | httpx -silent -o active-domains

    #get data on active domains
    hunter.py active-domains

    #jshunter on jsfiles
    cd out/
    jshunter jsfiles
    cd ..

    #wayback machine
    urls active-domains
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
    ssh -i "~/tools/server/reconpad.pem" ubuntu@35.154.79.99
}
checkey(){
    cat ~/bounty/maps-urls | sed "s/KEY_HERE/$1/g"
}
sdns(){
    shuffledns -d $1 -w $2 -r ~/tools/tools/files/resolvers.txt -strict-wildcard -silent
}
sendr(){
    scp -i "~/tools/server/reconpad.pem" $1 ubuntu@35.154.79.99:/home/ubuntu/$2
}
recvr(){
    scp -i "~/tools/server/reconpad.pem" ubuntu@35.154.79.99:/home/ubuntu/$1 $2
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
        cat $1 | grep '=' | grep -vE "\.(gif|jpeg|css|tif|tiff|png|woff|jpg|ico|pdf|svg|txt|js)" | uro | sort -u | kxss | tee -a $2 
    fi
}
sqli(){
    if [ $# != 2 ]
    then
        echo "need two arguments"
    else
        cat $1 | grep -iE '=|%3D' | gf sqli > $2
        python3 ~/tools/sqlmap-dev/sqlmap.py -m $2 --dbs --batch --risk 3 --level 5
    fi
}
fuzzer(){
    ssh -i "~/tools/server/fuzzer.pem" ubuntu@13.127.225.24
}
sendf(){
     scp -i "~/tools/server/fuzzer.pem" $1 ubuntu@13.127.225.24:/home/ubuntu/$2
}
recvf(){
    scp -i "~/tools/server/fuzzer.pem" ubuntu@13.127.225.24:/home/ubuntu/$1 $2
}
dork-root(){
    echo -n site:*.;join.py $1 | sed 's/,/ | site:*./g'
}
