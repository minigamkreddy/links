Introduction

U-boot which is also known as Das U-Boot, is an open source, primary boot loader used in embedded devices to package the instructions to boot the device's operating system kernel.

Here in this page we are going to

    Compile and build U-boot using Buildroot/Yocto.
    Introduce a test command into U-Boot command list.

Prerequisites

    Buildroot/Yocto latest version.
    Minimum 50GB of free disk space (for build using Yocto).
    Open network connection.
    Raspberry Pi 3 board.
    Micro SD card(4GB, 8GB, 16GB, 32GB).
    Card reader.
    USB to serial Cable.
        Connect Green color wire of serial cable to Pin10[RXD] of Raspberry Pi 3
        Connect White color wire of serial cable to Pin8[TXD] of Raspberry Pi 3
    USB PWR IN Cable (Type B USB Cable).

Procedure
Build using Buildroot

Buildroot is a tool which automates the building of a complete Linux system(U-boot, Linux kernel image) for an embedded system, using cross-compilation, which requires a good internet connection to download the required packages.

    Download the latest Buildroot from buildroot.org. 
	https://buildroot.org/download.html

    Extract the tar file. 

      $ tar -xvf buildroot-<version>.tar.gz

    Inside buildroot-<version>/ directory run the command 

      $ make raspberrypi3_64_defconfig

    Using this default configuration U-boot option is not selected, to select this option run 

      $ make menuconfig
	https://wiki.globaledgesoft.com/index.php/File:U-boot_option.png

    Select U-boot option under bootloaders.
	https://wiki.globaledgesoft.com/index.php/File:Board_defconfig.png

U-boot option.png


    Select board_defconfig and enter string as "rpi_3".

Board defconfig.png


    Disable Linux kernel option under kernel.

    Save the configuration.

    Make changes in buildroot-<version>/board/raspberrypi3-64/genimage-raspberrypi3-64.cfg as follows.

	https://wiki.globaledgesoft.com/index.php/File:Genimage_rpi3_64.png

Genimage rpi3 64.png


    To start the build process run (this takes time as it downloads and compiles all source files and toolchain).

      $ make

    Note: To build offline run [download all required source files according to the configuration].

      $ make source [which downloads source files to buildroot-<version>/dl/ and requires open network connection]
      $ make [to start build]

    If you get an error saying can’t find "Image", then rename "u-boot.bin" to "Image" in buildroot-<version>/output/images/ and run make again.

    If you get an error saying can’t find "bcm2837-rpi-3-b.dtb", then copy the file from buildroot-<version>/output/build/uboot-<version>/arch/arm/dts/ to buildroot-<version>/output/images/rpi-firmware/ and run make again.

    After successful building sdcard.img can be found in buildroot-<version>/output/images/.

    Copy the sdcard.img to SD card with the command

      $ sudo dd if=buildroot-<version>/output/image/sdcard.img of=/dev/sdX

Build using Yocto
Setting up host to use Yocto

    Install the essential packages for Ubuntu.

      $ sudo apt-get install gawk wget git-core diffstat unzip texinfo gcc-multilib \
      build-essential chrpath socat cpio python python3 python3-pip python3-pexpect \
      xz-utils debianutils iputils-ping libsdl1.2-dev xterm

    Clone the poky repository using the following command.

      $ git clone https://git.yoctoproject.org/git/poky

    Goto poky directory.

      $ cd poky

    Clone Raspberry Pi hardware support metadata and openembedded metadata.

      $ git clone https://git.yoctoproject.org/git/meta-raspberrypi
      $ git clone git://git.openembedded.org/meta-openembedded

Configure and build U-boot
Initialize the Yocto project’s build environment

    Run oe-init-build-env environment script to initialize the Yocto project's build environment.

      $ source oe-init-build-env [build-directory]
      The build-directory is an optional parameter where we perform the build, default is build.

Customizing build for Raspberry Pi 3

    Change the MACHINE variable in conf/local.conf to raspberrypi

      $ echo 'MACHINE = "raspberrypi" ' >> conf/local.conf

Note: To enable parallel make add the following lines to conf/local.conf

      $ echo 'BB_NUMBER_THREADS="4" ' >> conf/local.conf
      $ echo 'PARALLEL_MAKE="-j4" ' >> conf/local.conf

    Add hardware layer to layer configuration file conf/bblayers.conf

      $ bitbake-layers add-layer ../meta-raspberrypi

    To build U-boot run the command

      $ bitbake u-boot

    After build U-boot image can be found in build/tmp/deploy/images/raspberrypi/ directory.

Preparing SD card for booting

