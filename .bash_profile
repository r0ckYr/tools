#!/bin/bash

#-----------------------useful------------------------------------
fuzzer(){
    ssh -i "~/tools/server/fuzzer.pem" ubuntu@3.108.14.165
}
vps(){
    ssh -i "~/tools/server/rocky.pem" ubuntu@ec2-65-2-19-234.ap-south-1.compute.amazonaws.com
}
tekken(){
    wine ~/test/Tekken_3.exe & exit
}
endpoints(){
    cat $1 | grep -aoP "(?<=(\"|\'|\`))\/[a-zA-Z0-9_?&=\/\-\#\.]*(?=(\"|\'|\`))" | sort -u
}
conn(){
    ping www.google.com
}
prototype(){
    grep -Hnir -E "'backbone-qp'|'canjs-deparam'|hubspot|'jquery-bbq'|'jquery-deparam'|'jquery-parseparam'|'jquery-query-object'|'jquery-sparkle'|'mootools-more'|mutiny|Create|mutiny|'parse_str'|purl|'swiftype-site-search'|'v4fire-core'|yui3" | grep "\.js"
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
t(){
	tmux -f ~/.tmux.config
}
burp(){
	cd '/home/rocky/tools/Burp/Burp Suite Professional Edition v2020.12.1 x64 Full Activated + Extensions - WwW.Dr-FarFar.CoM/Burp Suite Professional Edition v2020.12.1'
	java -noverify -javaagent:Dr.FarFar.jar -jar burpsuite_pro_v2020.12.1.jar & exit
}
asnlookup(){
	python3 ~/tools/asnlookup/asnlookup.py -o $1
}
cleanup(){
	cat *.txt | sort -u > all.txt
	getintresting all.txt
	getroot all.txt
	gettldomains all.txt
}
finalize(){
	mkdir final
	cat all.txt | tee -a final/final.txt
	cat subfinder/all.txt | tee -a final/final.txt
	cat third_level_domains/all.txt | tee -a final/final.txt
	cd final

	cat final.txt | sort -u > t
	rm final.txt
	mv t final.txt

	probe final.txt
	getintresting active-final.txt
	getintresting final.txt
	getroot final.txt
	gettldomains final.txt
	cat active-final.txt | cut -d "/" -f 3 | sort -u | tee -a active-domains.txt
}
getroot(){
	cat $1 | rev | cut -d "." -f 1,2 | rev | sort -u | tee -a root-$1
}
getintresting(){
	words=("api" "uat" "prod" "admin" "corp" "stag" "jenkins" "jankins" "jire" "jira" "smal" "auth" "outh" "transfer")
	for i in "${words[@]}"
	do
		cat $1 | grep $i
	done | sort -u | tee -a potential-$1
}
gettldomains(){
     cat $1 | rev | cut -d "." -f 1,2,3 | rev | sort -u > t
     getthirdleveldomains.py t > third-level-$1
     rm t
}
words(){
    for w in $(cat $1)
    do
        for i in {1..7}
        do
            echo $w | cut -d "." -f $i
        done
    done | sort -u
}
break-urls(){
    for w in $(cat $1)
    do
        for i in {1..10}
        do
            echo $w | cut -d "/" -f $i
        done
    done | sort -u

}
server(){
    python3 -m http.server $1
}
bruteable(){
    bruteable.py $1 | rev | cut -d "." -f 1,2,3 | rev | sort -u
}
#-----------------------subdomain-discovery-------------------------
am(){
	mkdir amass
    sudo amass enum -passive -dir amass/ -d $1
}
crtsh(){
	python3 ~/tools/tools/crtsh.py "$1"
}
domains(){
	python3 ~/tools/tools/domains.py "$1"
}
subfind(){
	cat $1 | xargs -n1 -P4 -oI{} subfinder -silent -d {}
}
sublist(){
	mkdir sublister
	cp $1 sublister/
	cd sublister
	for i in $(cat $1)
	do
		python3 ~/tools/Sublist3r/sublist3r.py -d $i -o $i.txt
	done
	cleanup
	cd ..
}
brutelist(){
    cat $1 | xargs -n1 -P4 -I{} shuffledns -w ~/tools/SecLists/Discovery/DNS/dns-Rocky.txt -d {} -silent -r ~/tools/tools/files/resolvers.txt
}
brute(){
	shuffledns -w ~/tools/SecLists/Discovery/DNS/dns-Rocky.txt -d $1 -silent -r ~/tools/tools/files/resolvers.txt
}
bruteall(){
	for i in $(cat $1)
	do
		shuffledns -w $2 -d $i -silent -r ~/tools/tools/files/resolvers.txt
	done
}

crtshnahamsec(){
	curl -s https://crt.sh/?Identity=%.$1 | grep ">*.$1" | sed 's/<[/]*[TB][DR]>/\n/g' | grep -vE "<|^[\*]*[\.]*$1" | sort -u | awk 'NF'
}
aqua(){
	mkdir aquatone
	cat $1 | aquatone -silent -out aquatone/
}

#-----------------port-snanning--------------------------------------
nm(){
	sudo nmap -T4 -Pn -v --script=http-title $1
}
nms(){
	sudo nmap -T4 --script=http-title -v -Pn -oN nmap-$1 $1
}
nma(){
	sudo nmap -Pn -T4 -v -A $1
}
nmall(){
	sudo nmap --script=http-title -T4 -Pn -v -iL $1 -oN $2
}
mscan(){
	sudo masscan -p0-65535 $1 --rate=5000 --open -oG masscan-$1
}
msall(){
	sudo masscan -p0-65535 -iL $1 --rate=10000 --open -oG masscan-all-$1
}
mslist(){
	sudo masscan -p2075,2076,6443,3868,3366,8443,8080,9443,9091,3000,8000,5900,8081,6000,10000,8181,3306,5000,4000,8888,5432,15672,9999,161,4044,7077,4040,9000,8089,443,7447,7080,8880,8983,5673,7443,19000,19080 --rate=10000 --open -iL $1 -oG masscan-$1
}
mstop(){
	sudo masscan -p1-1000,2075,2076,6443,3868,3366,8443,8080,9443,9091,3000,8000,5900,8081,6000,10000,8181,3306,5000,4000,8888,5432,15672,9999,161,4044,7077,4040,9000,8089,443,7447,7080,8880,8983,5673,7443,19000,19080 --rate=10000 --open -iL $1 -oG masscan-top-$1

}
#---------------------content-discovery------------------------------
dirsearch(){
	python3 ~/tools/dirsearch/dirsearch.py -w ~/tools/tools/files/dict.txt -u $1 -t 100 -e $2 -H 'X-Forwarded-For: 127.0.0.1'
}
dlist(){
	python3 ~/tools/dirsearch/dirsearch.py -u $1 -w $2 -H 'X-Forwarded-For:127.0.0.1' -e $3 -t 200
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
    cat $1 | xargs -n1 -P4 -I{} recon.py {} | tee -a domains

    #subfinder
	cat $1 | xargs -n1 -P4 -I{} subfinder -silent -d {} | tee -a domains

    #clean domains
    sanitizer.py $1 domains | sort -u > t
    rm domains
    mv t domains

    #get third-level-domains
    gettldomains domains

    #recon.py on third-level-domains
	cat third-level-domains | xargs -n1 -P10 -I{} recon.py {} | tee -a domains

    #get bruteable domains
    bruteable domains > to-brute #bruteforce these later

    #sort and clean domains
    sanitizer.py $1 domains | sort -u > t
    rm domains
    mv t domains

    #get active domains
    probe domains

    #get data on active domains
    hunter.py active-domains

    #wayback machine
    #urls active-domains

    #screenshot later
}
probe(){
	splitter.py $1
    cat files | xargs -n1 -P4 -I{} sh -c 'cat {} | httprobe -prefer-https' | tee -a active-$1
    rm 1 2 3 4 files
    cat active-$1 | sort -u > t
    rm active-domains
    mv t active-domains
}
urls(){
    cat $1 | xargs -n1 -P4 -I{} geturls.py {} | tee -a urls
}
apis(){
    grep -Hnir api | grep key | vi -
}
rlist(){
    cat $1 | xargs -n1 -P4 -I{} recon.py {} | tee -a domains
}
am(){
    mkdir amass
    cat $1 | xargs -n1 -P4 -I{} amass enum -passive -src -config ~/tools/amass/config.ini -dir amass/ -d {}
}
takeover(){
    cd ~/tools/SubOver/
    SubOver -t 100 -l $1
    cd -
}
