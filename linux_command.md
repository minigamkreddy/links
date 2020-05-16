find *.log | wc -l

grep FAILED *.log | wc -l

grep "AssertionError" *.log | wc -l

grep "AssertionError" *.log -B 5 -A 5

grep panel_*_failed  | wc -l


To start the server : Command to start supplic

go get -u github.com/urfave/negroni

go get -u github.com/golang/dep/cmd/dep

https://www.gorillatoolkit.org/pkg/mux

https://github.com/Chennai-Golang/101-workshop/blob/master/Setup.md

https://github.com/AgarwalConsulting/learning-golang/blob/master/004-http-application/003-handler-interface.go

https://tour.golang.org/moretypes/4

https://github.com/sirupsen/logrus

https://12factor.net/

https://github.com/golang-standards/project-layout


To compile the go folders in the garnet


Example


/.goenv/src/github.com/Chennai-Golang/101-workshop/examples/packages

vi hello.go

go build .

./packages


http://gorm.io/docs/models.html

https://golang.org/src/unsafe/unsafe.go


examples on channels

https://tour.golang.org/concurrency/5


timer := time.After

(time.Microsecond * 10) <- timer

quit <- 0


golang.org/pkg/builtin


https://tour.golang.org/garbagecollector/1

https://github.com/go-ozzo/ozzo-validation


https://blog.golang.org/using-go-modules


Garbage Collector


GoTri-colour concurrent mark and sweep garbage collector


Python uses GC and ARC (Automatic Reference Coding)


GO


1) Mark phase

2) Sweep phases


Go uses the breathefirst traversing (depthfirst)


https://golang.org/pkg/runtime/


1) Latency: low latency

2) Throughput : how many operations can program can do

high Throughput


https://making.pusher.com/golangs-real-time-gc-in-theory-and-practice/

https://making.pusher.com/go-tool-trace/

https://github.com/WillSewell/gc-latency-experiment



GOMAXPROCS controls no of go routines


goenv version



go get -u github.com/google/pprof

pprof mem.prof

pprof -http localhost:9001 cpu.prof

apt-get install graphviz


https://golang.org/pkg/net/http/pprof/

https://github.com/WillSewell/gc-latency-experiment


To control the race condition in golang


go run -race main.go


GOMAXPROC=2 make run-go-preemption


gomega

ginkgo


https://onsi.github.io/ginkgo/

https://golang.org/pkg/runtime/debug/

https://golang.org/pkg/context/



docker build -t books-example:latest .

Docker run -it -p 9000:9000 books-examples:latest


IOP SETUP DOCUMENT


IOP SETUP ISSUES


2019-09-18 18:16:26,592 Vpanel [ERROR]: Failed to get ReconnectToApState thread status....

2019-09-18 18:16:26,592 Vpanel [ERROR]: ReconnectAP Thread execution is not completed....


sky control 00:25:FO:7C:08:BC


1. GTK not installed

*** Could not run GTK+ test program, checking why...

*** The test program failed to compile or link. See the file config.log for the

*** exact error that occured. This usually means GTK+ is incorrectly installed.


configure: error: Neither Qt nor GTK+ 2.12.0 or later are available, so Wireshark can't be compiled


apt-cache search GTK+ | grep GTK+

apt-get install libgtkgl2.0-dev


2. Wireshark not starting

vivint@vivint:~/Downloads/wireshark-1.10.6$ wireshark -v

wireshark: error while loading shared libraries: libwiretap.so.3: cannot open shared object file: No such file or directory


sudo ldconfig



3. sudo apt-get install vim synaptic g++ openssh-server openssh-client


4.sudo pip install polling


5.sudo pip install openpyxl


6.sudo pip install colorlog


7.2019-09-17 16:10:31,805 SetupPreliminaryCheck [ERROR]: No Internet Connection between test controller and external network.


8. Need to add info on setting SYSTEM_MESH_AP_INTERFACE and SYSTEM_INTERFACE


9. Sniffer config file path is wrong

vivint@vivint:~/Ges_Viv_STA-IOP_v10.0c/VivintSniffer$ ls

Automation_Logs Config_Sniffer.xml pktAnalysis sniffer_agent.sh Sniffer_Logs sniffer_service

vivint@vivint:~/Ges_Viv_STA-IOP_v10.0c/VivintSniffer$ vim Automation/Sniffer/Config_Sniffer.xml


10. Command to start sniffer service

sudo ./sniffer_agent.sh start


11. Wifi interface name of sniffer is hardcoded in sniffer_agent.sh and should be changed as per setup



12. Sniffer folder path is hardcoded

vivint@vivint:~/Ges_Viv_STA-IOP_v10.0c/VivintSniffer$ ./sniffer_service

