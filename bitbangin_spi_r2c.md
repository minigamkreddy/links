Installation & Setup

    Download Raspberry Pi OS from raspberrypi.org and flash it on SD Card.
	https://www.raspberrypi.org/
    For cross compilation refer procedure given on raspberry pi's .website
	https://www.raspberrypi.org/documentation/linux/kernel/building.md
    Have a zImage of the kernel in the sd card.

Enabling SPI Ports on Raspberry Pi

    Open the terminal and type "raspi-config".
    Go to interfacing options and enable "SPI".
    Reboot your Raspberry Pi.

Interfacing options.png
Spi menu.png
Interfacing ADC with Raspberry Pi
ADC MCP3202 Pins 	Raspberry Pi Ports
CS 	SPI0 CS0
CH0 	External Input Voltage
CH1 	External Input Voltage
Vss 	+5V
Din 	SPI0 MOSI
Dout 	SPI0 MISO
SCLK 	SPI0 SCLK
GND 	Ground

Note:

In the bit banging protocol we can configure any gpio pin as SCLK, MISO, MOSI, CS.
SPI protocol

For more information about SPI protocol refer the given link [1]
Initialization of ADC

For initialization of ADC(MCP3202) use following link: [2]
Bit banging for SPI
What is bit banging?

The bit banging is one of the serial communication technique. In this technique all the communication is handled by software instead of dedicated hardware. To transmit or receive data to/from the device, the configuration of gpio pins are done.
SPI Driver Implementation

Here, I have treated SPI slave as character device and, according to that, I have developed character device driver. Following function are used to implement the device driver for Bit banging SPI,

    module_init():
        alloc_chrdev_region()
        cdev_alloc()
        cdev_init()
        cdev_add()
        class_create()
        device_create()
        gpio_request()
        gpio_direction_output()
        gpio_direction_input()
        gpio_export()
    open()
    Read():
        gpio_set_value()
        gpio_get_value()
    module_exit()
        class_destroy()
        cdev_del()
        unregister_chrdev_region()
        gpio_unexport()
        gpio_free()

Algorithm for bit banging SPI

    Start
    Set the CS pin to low.
    Give some delay.
    Set the CLK pin to low.
    Give some delay.
    Set the Master Out Slave In (MOSI) pin to the first bit of the data to be sent.
    Read the state of the Master in Slave Out (MISO) to receive the first bit of data from slave.
    Set the CLK pin to high.
    Give some delay.
    Repeat the same procedure to send byte of data.
    Set the CS pin to high.
    Stop.

Working.png
Snapshots of setup and result
A.jpg
Rsz 12.jpg
Advantages of bit banging

    Choice of any gpio pins for any functionality.
    Absolute control over protocol.
    No need of dedicated hardware.

Disadvantages of bit banging

    In standard SPI hardware, SPI controller takes care of all the pulses, data shifting and timing but in the bit-banging you have to take every action yourself for each bit.
    Compared to dedicated hardware, more communication errors like glitches and jitters occur when bit banging is used.
    Consumes more time compared to the dedicated SPI hardware.

Reference

    https://lwn.net/Articles/532714/
    http://ww1.microchip.com/downloads/en/devicedoc/21034d.pdf
    https://www.raspberrypi.org/documentation/linux/kernel/building.md
    http://dlnware.com/theory/SPI-Transfer-Modes




I2C

Installation and Setup

    Download Raspberry Pi OS from raspberrypi.org and flash it on SD Card.(Link to download[[1]])

 // Flash raspbian image to SD card
 $ sudo dd if=2018-03-13-raspbian-stretch.img of=/dev/sdc status=progress
 // Connect USB to serial Cable:
  - Connect Green color wire of serial cable to Pin10[RXD] of Raspberry Pi 3
  - Connect White color wire of serial cable to Pin8[TXD] of Raspberry Pi 3

    For cross compilation refer procedure given on raspberry pi's website.click here to navigate[2]

    Have a zImage of the kernel in the SD card.

Enabling I2C Ports on Raspberry Pi

    Open the terminal and type "raspi-config".

    Go to interfacing options.

    Enable "I2C"

    Reboot your Raspberry Pi.


Interfacing options.png



Raspi-config.png



Enable i2c.png


Now , the i2c ports are enabled!!!!
I2C Protocol

For more information about I2C protocol refer given link [3]
Interfacing RTC with Raspberry Pi 3b
RTC DS1307 Pins 	Raspberry Pi Ports
SDA 	GPIO02 SDA1(pin - 03)
SCL 	GPIO03 SCL1(pin - 05)
VCC 	+5V(pin - 02 or 04)
GND 	Ground

Note: In bit banging protocol any gpio pin can be used as SDA, SCL pin.
Real Time Clock(RTC) DS1307

For more information about RTC(ds1307) refer the given link. [4] [5]
Bit banging for I2C
What is BIt banging?

The bit banging is one of the serial communication technique. In this technique all the communication is handled by software instead of dedicated hardware. To transmit or receive data to/from the device, the configuration of gpio pins are done.
I2C Driver Implementation

Here, I have treated I2C slave as character device and, according to that, I have developed character device driver. Following function are used to implement the device driver for Bit banging I2c,

    module_init():
        alloc_chrdev_region()
        cdev_alloc()
        cdev_init()
        cdev_add()
        class_create()
        device_create()
        gpio_request()
        gpio_direction_output()
        gpio_direction_input()
        gpio_export()
    open()
    Read():
        gpio_set_value()
        gpio_get_value()
    write()
        gpio_set_value()
        gpio_get_value()
    module_exit()
        class_destroy()
        cdev_del()
        unregister_chrdev_region()
        gpio_unexport()
        gpio_free()

Algorithm for bit banging I2C

    Writing to the RTC Register:
        Configure the SDA pin and SCL pin as Output pin.
        Start condition
        Send the slave address(7 bit) with write bit(1 bit)
        Change the direction of SDA pin from output to input
        Check the ACK bit
        Change the direction of SDA pin from input to output
        Send the register address(8 bit)
        Change the direction of SDA pin from output to input
        Check the ACK bit
        Send the data (8 bit)
        Change the direction of SDA pin from output to input
        Check the ACK bit
        Stop condition
    Reading data from RTC Register:
        Configure the SDA pin and SCL pin as Output pin.
        Start condition
        Send the slave address(7 bit) with write bit(1 bit)
        Change the direction of SDA pin from output to input
        Check the ACK bit
        Change the direction of SDA pin from input to output
        Send the register address(8 bit)
        Change the direction of SDA pin from output to input
        Check the ACK bit
        Change the direction of SDA pin from input to output
        Repeated start condition
        Send the slave address(7 bit) with Read bit(1 bit)
        Change the direction of SDA pin from output to input
        Check the ACK bit
        Read the data byte from register
        Change the direction of SDA pin from input to output
        Send the NACK bit
        Stop condition

Snapshots of setup and result
I2c.jpg
Advantages of bit banging

    Choice of any gpio pins for any functionality.
    Absolute control over protocol.
    No need of dedicated hardware.

Disadvantages of bit banging

    In standard I2C hardware, I2C controller takes care of all the ACK, NACk, data shifting and timing but in the bit-banging you have to take every action yourself for each bit.
    Compared to dedicated hardware, more communication errors like glitches and jitters occur when bit banging is used.
    Consumes more time compared to the dedicated I2C hardware.

References

    https://learn.sparkfun.com/tutorials/i2c
    https://datasheets.maximintegrated.com/en/ds/DS1307.pdf
    https://lwn.net/Articles/532714/
    https://www.raspberrypi.org/documentation/linux/kernel/building.md


