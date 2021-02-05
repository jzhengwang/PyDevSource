import socket
import fcntl
import struct


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
    self.lcd_display_string(get_ip_address('eth0'), 2)  # mylcd.lcd_display_string(get_ip_address('wlan0'), 2)
