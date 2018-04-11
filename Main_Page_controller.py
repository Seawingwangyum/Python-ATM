from tkinter import *
from tkinter import messagebox
import csv

from Main_Page import MainWindow


class MainController:
    def __init__(self, parent):
        self.master = parent
        self.main_gui = MainWindow(parent)

        self.main_gui.deposit_button.bind("<Button-1>", self.deposit)
        self.main_gui.withdraw_button.bind("<Button-1>", self.withdraw)
        self.main_gui.check_balance_button.bind("<Button-1>", self.check_balance)


    def deposit(self):
        pass

    def withdraw(self):
        pass

    def check_balance(self):
        pass