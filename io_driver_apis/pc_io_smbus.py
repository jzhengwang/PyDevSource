class SMBus():
    def __init__(self, addr):
        self.addr = addr

    def write_byte(self, cmd):
        self.cmd = cmd

    def write_byte_data(self, addr, cmd, data):
        self.data = data

    def read_byte(self):
        pass

    def read_byte_data(self, data):
        pass

    def read_block_data(self, cmd):
        pass
