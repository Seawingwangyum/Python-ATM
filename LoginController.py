
from tkinter import *
from tkinter import messagebox
import csv

from LoginScreen import loginscreen
from Main_Page import MainWindow

class LoginController:
    def __init__(self, parent):
        self.master = parent
        self.login_gui = loginscreen(parent)

        self.login_gui.login_button.bind("<Button-1>", self.login)


    def login(self, event = 'none'):
        all_accounts = []
        credit_card = self.login_gui.name_entry.get()
        pin = self.login_gui.pass_entry.get()
        with open('account.csv', 'r') as bank_accounts:
            csv_reader = csv.reader(bank_accounts)

            next(csv_reader)

            for line in csv_reader:
                user_exist = False
                password_correct = False
                if line[4] == credit_card:
                    user_exist = True
                    if line[2] == pin:
                        password_correct = True
                        all_accounts.append(line)

        if len(all_accounts) > 0:
            for user in all_accounts:
                MainWindow(self.master,user[0])

        elif not user_exist:
            messagebox.showinfo(title='Not in database', message='Credit Card Number is not in our Files')

        elif not password_correct:
            messagebox.showinfo(title='Incorrect Pin', message='Incorrect Pin, Please try again')



if __name__ == "__main__":
    root = Tk()
    LoginController(root)
    mainloop()