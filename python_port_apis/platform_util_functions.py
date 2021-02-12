import platform
import sys


class platform_util:
    cpu_name: object
    pc_cpu_tuple = ("AMD64", "x86_64")
    pi_cpu_tuple = ("aarch64", "NULL")

    def __init__ ( self ):
        self.os_name = platform.uname().system
        self.os_version = platform.uname().version
        self.os_machine = sys.platform
        self.cpu_name = platform.uname().machine
        self.node_name = platform.uname().node
        self.py_version = platform.python_version()
        self.system_ver = sys.version
        self.system_hw = sys.platform

    def is_platform_pi(self):
        for cpu_name in self.pi_cpu_tuple:
            if self.cpu_name == "cpu_name":
                return True
        return False

    def is_platform_windows(self):
        if self.os_name == "Windows":
            return True, self.os_machine
        else:
            return False

    def is_platform_linux(self):
        if self.os_name == "Linux":
            return True, self.os_machine
        else:
            return False

    def is_platform_pc(self):
        for cpu_name in self.pc_cpu_tuple:
            if self.cpu_name == cpu_name:
                return True
        return False

    def get_node_name ( self ):
        return self.node_name

    def get_node_sys_info ( self ):
        return self.system_hw, self.system_ver

    def get_python_version ( self ) -> object:
        return self.py_version

    def get_cpu_name ( self ):
        return self.cpu_name
