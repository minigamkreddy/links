cd /opt/
wget ftp://172.16.2.4/Linux/firefox/firefox-59.0.2.tar.bz2
tar -xvf firefox-59.0.2.tar.bz2
cd /usr/bin/
mv firefox firefox_old
ln -s /opt/firefox/firefox /usr/bin/firefox
