from tkinter import *
from Deposit import *
from Withdraw import *
from Balance import *
from History import *

# determines what menu is supposed to be o
class SubmenuControl:
    def __init__(self, last_menu, parent, option, account):
        self.last_menu = last_menu
        self.master = parent
        self.option = option
        self.account = account

        if option == "deposit":
            self.open_deposit()
            
        elif option == "withdraw":
            self.open_withdraw()
        
        elif option == "balance":
            self.open_balance()

        else:
            self.open_history()

    def deposit_money(self):
        try:
            money = self.deposit_gui.deposit_amount.get()
            accepted = self.account.deposit(int(money))
            if accepted == True:
                self.master.withdraw()
                messagebox.showinfo(title="confirmation", message="you have depositied ${}".format(money))
                self.last_menu.deiconify()
                self.master.destroy()
            else:
                messagebox.showinfo(title="Invalid", message="Selection Invalid")
        except ValueError:
            self.master.withdraw()
            messagebox.showinfo(title="Invalid", message="Selection Invalid")
            self.master.deiconify()

    def withdraw_money(self):
        try:
            money = self.withdraw_gui.withdraw_amount.get()
            accepted = self.account.withdraw(int(money))
            if accepted == True:
                self.master.withdraw()
                messagebox.showinfo(title="confirmation", message="you have withdrawed ${}".format(money))
                self.master.deiconify()
                self.last_menu.deiconify()
                self.master.destroy()
            else:
                messagebox.showinfo(title="Invalid", message="Selection Invalid")
        except ValueError:
            self.master.withdraw()
            messagebox.showinfo(title="Invalid", message="Selection Invalid")
            self.master.deiconify()

   
    def cancel_transaction(self):
        self.last_menu.deiconify()
        self.master.destroy()

    def open_deposit(self):
        self.deposit_gui = deposit(self.master)
        self.deposit_gui.cancel_button.config(command=self.cancel_transaction)
        self.deposit_gui.confirm_button.config(command = self.deposit_money)

    def open_withdraw(self):
        self.withdraw_gui = withdraw(self.master)
        self.withdraw_gui.cancel_button.config(command=self.cancel_transaction)
        self.withdraw_gui.confirm_button.config(command = self.withdraw_money)

    def open_balance(self):
        self.balance_gui = balance(self.master)
        self.balance_gui.balance_amount["text"] = "${}".format(self.account.balance)
        self.balance_gui.back_button.config(command=self.cancel_transaction)

    def open_history(self):
        self.history_gui = history(self.master)
        self.history_gui.return_button.config(command=self.cancel_transaction)
        self.history_gui.history_list.config(yscrollcommand=self.history_gui.history_scrollbar.set)
        for entry in self.account.read_history_logs():
            self.history_gui.history_list.insert(END, entry)