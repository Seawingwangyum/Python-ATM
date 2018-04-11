from tkinter import *
from tkinter import messagebox
import csv

from Main_Page import MainWindow


class MainController:
    def __init__(self, parent, account):
        bank_account = self.open_file(account)
        self.master = parent
        self.main_gui = MainWindow(self.master, bank_account[1])

        self.main_gui.deposit_button.bind("<Button-1>", self.deposit)
        self.main_gui.withdraw_button.bind("<Button-1>", self.withdraw)
        self.main_gui.check_balance_button.bind("<Button-1>", self.check_balance)

    def open_file(self,account):
        with open('account.csv', 'r') as bank_accounts:
            csv_reader = csv.reader(bank_accounts)

            next(csv_reader)

            for line in csv_reader:
                if line[0] == account:
                    bank_account = line

        return bank_account


    def deposit(self):
        pass

    def withdraw(self):
        pass

    def check_balance(self):
        pass

if __name__ == "__main__":
    root = Tk()
    MainController(root,'10003')
    mainloop()