/home/vivint/VivintSniffer/Config_Sniffer.xml

/home/vivint/VivintSniffer/Config_Sniffer.xml

Traceback (most recent call last):

File "sniffer_service.py", line 24, in <module>

File "/tmp/pip-install-8GakXp/PyInstaller/PyInstaller/loader/pyimod03_importers.py", line 395, in load_module

File "SnifferParserUtils.py", line 3, in <module>

File "/tmp/pip-install-8GakXp/PyInstaller/PyInstaller/loader/pyimod03_importers.py", line 395, in load_module

File "TsharkCheck.py", line 15, in <module>

IOError: [Errno 2] No such file or directory: '/home/vivint/VivintSniffer/Config_Sniffer.xml'

[30619] Failed to execute script sniffer_service


13. minicom not installed

vivint@vivint:~$ sudo minicom -D /dev/ttyUSB0 -b 115200

sudo: minicom: command not found

sudo apt-get install minicom


14. Install latest geckodriver


15. sudo apt-get install aptitude


16.sudo pip install selenium==3.6.0


17. In the TestSuiteControl.py we need to change sniffer ip address


SNIFFER_XMLRPC_SERVER = 'http://192.168.1.24:60025'

SNIFFER_XMLRPC_SERVER = 'https://sniffer_ip_address:60025'


18. In TBConfig.xlsx we need to change the mac address of the AP which is related to the 2.4 Ghz and 5Ghz and also we need to change the sniffer path ,sniffer ip ,DUT_MAC as the panel mac.


19.Iperf

sudo apt-get install iperf



20.Wireshark issues


checking for bison... no

checking for byacc... no

checking for yacc... no


sudo apt-get install bison

sudo apt-get install byacc

sudo apt-get install yacc


21. sudo apt-get install arp-scan



'dutpath: ', '/media/sda1/Logs/Dut_log_Sep_19_2019_10_57_18')

('logname: ', 'TPLINK_ARCHERC9_open5g_20190919_052821')



git clone and push lines


git clone links


1) git clone http://gitlab.globaledgesoft.com:81/root/ges.git

2) git clone https://gs.globaledgesoft.com/hl.ashweeja/Regression_Automation.git

3) git checkout video_automation

4) gs.globaledgesoft.com

5) https://stackoverflow.com/questions/21181231/server-certificate-verification-failed-cafile-etc-ssl-certs-ca-certificates-c


git push code comments


3) git status

4) git add .

5) git config --global user.email "hl.ashweeja”

6) git config --global user.name "manoj"

7) git commit -m "latest changes"

8) git push origin video_automation

9) git show

10) git log

11) git branch

12) git merge

13)


https://golang.org/pkg/encoding/hex/#Decode

https://www.swtestacademy.com/xpath-selenium/

https://updateseng.vivint.com/innovation/packages/branches/3.19.4/3.19.4.29097/

We are using the latest firmware downloaded from the below links. Also shared all the firmware used by GES in our slack channel.

For Vivotek cameras:

https://updateseng.vivint.com/innovation/camera_firmwares/Vivotek/

For Alpha cameras:

https://updateseng.vivint.com/innovation/camera_firmwares/Alpha/

 

https://pypi.org/project/nose-progressive/

https://pypi.org/project/nose-terse-output/

https://pypi.org/project/nose-leak-detector/

https://pypi.org/project/vivint-slickqa-snot/ - Open source!!!

https://pypi.org/project/tissue/

 




ant : wpa_supplicant -Dnl80211 -iwlan0 -c/etc/wpa_supplicant.conf

I tried to compile wpa_supplicant 2.9 on device by following commands:
pkg install wget build-essential pkg-config openssl openssl-static dbus dbus-glib dbus-glib-static dbus-static readline readline-static ncurses ncurses-static libnl libnl-static
wget https://www.w1.fi/releases/wpa_supplicant-2.9.tar.gz && tar xvf wpa_supplicant-2.9.tar.gz
cd wpa_supplicant-2.9/wpa_supplicant/
cp defconfig .config
make

-D : specifies the driver

-i : wireless interface

-c : configuration file for connection.

Configuration file examples for connections:

nmcli is a command line tool for controlling Network Manager.nmcli is used to create, display, edit, delete, activate, and deactivate network connections, as well as control and display network device status.
nmcli -help
nmcli con show : Lists all the Network connections which is created under network manager.
wpa_cli -i <interface> status
ps -aux | grep -v grep | grep wpa_supplicant
/sbin/wpa_supplicant -u -s -O /run/wpa_supplicant

regression exexution command
python run_regression_with_sky.py -s regression_sanity_test.py -a test_id='test_case_number' -l test.log

https://pypi.org/project/nose-progressive/

https://pypi.org/project/nose-terse-output/