SD card needs to have msdos partition table with boot(formatted with FAT32) partition(size >20MB) to load the boot files and rest can be used for rootfs. Now follow the below steps to create partitions and add boot files to the SD card.

    Plug in the SD card and do dmesg to know the device.
    Now run the following commands to create partitions and format the partitions.

     $ sudo umount /dev/sdx* 
           (here replace x with that of dmesg output)
     $ sudo parted -s  /dev/sdx \
       mklabel msdos \
       mkpart primary fat32 1M 30M \
       mkpart primary ext4 30M 100%
     $ sudo mkfs.vfat /dev/sdx1
     $ sudo mkfs.ext4 /dev/sdx2

    Now mount boot partition to /mnt

     $ sudo mount /dev/sdx1 /mnt

    Copy the U-boot image to this partition.

     $ sudo cp -iv u-boot-raspberrypi-<version>.bin /mnt/

    Clone the Raspberry Pi's firmware 

     $ git clone https://github.com/raspberrypi/firmware.git

    Copy the minimum set of required files to the SD card.

     $ sudo cp -iv firmware/boot/{bootcode.bin,fixup.dat,start.elf,bcm2710-rpi-3-b.dtb,bcm2710-rpi-3-b-plus.dtb} /mnt/
     $ sudo cp -iv ./tmp/work/raspberrypi-poky-linux-gnueabi/u-boot/<u-boot_version>/build/arch/arm/dts/bcm2837-rpi-3-b.dtb /mnt/

    Create config.txt file in the boot partiton with the following content.

     kernel=u-boot.bin #replace u-boot.bin with the u-boot image copied to boot partition
     disable_overscan=1
     gpu_mem_256=100
     gpu_mem_512=100
     gpu_mem_1024=100
     arm_64bit=1
     enable_uart=1

    Create cmdline.txt file in the boot partition and write the following content.

     root=/dev/mmcblk0p2 rootwait console=tty1 console=ttyAMA0,115200

    Now unmount the SD card

     $ sync && sudo umount /mnt

Testing the bootloader

    Plugin the SD card to Raspberry Pi 3 board and make connections accordingly.
    Now open minicom and powerup the Raspberry Pi 3 and board starts booting.

	https://wiki.globaledgesoft.com/index.php/File:U-boot_boot_screen.png

     $ sudo minicom -D /dev/ttyUSBx

U-boot boot screen.png

    Press any key to stop autoboot.

Adding test command in U-boot
Add a test command

    Uboot commands are defined in files present in uboot-<version>/common directory.
    To add a new command create a file in the same format.
    Include the necessary header files depending on what the command would do.
    Add your command as "do_<command>" function. This is the function where you have to define the functionality of command.
    U_BOOT_CMD( ) function will include your command to the list of commands of u-boot
        U_BOOT_CMD(name,maxargs,repeatable,command,"usage","help")
            name: This is the name of the commad. This is not a string.
            maxargs: Maximum number of arguments this function takes.
            repeatable: Either 0 or 1 to indicate if autorepeat is allowed.
            command: Function pointer (*cmd)(struct cmd_tbl_s *, int, int, char *[]);
            usage: Short description. This is a string
            help: Long description. This is a string.
    Include the following line in common/Makefile to compile the command while building uboot

     obj-y += <command>.o

Workaround in Buildroot

    After make source, u-boot-<version>.tar.bz2 file can be found in buildroot-<version>/dl/uboot/.
    Extract the tar file using command 

     tar -xvf u-boot-<version>.tar.bz2

    Add the command as described above.
    Now remove old tar file and create new tar file in dl/u-boot-<version> directory using following command.

     tar -cvjSf u-boot-<version>.tar.bz2  u-boot-<version>

    Now compute the hash value for newly created tar file using command

     sha256sum  u-boot-<version>.tar.bz2

    Replace the hash value in buildroot-<version>/boot/uboot/uboot.hash with the new value and save.
    Now build u-boot using buildroot and test on board.

Note:

    If you have already built sdcard.img and trying to add a new command, then follow the below steps.
    Remove “.stamp_built” file in “buildroot-<version>/output/build/uboot-<version>/” directory.
    Run “make clean” in “buildroot-<version>/output/build/uboot-<version>/” directory.
    Remove “Image/zImage/u-boot.bin”, “sdcard.img” file in “buildroot-<version>/output/images/” directory.
    Add the command as described above.
    Now build u-boot using buildroot and test on board.

Workaround in Yocto

    After adding the hardware layer in the layer configuration file conf/bblayers.conf, run the command

    $ bitbake -c do_unpack u-boot

    Now we can find the u-boot source files at poky/build/tmp/work/raspberrypi-poky-linux-gnueabi/u-boot/1_2018.07-r0/git directory.
    Add command as described above.
    Now build the u-boot with the command

    $ bitbake u-boot

Note:

    If u-boot is already built and then you are trying to re-built u-boot with new test command, then run the command

    $ bitbake -c do_cleansstate u-boot

    And then add the command as mentioned above.

Some useful tips for Yocto

    To enable parallel make add the following lines to conf/local.conf

      $ echo 'BB_NUMBER_THREADS="4" ' >> conf/local.conf
      $ echo 'PARALLEL_MAKE="-j4" ' >> conf/local.conf

    Clone meta-openembedded if build isn't working

      $ git clone git://git.openembedded.org/meta-openembedded

    You can significantly speed up your build and guard against fetcher failures by using mirrors. To use mirrors, add these lines to your local.conf file in the Build directory:

    SSTATE_MIRRORS = "\
    file://.* http://sstate.yoctoproject.org/dev/PATH;downloadfilename=PATH \n \
    file://.* http://sstate.yoctoproject.org/2.4/PATH;downloadfilename=PATH \n \
    file://.* http://sstate.yoctoproject.org/2.5.1/PATH;downloadfilename=PATH \n \
    "
                       


References

    Buildroot doc.
    buildroot-version/docs/manual/manual.pdf
    https://github.com/lentinj/u-boot/blob/master/doc/README.commands
    https://www.yoctoproject.org/docs/current/brief-yoctoprojectqs/brief-yoctoprojectqs.html
    https://wiki.globaledgesoft.com/index.php/Yocto_Build_System
    https://git.yoctoproject.org/cgit/cgit.cgi/
    https://www.yoctoproject.org/software-overview/
