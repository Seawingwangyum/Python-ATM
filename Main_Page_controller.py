from tkinter import *
from tkinter import messagebox
import csv
from Deposit import *
from Withdraw import *
from Check_Balance import *
from LoginController import *
from tempfile import NamedTemporaryFile
import shutil
from Controller import *


from Main_Page import MainWindow


class MainController:
    def __init__(self, parent, account):
        bank_account = self.open_file(account)
        self.account_info = acc_info(bank_account)
        self.master = parent
        self.main_gui = MainWindow(self.master, bank_account[1])

        self.main_gui.deposit_button.config(command=self.deposit)
        self.main_gui.withdraw_button.config(command=self.withdraw)
        self.main_gui.check_balance_button.config(command=self.check_balance)

    def open_file(self,account):
        with open('account.csv', 'r') as bank_accounts:
            csv_reader = csv.reader(bank_accounts)

            next(csv_reader)

            for line in csv_reader:
                if line[0] == account:
                    bank_account = line

        return bank_account

    def deposit(self):
        self.master.withdraw()
        self.newwindow = Toplevel(self.master)
        deposit(self.master,self.newwindow, self.account_info)
        
    def withdraw(self):
        self.master.withdraw()
        self.newwindow = Toplevel(self.master)
        withdraw(self.master, self.newwindow, self.account_info)

    def check_balance(self):
        #self.master.withdraw()
        self.newwindow = Toplevel()
        check_balance(self.master, self.newwindow, self.account_info)

        




if __name__ == "__main__":
    root = Tk()
    MainController(root,'10003')
    mainloop()
    write_file(['10004','Justin Salisi','1996', 'savings','12345678901234569','25000','10004.csv'])