from tkinter import *
from tkinter import messagebox
import csv
from Deposit import *
from Withdraw import *
from Check_Balance import *
from Main_Page import MainWindow
from Controller import *


class MainController:
    def __init__(self, parent, account):
        self.bank_account = self.open_file(account)
        self.acc_obj = acc_info(self.bank_account)
        self.master = parent
        self.main_gui = MainWindow(self.master, self.bank_account[1])

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
        self.newwindow = Toplevel()
        deposit(self.master ,self.newwindow, self.acc_obj)
        self.Cancelbutton()

        
    def withdraw(self):
        self.master.withdraw()
        self.newwindow = Toplevel(self.master)
        withdraw(self.master ,self.newwindow, self.acc_obj)
        self.Cancelbutton()

    def check_balance(self):
        self.master.withdraw()
        self.newwindow = Toplevel()
        check_balance(self.newwindow)
        self.Cancelbutton()

    def onCloseOtherFrame(self, otherframe):
        otherframe.destroy()
        self.master.deiconify()

    def Cancelbutton(self):
        self.cancel = lambda: self.onCloseOtherFrame(self.newwindow)
        self.button_frame = Frame(self.newwindow)
        self.cancel_button = Button(self.newwindow, text="Cancel", width=10,command=self.cancel)
        self.cancel_button.grid(row=1, column=0, sticky=W, padx=50)




if __name__ == "__main__":
    root = Tk()
    MainController(root,'10003')
    mainloop()