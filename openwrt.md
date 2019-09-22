What is OpenWRT?

    OpenWrt is a Linux-based customizable operating system for embedded devices.
    Named “WRT” after the first device that prompted porting Linux to them “Linksys WRT45G”
    First release: Jan 2004
    First Stable version : July 2018

File:Exam.jpg
Why OpenWRT?

    Free and Open Source
    Community driven (cf. DD­WRT)
    Large repository of packages
    Broadest hardware support - 680+ devices
    Used by many OEMs – Netgear, Linksys, TP-Link, D-Link
    Today, OpenWrt can be used in various embedded devices including Wi-Fi routers, wired routers, residential gateways, smartphones, laptops and even x86-based PCs.

General requirements for OpenWrt/LEDE support

    Architecture: MIPS, ARM, PowerPC, x86, ...etc
    Chipsets: 

 – Atheros AR71xx/AR724x/913x
 – Broadcom BCM47xx/53xx/27xx
 – To see more about Chipsets click here

    SoC / target supported by OpenWrt/LEDE
    Sufficient Flash to accommodate OpenWrt/LEDE firmware image

 - 4MB min (won't be able to install GUI (LuCI))
 - 8MB better (will fit GUI and some other applications)

    Sufficient RAM for stable operation

 - 32MB min, 64MB better

Note : Devices with ≤4MB flash and/or ≤32MB ram suffer from limitations in usability, extensibility and stability of operation. Consider this when choosing a device to buy, or when deciding to flash OpenWrt on your device because it is listed as supported. See 432_warning for details.
What Packages?

- Filesystems           : CIFS (Samba), NFS, sshfs, ext4 ...
- Filesystem tools      : lvm2
- Editors               : nano, joe, vim
- IRC                   : Bahamut IRC, Eggdrop IRC, lirc, irssi, Torrent, Tor
- Proxies               : dansguardian
- Network authentication: FreeRADIUS
- Dynamic DNS           : ddns­scripts, ndyndns, odhcpd,dnsmasq 
- VPN                   : OpenVPN, StrongSWAN, Racoon, PPTP, xl2tpd
- Webcams               : crtmpserver, ...
- Email                 : mini­sendmail, mutt
- Monitoring            : Munin Lite, Nagios
- Databases             : MySQL, PostgreSQL, SQLite
- Web Servers           : uhttpd, apache, nginx, lighttpd
- Languages             : Perl, PHP, Python, Ruby, LUA, Erlang
- Printing              : CUPS
- Audio                 : ALSA, PulseAudio
- Video                 : ffmpeg
- Multimedia            : minidlna,miniupnp
- VoIP                  : Asterisk, Freeswitch, kamailio

Category:



Downloading

1. Create separate directory

          mkdir project
          cd project


2. Install git , to conveniently download the source code

          sudo apt-get install git


3. Download using following command

          git clone https://git.openwrt.org/openwrt/openwrt.git

Note : Do everything as normal user upto here, don't use root user or sudo!


Compiling

1. Installing in context of ./scripts/feeds script means “making package available in make menuconfig” rather than really installing or compiling package. Also, after you have been developing for a while, and your copy of the repository is getting behind, running “feeds update -a” will pull the latest updates for the feeds.

    Update feeds: 

              ./scripts/feeds update -a


    Make downloaded package/packages available in make menuconfig:

              ./scripts/feeds install <PACKAGENAME>

or

              ./scripts/feeds install -a


2. The build system configuration interface handles the selection of the target platform, packages to be compiled, packages to be included in the firmware file, some kernel options, etc. Start the build system configuration interface by writing the following command(root user):

            make menuconfig

It will open window as below shown, and select Target System

           Make menu1.png

3. If you want to build images for the Raspberry Pi select:

    In “Target System” choose “Broadcom BCM27xx”

Note: Use UP and DOWN arrow keys to select then press red circle marked select button

           Make menu2.png


    In “Sub Target” choose “BCM2710 64 bit based boards”

           Make menu3.png

    Select exit and save your settings.

            Make menu12.png

            Save1.png


Note : Install Dependencies before compiling. Type below command for Ubuntu. For other machines click Here

    sudo apt-get install build-essential subversion git-core libncurses5-dev zlib1g-dev gawk flex quilt libssl-dev xsltproc libxml-parser-perl mercurial bzr ecj cvs unzip


    Now build images using make command. That may take hours: 

            make V=s 


4. In case of error enter the following command

            export FORCE_UNSAFE_CONFIGURE=1
            apt-get install coreutils

Flash To SD card
Using Etcher App

Download 'Ethcher' from the below link and open downloaded App.

       https://etcher.io/
	https://www.balena.io/etcher/

       Etcher2.png

Then select the image, the images can be found in path ./bin/targets/brcm2708/brcm2710/, choose ext4 factory image and flash to SD card

       Image1.png

       Etcher.png
	https://wiki.globaledgesoft.com/index.php/File:Etcher.png


Etcher is typically the easiest option for most users to write images to SD cards, so it is a good place to start. If you're looking for more advanced options on Linux, you can use the standard command line tools below. Note: use of the dd tool can overwrite any partition of your machine. If you specify the wrong device in the instructions below, you could delete your primary Linux partition. Please be careful.
Using Command Line

       dd if=openwrt-brcm2708-bcm2710-rpi-3-ext4-factory.img.gz of=/dev/sdX status=progress

Here, if – input file (image path) of – output file (partition on SD card)

status = progress is optional to watch copying


    Pages with broken file links





DHCP Server

    By default the DHCP server(DNSMasq Package) is enabled and the IP address is configured as static 192.168.1.1

To see open make menuconfig and go to Base System -> dnsmasq

    Base System.png

    Dnsmasq.png

Note  : In order to set it up with a IP different from the default 192.168.1.1 follow any one of the method given below.

1. Using File :

go to the folder /etc/config/network change in folder itself.

   Nw1.png

2. Using Command Line :

Type following command

   uci set network.lan.ipaddr=192.168.1.199
   uci commit
   /etc/init.d/network restart

   Nw2.png

DHCP Client

In order to set it up as a DHCP client, follow anyone of the below steps.

1. Using command line type the following command

     uci set network.lan.proto=dhcp
     uci commit
     /etc/init.d/network restart

2. Open the folder /etc/config/network and do changes as shown below.

     Nw4.png


OpenWrt work as Access-Point

    Access-Point packages kmod-mac80211 and hostapd-common are by default enabled. 

    By default the wireless is Turned OFF. You can turn it ON in the /etc/config/wireless by changing disabled '1' to disabled '0'

or you can use Command Line:

     uci set wireless.@wifi-device[0].disabled=0; uci commit wireless; wifi

    Then restart the network configuration by using below command

     /etc/init.d/network restart


USB tethering is used to connect your OpenWrt-Router over your Smartphone with the Internet.

1. Enable below packages, after that compile it and flash to SD card ( To know how to compile and flash click Here.

    Kernel modules -> USB Support -> kmod-usb-net -> kmod-usb-net-rndis
    
    Usb-eth1.png   Usb-eth2.png

    Usb-eth3.png
  
    Usb-eth10.png

orElse use the Below command

    opkg update
    opkg install kmod-usb-net kmod-usb-net-rndis kmod-usb-net-cdc-ether


2. On the router use the new USB0 network interface as WAN connection and set the protocol to DHCP client mode.

    uci del network.wan
    uci set network.wan=interface
    uci set network.wan.ifname=usb0
    uci set network.wan.proto=dhcp
    uci commit network
    ifup wan

orElse open folder /etc/config/network and add following lines. Once added below lines, restart the network settings using /etc/init.d/network restart

    option interface 'wan'
           option ifname 'usb0'
           option proto 'dhcp'


3. On the Smartphone, connect it with the USB cable to your routers USB port and enable USB Tethering. To enable goto,

    Settings->More->USB tethering

Once you enable USB tethering, DHCP server running on smartphone will assign IP to the wan interface. 

The Raspberry Pi-3 board has only one network port, to get two or more network ports we can do one thing by using USB to Ethernet converter. But before we use USB to Ethernet converter we need to enable below mentioned packages in OpenWRT.

    In make menuconfig select

Kernel modules -> USB Support -> kmod-usb-net  
                              -> kmod-usb-net-dm9601-ether

  Usb-eth1.png   Usb-eth2.png

  Usb-eth3.png

  Usb-eth4.png


    Then Compile and flash the image into SD-card.( To know how to compile and flash click Here.


    To your Raspberry Pi USB port connect USB-Ethernet Adapter.

  Usb-eth6.png

once you connected adapter you should get the new mac address as below shown in figure.

  Usb-eth7.png


    Then open file /etc/config/network, and add eth1 Interface as below,

  Usb-eth8.png


    Then restart the network using below command.

  /etc/init.d/network retstart

    Type ifconfig in command line you will get new interface eth1 as below.

  Usb-eth9.png

Navigation menu

    Kr.miniga
    Talk
    Preferences
    Watchlist
    Contributions
    Log out

    Page
    Discussion

    Read
    Edit
    View history
    Watch

More

    Main page
    Recent changes
    Random page
    Help

Tools

    What links here
    Related changes
    Upload file
    Special pages
    Printable version
    Permanent link
    Page information


How to add our own package to OpenWrt

1) cd $(TOPDIR)/package

   TOPDIT is environment variable, which defined the proper path in your system 


2) Create a helloworld directory and then into the helloworld directory

  mkdir helloworld
  cd helloworld


3) Create a src directory and then into the src directory

  mkdir src
  cd src


