Aim

    To build linux kernel image for raspberrypi-3 and load it using U-boot.


Requirements

    Raspberry Pi 3-B board.
    Linux host system with OS version Ubuntu 16.04 or higher.
    USB PWR IN Cable (Type B USB Cable).
    Open network connection.
    Card reader.
    SD card (>=4Gb) with working U-boot.
        Note: To setup u-boot refer U-boot for Raspberry PI 3 in wiki.
    USB to serial cable.
        Connect Green color wire of serial cable to Pin10[RXD] of Raspberry Pi 3 .
        Connect White color wire of serial cable to Pin8[TXD] of Raspberry Pi 3.


Procedure

    Download and extract the latest linux kernel zip fle for raspberrypi from https://github.com/raspberrypi/linux
    Download and extract aarch64-linux-gnu toolchain from https://developer.arm.com/open-source/gnu-toolchain/gnu-a/downloads
    Inside linux-<version/ run the command

     $ make ARCH=arm64 bcmrpi3_defconfig

    Now compile using given command

     $ make ARCH=arm64 CROSS_COMPILE=/path/to/bin/directory/of/toolchain/aarch64-linux-gnu-  -j$(nproc)

    After building, kernel images (Image & Image.gz) can be found in linux-<version>/arch/arm64/boot/.
    Now to make kernel image u-boot compatible(uImage) we will use mkimage tool. If mkimage tool is not present you can get it by installing u-boot-tools package.
    Inside linux-<version>/arch/arm64/boot/ run the command.

     $ mkimage -A arm64 -O linux -C none -T kernel -K  dts/broadcom/bcm2837-rpi-3-b.dtb -a 0x08000000 -e 0x08000000\
     -n Raspberrypi3 -d Image uImage

    After the image has been created successfully, you should get an output similar to following.

Kernel mkimage.png

    Now connect the u-boot enabled SD card and copy the created uImage into the boot partition.
    Open minicom and powerup the Raspberry Pi 3 and thus board starts booting.
    If the u-boot is working properly you can see the u-boot prompt.
    To load kernel image run the below u-boot commands in u-boot prompt.

     fatload mmc 0 0x05000000 uImage
     bootm 0x05000000 - ${fdt_addr}

    Now you can see the kernel loading.

Buildroot.png


    Notes
        While loading kernel image if your board is resetting after giving an error saying Image too large:Increase CONFIG_SYS_BOOTM_LEN then increase CONFIG_SYS_BOOTM_LEN macro value in /buildroot-<version>/output/build/uboot-<version>/common/bootm.c file from 0x800000 to 0xf00000. Now build u-boot image again and try.
        Kernel load address for raspberrypi-3-B can be in between 0x0 – 0x39000000.For more information run bdinfo command in u-boot prompt.

References

    https://elinux.org/RPi_U-Boot
    https://www.raspberrypi.org/forums/viewtopic.php?t=134018&start=25
