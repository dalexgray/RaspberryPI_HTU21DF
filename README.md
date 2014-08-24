RaspberryPI_HTU21DF
===================
This is a python driver to use with Adafruit's HTU21D-F breakout board.
https://www.adafruit.com/product/1899

This driver requires the pigpio library, available at http://abyz.co.uk/rpi/pigpio/index.html

To install this library please navagate to its folder and sudo python HTU21DF.py install

I wanted to use this sensor in a project with a Raspberry Pi but I only found drivers written in C, so I wrote my own.

Please keep in mind that it does not use every function offered by the sensor.  When temperature and humidity are read the i2c clock is held though there is a no hold mode available.  I also have not writted functions to read and write to the user register.
The only functions are read_temperature, read_humidity, and reset.

If you use an old revision A Raspberry Pi you will have to change the i2c bus in the driver from 1 to 0.
