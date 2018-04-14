from tkinter import *
from tkinter import messagebox
import csv
from tempfile import NamedTemporaryFile
import shutil
from Model import *
from SubmenuController import SubmenuControl
from Main_Page import MainWindow


class MainController:
    def __init__(self, last_menu, parent, account):
        bank_account = self.open_file(account)
        self.last_menu = last_menu
        self.account_info = acc_info(bank_account)
        self.master = parent
        self.main_gui = MainWindow(self.master, bank_account[1])

        self.main_gui.deposit_button.config(command=self.deposit)
        self.main_gui.withdraw_button.config(command=self.withdraw)
        self.main_gui.check_balance_button.config(command=self.check_balance)
        self.main_gui.check_history_button.config(command=self.check_history)
        self.main_gui.done_button.config(command=self.logout)


    def open_file(self,account):
        with open('account.csv', 'r') as bank_accounts:
            csv_reader = csv.reader(bank_accounts)

            next(csv_reader)

            for line in csv_reader:
                if line[0] == account:
                    bank_account = line

        return bank_account

    def deposit(self):
        self.hide_menu()
        SubmenuControl(self.master,self.newwindow, "deposit",self.account_info)
        
    def withdraw(self):
        self.hide_menu()
        SubmenuControl(self.master, self.newwindow, 'withdraw',self.account_info)

    def check_balance(self):
        self.hide_menu()
        SubmenuControl(self.master, self.newwindow, 'balance',self.account_info)

    def check_history(self):
        self.hide_menu()
        SubmenuControl(self.master, self.newwindow, "history", self.account_info)

    def hide_menu(self):
        self.master.withdraw()
        self.newwindow = Toplevel()
    
    def logout(self):
        self.account_info.write_to_logs()
        self.last_menu.deiconify()
        self.master.destroy()

        




if __name__ == "__main__":
    root = Tk()
    MainController("last window",root,'10003')
    mainloop()
    # write_file(['10004','Justin Salisi','1996', 'savings','12345678901234569','25000','10004.csv'])