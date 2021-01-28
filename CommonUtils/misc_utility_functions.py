# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep


class TerminalFunctionApi:
    def __init__(self):
        self.name = name

    def clear(self):
        if self.name == 'nt':  # for windows
            _ = system('cls')
        else:
            _ = system('clear')

    def print_hi(self, userName):
        print("Hello " + userName + "! Welcome to PyCharm!")
