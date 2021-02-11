from os import system, name


class TerminalFunctionApi:
    def __init__(self):
        self.name = name

    def clear(self):
        if self.name == 'nt':  # for windows
            _ = system('cls')
        else:
            _ = system('clear')

    @staticmethod
    def print_hi(userName):
        print("Hello " + userName + "! Welcome to PyCharm!")