https://pypi.org/project/nose-leak-detector/

https://pypi.org/project/vivint-slickqa-snot/ - Open source!!!

https://pypi.org/project/tissue/

 

http://updateseng.vivint.com/innovation/packages/branches/3.19.4.emb2810/3.19.4.emb2810.28932/



ping camera serial command
sudo minicom -D /dev/ttyUSB0 -b 57600

for panel
curl 127.0.0.1:8080/service/
in panel for nfc
curl 127.0.0.1:8080/primary_touch_link_device/
curl 127.0.0.1:8080/primary_touch_link_device/ | grep local
factory reset command for ping camera
curl 127.0.0.1/config/system_reset.cgi?reset=go
reboot


grep -rn 'FAILED' -B 5 *.log
grep -rn 'FAILED' -A 5 *.log
grep -rn 'FAILED' *.log

echo p@ssw0rd | sudo -S python /home/vivint/local-repos/rpi/rpi_io.py A700P8VY off 1
echo p@ssw0rd | sudo -S python /home/vivint/local-repos/rpi/rpi_io.py A700P8VY on 1
echo p@ssw0rd | sudo -S iw wlp0s20f3 scan | grep "VIVINT_DBC_(6F:01:42)"
curl --digest -u root:adcvideo http://192.168.1.1/cgi-bin/admin/setparam.cgi?system_enabletty=1
ssh vivint@192.168.50.69
echo p@ssw0rd | sudo -S iw wlp0s20f3 scan | grep "VIVINT_DBC_(6F:01:42)"
tail -f ges_panel_rtspd_stream_validation_1.log

sly-qt5-image-imx6dl-slimline-3.19.4.emb382.28852.rootfs.tar.bz2 for wall sly
touchlink-qte-image-glibc-ipk-3.19.4.29054-touchlink.rootfs.tar.bz2 for sky control

git clone http://gitlab.globaledgesoft.com:81/root/ges.git
git checkout video_automation
git status
git add lib/ges.py
git diff lib/ges.py
git commit -m "modified duration validation validate_camera_rtspd_stream"
git push origin video_automation

 ps -ef | grep nose
sudo killall python
 ps -ef | grep python

nosetests -c ../config/panels/ges_ping_wallsly.ini --nocapture --nologcapture ges_panel_rtspd_stream_validation.py |& tee ges_panel_rtspd_stream_validation.log
python regression_ges.py ../config/panels/ges_ping_wallsly.ini

grep -inr "signal_stream_duplicated"  | cameras.log


Can you check if following prints are present in cameras.log?

 

So what you are seeing is not the fix -  I don't believed we able to reproduce the issue.  If the issue happen with the fix you would see this in the log:

Is the camera still able to stream

_test_rtsp_streams: 404 Occured when testing stream for

then 

404 File Not Found, Or In Incorrect Format

I have a simpler change I like to test - build coming today

ssh qaadmin@10.1.44.78
ssh qadmin@10.1.44.157

 "rpi": {
    "username": "qaadmin",
    "ip": "10.1.44.78"
}

"sniffer": {
    "username": "qaadmin",
    "enable": "true",
    "dest_path": "/home/qaadmin/sniffer",
    "ip": "10.1.44.78",
    "password": "password100",
    "capture_path": "/tmp/",
    "channel": "1"
  },

"panel": {
    "nw_username": "root",
"admin_user": "testadmin",
 "host_password": "ap3x!",
    "host_username": "root",
"ip": "10.1.44.80",
"nw_br_lan_ip": "172.16.10.254",
}




stat -c "%U %G" sniffer
sudo chown vivint sniffer
stat -c "%U %G" Captures/
ls | grep '^d' | xargs
ls -d */ | xargs sudo chown vivint

sudo iptables -t nat -A POSTROUTING -s 192.168.20.0/24 -o eth0 -j MASQUERADE



https://www.cyberciti.biz/faq/how-to-use-iptables-with-multiple-source-destination-ips-addresses/

iptables -t nat -A POSTROUTING -o eth1 -j MASQUERADE



iptables -t nat -A PREROUTING  -p tcp -i eth0 -d 10.1.44.2 -j DNAT --to-destination 192.168.2.2
iptables -t nat -A PREROUTING  -p udp -i eth0 -d 10.1.44.2 -j DNAT --to-destination 192.168.2.2



 

https://www.youtube.com/watch?v=P3GRaGy9fMI

 https://serverfault.com/questions/234370/forward-all-ports-incoming-to-a-specific-ip-to-internal-ip-address


The link to block the mdns packets in wired and wireless


https://www.ctrl.blog/entry/how-to-disable-mdns-linux.html


the link to block the multicast traffic in wired and wiresless


