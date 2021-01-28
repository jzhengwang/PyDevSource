# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from math import *
from matplotlib import *


class MathSymbolsMap:
    def __init__ ( self ):
        self.SymDict = {
            "+": "+",
            "-": "-",
            "*": "×",
            "/": "÷",
            "'": "$$f'",
            "**": "$x^p$",
            "inf": "$\infty$",
        }

        self.FuncDict = (
            ",",
        )

    def update_math_Sym_dict ( self, key, Sym ):
        self.SymDict.update({key: Sym})

    def show_math_sym_list ( self ):
        xDict = self.SymDict.values()
        print(xDict)
