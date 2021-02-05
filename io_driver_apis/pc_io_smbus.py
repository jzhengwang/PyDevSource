from common_utils.dbg_logging_util import DbgUtilityApi
from common_utils.gui_utility_functions import GuiUtility

dbg_log_name = "../dbg_log/dbg{file}log".format(file=__name__).replace("__", "_", -1)


class SMBus:
    def __init__(self, io_addr):
        self.addr = io_addr
        self.logging = DbgUtilityApi('DEBUG', 'main', dbg_log_name)
        self.lcd_gui = GuiUtility("Welcome", "Arial Bold", 0, 20, 0, "0x0", self.logging)
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