https://unix.stackexchange.com/questions/25872/how-can-i-know-if-ip-multicast-is-enabled


the iptables link to disable the mdns input packet


https://unix.stackexchange.com/questions/271164/how-to-block-broadcast-messages-apples-mdns-traffic


https://www.binarytides.com/linux-netstat-command-examples/


sudo iptables -A INPUT -i any -p udp -m state --state NEW -m udp --dport 5353 -j DROP
sudo iptables -L -v -n


ip maddr show
sudo iptables -F
sudo ufw deny out 5353/udp comment "drop outgoing mDNS"

sudo iptables -A INPUT -d 224.0.0.251 -p udp --dport 5353 -j DROP

sudo iptables -t filter -L INPUT -n -v

ifconfig wlan0 -multicast
ip link show wlan0 | grep MULTICAST


sudo iptables -A INPUT -i wlan0 -p udp -m state --state NEW -m udp --dport 5353 -j DROP
sudo iptables -A INPUT -i any -d 224.0.0.251 -p udp --dport 5353 -j DROP


sudo ufw deny out 5353/udp comment "drop outgoing mDNS"
sudo ufw deny in 5353/udp comment "drop outgoing mDNS"



Hi All,


The commands to block the mdns traffic are.


a) We can DENY the MDNS traffic using the "firewall (ufw)".
    i)   "sudo ufw status"  is used to check whether the ufw is enabled or not.
    ii)  "sudo ufw enable" is used to enable the ufw.
    iii) "sudo ufw deny out 5353/udp comment "drop outgoing mDNS" "  this command is used to deny the mdns outgoing traffic.
    iv) "sudo ufw deny in 5353/udp comment "drop incomming mDNS" " this command is used to deny the mdns  incomming traffic.
                Here the 5353 is the port number of mdns


The link related to the ufw commands
    https://www.ctrl.blog/entry/how-to-disable-mdns-linux.html

b)  We can DENY the multicast traffic using the "ifconfig" command
    i) "ip maddr show" with this command we can find each interface information.
    ii) "ip link show 'interface_name'  | grep MULTICAST" this command is used to check the multicast traffic running on the particular interface.
    ii) "sudo ifconfig 'interface_name' multicast"  this command is used to allow the multicast traffic.
    iii) "sudo ifconfig 'interface_name' -multicast" this command is  used to deny the multicast traffic.


The link related to the ifconfig commands
        https://unix.stackexchange.com/questions/25872/how-can-i-know-if-ip-multicast-is-enabled


        
c) We can DENY the MDNS traffic using the "iptables" command
    i) "sudo iptables -A INPUT -i enp2s0 -d 224.0.0.251 -p udp -m state --state NEW -m udp --dport 5353 -j DROP "  this command is used to deny the mdns port 5353.
    ii) "sudo iptables -t filter -L INPUT -n -v" this command is used to check whether  the rule is applied or not.
    iii) " sudo ip6tables -A INPUT -i enp2s0 -d ff02::fb -p udp -m state --state NEW -m udp --dport 5353 -j DROP "  this command is used to deny the ipv6 mdns port 5353.
            Here ff02::fb is the multicast ip address of ipv6
The link related to the iptables commands.
    https://unix.stackexchange.com/questions/271164/how-to-block-broadcast-messages-apples-mdns-traffic


                firewall commands	
i)  sudo ufw status
ii) sudo ufw enable
iii) sudo ufw deny out 5353/udp comment "drop outgoing mDNS"
iv) sudo ufw deny in 5353/udp comment "drop incomming mDNS"
                Here the 5353 is the port number of mdns
	
The link related to the ufw commands
    https://www.ctrl.blog/entry/how-to-disable-mdns-linux.html
	
                ifconfig commands	
i) ip maddr show
ii) ip link show 'interface_name'  | grep MULTICAST
iii) sudo ifconfig 'interface_name' multicast
iv) sudo ifconfig 'interface_name' -multicast

	
The link related to the ifconfig commands
        https://unix.stackexchange.com/questions/25872/how-can-i-know-if-ip-multicast-is-enabled

	
                iptables commands	
i) sudo iptables -A INPUT -i 'interface_name' -d 224.0.0.251 -p udp -m state --state NEW -m udp --dport 5353 -j DROP
ii) sudo iptables -t filter -L INPUT -n -v
iii) sudo ip6tables -A INPUT -i enp2s0 -d ff02::fb -p udp -m state --state NEW -m udp --dport 5353 -j DROP
         Here ff02::fb is the multicast ip address of ipv6
	
The link related to the iptables commands.
    https://unix.stackexchange.com/questions/271164/how-to-block-broadcast-messages-apples-mdns-traffic

	
  



sudo tcpdump -s 0 port mdns -i eno1 -w mycap.pcap



