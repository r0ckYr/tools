#!/bin/bash
sudo apt purge -y man-db
sudo apt-get -y update
sudo apt-get -y upgrade


sudo apt-get install -y libcurl4-openssl-dev
sudo apt-get install -y libssl-dev
sudo apt-get install -y libssl-doc
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
sudo apt install unzip
sudo apt-get install -y xargs
sudo apt-get install -y nmap
sudo apt install chromium-browser
sudo apt install -y cmake
sudo apt install -y whois
pip3 install jsbeautifier
pip3 install keyboard
sudo pip3 install keyboard
pip3 install urllib3
pip3 install bs4
pip3 install arjun
pip3 install uro

#install my tools
git clone https://github.com/r0ckYr/tools.git
cd tools
rm README.md

#dirsearch
git clone https://github.com/maurosoria/dirsearch.git
cd dirsearch/
pip3 install -r requirements.txt
sudo python3 setup.py install
cd ~/tools

#vhost discovery
git clone https://github.com/jobertabma/virtual-host-discovery.git

#masscan
sudo apt-get --assume-yes install git make gcc
git clone https://github.com/robertdavidgraham/masscan
cd masscan
make
sudo make install
cd ~/tools

#sqlmap
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev

#massdns
git clone https://github.com/blechschmidt/massdns.git
cd ~/tools/massdns
make
sudo make install
cd ~/tools/

#dnsgen
git clone https://github.com/ProjectAnte/dnsgen
cd dnsgen
pip3 install -r requirements.txt
sudo python3 setup.py install
cd -

#dnsvalidator
git clone https://github.com/vortexau/dnsvalidator.git
cd dnsvalidator
pip3 install -r requirements.txt
sudo python3 setup.py install
cd -

#urldedupe
git clone https://github.com/ameenmaali/urldedupe.git
cd urldedupe
cmake CMakeLists.txt
make
sudo cp urldedupe /usr/local/bin
cd -

#install aquatone
mkdir aquatone
cd aquatone
wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip
unzip aquatone_linux_amd64_1.7.0.zip
sudo cp aquatone /usr/local/bin
cd -

cd ~/
#install go
wget https://golang.org/dl/go1.17.2.linux-amd64.tar.gz
tar -xvf go1.17.2.linux-amd64.tar.gz
sudo cp -r go /usr/local
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

#httprobe
go get -u github.com/tomnomnom/httprobe

#unfurl
go get -u github.com/tomnomnom/unfurl

#waybackurls
go get github.com/tomnomnom/waybackurls

#anew
go get -u github.com/tomnomnom/anew

#subover
go get github.com/Ice3man543/SubOver

#shuffledns
GO111MODULE=on go get -v github.com/projectdiscovery/shuffledns/cmd/shuffledns

#subfinder
GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder

#ffuf
go get -u github.com/ffuf/ffuf

#dnsx
go get -v github.com/projectdiscovery/dnsx/cmd/dnsx

#httpx
GO111MODULE=on go get -v github.com/projectdiscovery/httpx/cmd/httpx

#kxss
go get github.com/Emoe/kxss

#qsreplace
go get -u github.com/tomnomnom/qsreplace

#interactsh
go install -v github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest

#amass
cd ~/tools
mkdir amass
cd amass
wget https://github.com/OWASP/Amass/releases/download/v3.14.1/amass_linux_amd64.zip
unzip amass_linux_amd64.zip
cd amass_linux_amd64
mv ~/tools/tools/files/config.ini .
cp amass ~/go/bin
cd


#clean
rm install.sh
rm *.tar.gz
