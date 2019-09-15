https://github.com/AgarwalConsulting/learning-golang
https://github.com/Chennai-Golang




FROM GITHUB:
git clone https://github.com/jemcek/packETH.git
cd packETH
./autogen.sh (you will need aclocal,autoconf,autoheader and automake installed to run this)
autoreconf -f -i (optional if needed sometimes)
./configure
make
make install
./packETH

FROM SOURCEFORCE:
    1. 1)get the package from the DOWNLOAD page
    2. 2)unpack it: 
        tar xjvf packETH.x.y.tar.bz    (where x.y is the version you downloaded)
    3. 3)cd packETH
    4. 4)autoreconf -f -i (needed sometimes)
    5. 5)./configure
    6. 6)make 
    7. 7)make install   (optional)

Depending on your Linux distribution and type of installation additional packages may be needed. For example:

1) Centos 7.4 (minimal):
yum groupinstall 'Development Tools'
yum install gtk2-devel.x86_64

    2. 2)Ubuntu 18.04 server
sudo apt-get install build-essential
sudo apt-get install autoconf
sudo apt-get install pkg-config
sudo apt-get install gtk+2.0


LINUX PACKAGES (Ubuntu, Redhat, etc...): 
There are precompiled packages for many linux distribution available but normally they are not the latest versions. To install type as root or superuser:

Redhat, Centos: yum install packeth
Debian, Ubuntu: apt-get install packeth



mkdir Beaglebone
cd Beaglebone/
git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
cd linux/
make -j4 ARCH=arm CROSS_COMPILE=/home/shaik/Beaglebone/toolchain_blackbone/bin/arm-linux-gnueabi-  distclean
make -j4 ARCH=arm CROSS_COMPILE=/home/shaik/Beaglebone/toolchain_blackbone/bin/arm-linux-gnueabi-  multi_v7_defconfig
 make -j4 ARCH=arm CROSS_COMPILE=/home/shaik/Beaglebone/toolchain_blackbone/bin/arm-linux-gnueabi-

sudo make -j4 ARCH=arm CROSS_COMPILE=/home/shaik/Beaglebone/gcc-linaro-6.5.0-2018.12-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf- uImage dtbs LOADADDR=0x80008000 

git clone https://github.com/u-boot/u-boot
cd u-boot/
make -j4 ARCH=arm CROSS_COMPILE=/home/shaik/Beaglebone/gcc-linaro-6.5.0-2018.12-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf- distclean
make -j4 ARCH=arm CROSS_COMPILE=/home/shaik/Beaglebone/gcc-linaro-6.5.0-2018.12-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf- am335x_evm_config
make -j4 ARCH=arm CROSS_COMPILE=/home/shaik/Beaglebone/gcc-linaro-6.5.0-2018.12-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-

cd linux/
sudo make ARCH=arm CROSS_COMPILE=/home/shaik/Beaglebone/gcc-linaro-6.5.0-2018.12-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf- -j4 modules
sudo make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- INSTALL_MOD_PATH=/media/shaik/f051490a-dd8d-4b33-963b-68bfcd8c385a/ modules_install


https://embedjournal.com/kernel-compilation-beaglebone-black/
https://elinux.org/Building_BBB_Kernel
https://embedjournal.com/kernel-compilation-beaglebone-black/
https://longervision.github.io/2018/01/10/Embedded/beaglebone-black-uboot-kernel/
http://www.bootembedded.com/embedded-linux/building-embedded-linux-scratch-beaglebone-black/

