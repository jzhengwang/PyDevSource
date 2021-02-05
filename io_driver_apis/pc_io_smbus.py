from common_utils.dbg_logging_util import DbgUtilityApi
from common_utils.gui_utility_functions import GuiUtility
from datetime import *

dbg_log_name = "../dbg_log/dbg{file}log".format(file=__name__).replace("__", "_", -1)
new_date_time = datetime.now()
date_only = '{0:%Y-%m-%d}'.format(new_date_time)
time_only = '{:%H:%M:%S}'.format(new_date_time)
current_date = "LCD Screen Simulator: {date} Time:{time}".format(date=date_only, time=time_only)


class SMBus:
    def __init__(self, io_addr):
        self.addr = io_addr
        self.logging = DbgUtilityApi('DEBUG', 'main', dbg_log_name)
        self.lcd_gui = GuiUtility(current_date, "Arial Bold", 20, 20, 10, "400x80", self.logging)
        self.lcd_gui.open_info_window("Hello World!", 0)
        self.cmd = 0
        self.data = 0

    def write_byte(self, io_addr, cmd):
        self.addr = io_addr
        self.cmd = cmd

    def write_byte_data(self, addr, cmd, data):
        self.addr = addr
        self.cmd = cmd
        self.data = data

    def read_byte(self):
        pass

    def read_byte_data(self, data):
        pass

    def read_block_data(self, cmd):
        pass
