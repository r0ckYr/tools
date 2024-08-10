#!/bin/bash
sudo mv needrestart.conf /etc/needrestart/needrestart.conf
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
sudo apt-get install -y python-dnspython
sudo apt-get install -y git
sudo apt-get install -y rename
sudo apt install -y unzip
sudo apt-get install -y xargs
sudo apt-get install -y nmap
sudo apt install -y chromium-browser
sudo apt install -y cmake
sudo apt install -y whois
sudo apt install -y vim
pip3 install jsbeautifier
pip3 install keyboard
sudo pip3 install keyboard
pip3 install urllib3
pip3 install bs4
pip3 install arjun

#install my tools
git clone https://github.com/r0ckYr/tools.git
cd tools
rm README.md

#install vim configs
cd configs
tar -xzf v.tgz -C ~/
mv .vimrc ~/
cd ..
cd ~/tools

#masscan
sudo apt-get --assume-yes install git make gcc
git clone https://github.com/robertdavidgraham/masscan
cd masscan
make
sudo make install
cd ~/tools

#sqlmap
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap

#massdns
git clone https://github.com/blechschmidt/massdns.git
cd ~/tools/massdns
make
sudo make install
cd ~/tools/

#dnsvalidator
git clone https://github.com/vortexau/dnsvalidator.git
cd dnsvalidator
pip3 install -r requirements.txt
sudo python3 setup.py install
cd ~/tools

#urldedupe
git clone https://github.com/ameenmaali/urldedupe.git
cd urldedupe
cmake CMakeLists.txt
make
sudo cp urldedupe /usr/local/bin
cd -

cd ~/
#install go
wget https://golang.org/dl/go1.21.3.linux-amd64.tar.gz
tar -xvf go1.21.3.linux-amd64.tar.gz
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

#unfurl
go install github.com/tomnomnom/unfurl@latest

#waybackurls
go install github.com/tomnomnom/waybackurls@latest

#anew
go install github.com/tomnomnom/anew@latest

#subover
go install github.com/Ice3man543/SubOver@latest

#subfinder
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

#ffuf
go install github.com/ffuf/ffuf@latest

#dnsx
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest

#puredns
go install github.com/d3mondev/puredns/v2@latest

#httpx
go install -v github.com/projectdiscovery/httpx/cmd/httpx@v1.3.1

#kxss
go install github.com/Emoe/kxss@latest

#qsreplace
go install github.com/tomnomnom/qsreplace@latest

#interactsh
go install -v github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest

#getJs
go install github.com/003random/getJS@latest

#gotator
go install github.com/Josue87/gotator@latest

#gua
go install github.com/lc/gau/v2/cmd/gau@latest
go install github.com/bp0lr/gauplus@latest

#github-subdomains
go install github.com/gwen001/github-subdomains@latest

#VhostFinder
go install -v github.com/wdahlenburg/VhostFinder@latest

#jsluice
go install github.com/BishopFox/jsluice/cmd/jsluice@latest

#amass
cd ~/tools
mkdir amass
cd amass
wget https://github.com/owasp-amass/amass/releases/download/v4.0.2/amass_Linux_amd64.zip
unzip amass_Linux_amd64.zip
mv ~/tools/tools/files/config.ini .
cd amass_Linux_amd64
cp amass ~/go/bin
cd

cd ~/tools
mkdir x8
cd x8
wget https://github.com/Sh1Yo/x8/releases/download/v4.3.0/x86_64-linux-x8.gz
gzip -d x86_64-linux-x8.gz
mv x86_64-linux-x8 x8
chmod +x x8
sudo cp x8 /usr/local/bin/

#clean
cd ~/
rm install.sh
rm *.tar.gz
