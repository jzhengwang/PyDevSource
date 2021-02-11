import platform
import sys


class platform_util:
    cpu_name: object

    def __init__(self):
        self.os_name = platform.uname().system
        self.os_version = platform.uname().version
        self.os_machine = sys.platform
        self.cpu_name = platform.uname().machine
        self.node_name = platform.uname().node
        self.py_version = platform.python_version()
        self.system_ver = sys.version
        self.system_hw = sys.platform

    def is_platform_pi(self):
        if self.cpu_name == "aarch64":
            return True
        else:
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
        if self.cpu_name == "AMD64":
            return True
        else:
            return False

    def get_node_name(self):
        return self.node_name

    def get_node_sys_info(self):
        return self.system_hw, self.system_ver

    def get_python_version(self) -> object:
        return self.py_version

    def get_cpu_name(self):
        return self.cpu_name
