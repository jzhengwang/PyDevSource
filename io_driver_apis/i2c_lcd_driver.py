# -*- coding: utf-8 -*-
# Original code found at:
# https://gist.github.com/DenisFromHR/cc863375a6e19dce359d

"""
Compiled, mashed and generally mutilated 2014-2015 by Denis Pleic
Made available under GNU GENERAL PUBLIC LICENSE

# Modified Python I2C library for Raspberry Pi
# as found on http://www.recantha.co.uk/blog/?p=4849
# Joined existing 'i2c_lib.py' and 'lcddriver.py' into a single library
# added bits and pieces from various sources
# By DenisFromHR (Denis Pleic)
# 2015-02-10, ver 0.1

"""
import os
import sys
from time import sleep

# i2c bus (0 -- original Pi, 1 -- Rev 2 Pi)
I2CBUS = 0  # WZ May need change for rock64
# LCD Address
ADDRESS = 0x3F  # WZ Need change for rock64

if sys.platform == 'linux' and os.uname().machine == "aarch64":
    import smbus
    rock64_platform = True
else:
    import io_driver_apis.pc_io_smbus as pc_io_smbus
    rock64_platform = False


class i2c_device:
    def __init__(self, addr, port=I2CBUS):
        self.addr = addr
        if rock64_platform:
            self.bus = smbus.SMBus(port)
        else:
            self.bus = pc_io_smbus.SMBus(port)

    # Write a single command
    def write_cmd(self, cmd):
        self.bus.write_byte(self.addr, cmd)
        sleep(0.0001)

    # Write a command and argument
    def write_cmd_arg(self, cmd, data):
        self.bus.write_byte_data(self.addr, cmd, data)
        sleep(0.0001)

    # Write a block of data
    def write_block_data(self, cmd, data):
        self.bus.write_block_data(self.addr, cmd, data)
        sleep(0.0001)

    # Read a single byte
    def read(self):
        return self.bus.read_byte(self.addr)

    # Read
    def read_data(self, cmd):
        return self.bus.read_byte_data(self.addr, cmd)

    # Read a block of data
    def read_block_data(self, cmd):
        return self.bus.read_block_data(self.addr, cmd)