4) Create helloworld.c and Makefile

  vim helloworld.c

  #include <stdio.h>
  int main(void)
  {
    printf(" hello world form OpenWrt !!! \n");
    return 0;
  }


5) vim Makefile

  #build a Makefile for helloworld.c
  helloworld: helloworld.o
       $(CC) $(LDFLAGS) helloworld.o -o helloworld
  helloworld.o: helloworld.c
    	$(CC) $(CFLAGS) -c helloworld.c
  clean:
    	rm *.o helloworld


6) Return to the HelloWorld directory

  cd ../

    Create Makefile

  vim Makefile


  ###############################################
  #OpenWrt Makefile for helloworld program
  ##############################################
  include $(TOPDIR)/rules.mk
  # Name and release number of this package
  PKG_NAME:=helloworld
  PKG_RELEASE:=1
  # This specifies the directory where we're going to build the program.
  # The root build directory, $(BUILD_DIR), is by default the  build_mipsel
  # directory in your OpenWrt SDK directory

  PKG_BUILD_DIR := $(BUILD_DIR)/$(PKG_NAME)
  include $(INCLUDE_DIR)/package.mk
  # Specify package information for this program.
  # The variables defined here should be self explanatory.
  # If you are running Kamikaze, delete the DESCRIPTION
  # variable below and uncomment the Kamikaze define
  # directive for the description below
  
  define Package/helloworld
       SECTION:=utils
       CATEGORY:=Utilities
       TITLE:=Helloworld -- prints a snarky message
  endef
  # Uncomment portion below for Kamikaze and delete DESCRIPTION variable above
  define Package/helloworld/description
     you have to figure out what this program does.
  endef

  # Specify what needs to be done to prepare for building the package.
  # In our case, we need to copy the source files to the build directory.
  # This is NOT the default.  The default uses the PKG_SOURCE_URL and the
  # PKG_SOURCE which is not defined here to download the source from the web.
  # In order to just build a simple program that we have just written, it is
  # much easier to do it this way.
  
  define Build/Prepare
          mkdir -p $(PKG_BUILD_DIR)
          $(CP) ./src/* $(PKG_BUILD_DIR)/
  endef
  # We do not need to define Build/Configure or Build/Compile directives
  # The defaults are appropriate for compiling a simple program such as   this one
  # Specify where and how to install the program. Since we only have one  file,
  # the helloworld executable, install it by copying it to the /bin directory on
  # the router. The $(1) variable represents the root directory on the router running
  # OpenWrt. The $(INSTALL_DIR) variable contains a command to prepare the install
  # directory if it does not already exist.  Likewise $(INSTALL_BIN) contains the
  # command to copy the binary file from its current location (in our case the build
  # directory) to the install directory.

  define Package/helloworld/install
          $(INSTALL_DIR) $(1)/bin
          $(INSTALL_BIN) $(PKG_BUILD_DIR)/helloworld $(1)/bin/
  endef
  # This line executes the necessary commands to compile our program.
  # The above define directives specify all the information needed, but this
  # line calls BuildPackage which in turn actually uses this information to build a package.

  $(eval $(call BuildPackage,helloworld))


7) Note : Provided screenshot below :

Package openwrt.png


8) Select Packages

  make menuconfig
  Utilities  --->  [*]helloworld


9) Compile Packages

    Back to $ (TOPDIR) directory and then compile:

     make package/helloworld/compile V=s

    This command is only to compile this package, so time will be shorter. If you compile successfully, you can see helloworld_1_ramips_24kec.ipk in the directory $(TOPDIR)/bin/ramips/packages. 

     make package/helloworld/clean V=s

    Of course, these two commands are used together:

     make package/helloworld/{clean,compile} V=s 

    If you want to compile the software package into the firmware, you need to use it: 

     make V=s


10) After dumping OpenWRT image into board Run helloworld

    helloworld 

    Program effect：

    hello world form OpenWrt !!!

Navigation menu

    Kr.miniga
    Talk
    Preferences
    Watchlist
    Contributions
    Log out

    Page
    Discussion

    Read
    Edit
    View history
    Watch

More

    Main page
    Recent changes
    Random page
    Help

Tools

    What links here
    Related changes
    Upload file
    Special pages
    Printable version
    Permanent link
    Page information

    This page was last modified on 24 October 2018, at 07:16.
    This page has been accessed 43 times.




