import sys
import socket
import fcntl
import struct
import time
from time import *
import os

import i2c_lcd_driver

class i2c_device_util:
	def __init__(self, dev_name, logging):
		self.io_name = dev_name
		self.logging = logging
		self.io_device = i2c_lcd_driver.i2c_device.lcd()

	###########################
	#   WRITE TO THE DISPLAY  #
	###########################
	def lcd_display_str(self, str_name, row, col, clr):
		self.io_device.lcd_clear() #CLEAR THE SCREEN The function mylcd.lcd_clear() clears the screen
		#mylcd.lcd_display_string() prints text to the screen and also lets you chose where to position
		self.io_device.lcd_display_string(str_name, 1)

	###########################
	#  BLINKING DISPLAY TEXT  #
	###########################
	def lcd_blink_text(self):
		while True:
			self.io_device.lcd_display_string(u"Hello world!")
			time.sleep(1)
			self.io_device.lcd_clear()
			time.sleep(1)

	###################################################################
	#                  PRINT YOUR IP ADDRESS                          #
	# This code prints IP address of your ethernet connection (eth0)  #
	# To print the IP of your WiFi connection, change eth0 to wlan0   #
	###################################################################
	def get_ip_address(self, ifname):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		return socket.inet_ntoa(fcntl.ioctl(
			s.fileno(),
			0x8915,
			struct.pack('256s', ifname[:15])
		)[20:24])
		io_device.lcd_display_string("IP Address:", 1)
		self.lcd_display_string(get_ip_address('eth0'), 2) #mylcd.lcd_display_string(get_ip_address('wlan0'), 2)

	#PRINT THE DATE AND TIME
	def lcd_display_time(self):
		self.io_device.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 1)
		self.io_device.lcd_display_string("Date: %s" %time.strftime("%m/%d/%Y"), 2)

	def lcd_scroll_text(self, b_continue, b_left2right):
		str_pad = " " * 16
		my_long_string = "This is a string that needs to scroll"
		my_long_string = str_pad + my_long_string

		while b_continue:
			for i in range (0, len(my_long_string)):
				lcd_text = my_long_string[i:(i+16)]
				self.io_device.lcd_display_string(lcd_text,1)
				sleep(0.4)
				self.io_device.lcd_display_string(str_pad,1)