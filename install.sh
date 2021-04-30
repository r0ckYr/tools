#!/bin/bash
sudo apt-get -y update
sudo apt-get -y upgrade


sudo apt-get install -y libcurl4-openssl-dev
sudo apt-get install -y libssl-dev
sudo apt-get install -y jq
sudo apt-get install -y ruby-full
sudo apt-get install -y libcurl4-openssl-dev libxml2 libxml2-dev libxslt1-dev ruby-dev build-essential libgmp-dev zlib1g-dev
sudo apt-get install -y build-essential libssl-dev libffi-dev python-dev
sudo apt-get install -y python-setuptools
sudo apt-get install -y libldns-dev
sudo apt-get install -y python3-pip
sudo apt-get install -y python-pip
sudo apt-get install -y python-dnspython
sudo apt-get install -y git
sudo apt-get install -y rename
sudo apt-get install -y xargs

#get my tools
git clone https://github.com/r0ckYr/tools.git
cd tools
rm README.md

#install go
wget https://golang.org/dl/go1.16.3.linux-amd64.tar.gz
sudo tar -xvf go1.16.3.linux-amd64.tar.gz
sudo mv go /usr/local
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export TOOLSPATH=/home/ubuntu/tools/tools/
export PATH=$GOPATH/bin:$GOROOT/bin:$TOOLSPATH/recon:$TOOLSPATH/urls:$TOOLSPATH:$TOOLSPATH/hunter:$PATH
source ~/tools/.bash_profile

echo 'export GOROOT=/usr/local/go' >> ~/.bashrc
echo 'export GOPATH=$HOME/go'	>> ~/.bashrc
echo 'export TOOLSPATH=/home/ubuntu/tools/tools/' >> ~/.bashrc
echo 'export PATH=$GOPATH/bin:$GOROOT/bin:$TOOLSPATH/recon:$TOOLSPATH/urls:$TOOLSPATH:$TOOLSPATH/hunter:$PATH' >> ~/.bashrc
echo 'source ~/tools/.bash_profile' >> ~/.bashrc
source ~/.bashrc

#dirsearch
git clone https://github.com/maurosoria/dirsearch.git

#install aquatone
go get github.com/michenriksen/aquatone

#install chromium
sudo snap install chromium

#virtual host discovery
git clone https://github.com/jobertabma/virtual-host-discovery.git

#sqlmap
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev

#knockpy
git clone https://github.com/guelfoweb/knock.git

#nmap
sudo apt-get install -y nmap

#massdns
git clone https://github.com/blechschmidt/massdns.git
cd ~/tools/massdns
make
make install
cd ~/tools/

#httprobe
go get -u github.com/tomnomnom/httprobe

#unfurl
go get -u github.com/tomnomnom/unfurl

#waybackurls
go get github.com/tomnomnom/waybackurls

#seclist
echo "downloading Seclists"
cd ~/tools/
git clone https://github.com/danielmiessler/SecLists.git
cd ~/tools/SecLists/Discovery/DNS/
##THIS FILE BREAKS MASSDNS AND NEEDS TO BE CLEANED
cat dns-Jhaddix.txt | head -n -14 > clean-jhaddix-dns.txt
cd ~/tools/
echo "done"

#subover
go get github.com/Ice3man543/SubOver

#shuffledns
GO111MODULE=on go get -v github.com/projectdiscovery/shuffledns/cmd/shuffledns

#subfinder
GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder

#ffuf
go get -u github.com/ffuf/ffuf

#masscan
sudo apt-get --assume-yes install git make gcc
git clone https://github.com/robertdavidgraham/masscan
cd masscan
make
sudo make install

#amass

