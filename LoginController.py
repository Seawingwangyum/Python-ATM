from tkinter import *
from tkinter import messagebox
import csv
from Main_Page_controller import *
from LoginScreen import loginscreen


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
                self.newwindow = Toplevel()
                self.master.withdraw()
                MainController(self.newwindow,user[0])
                self.logout = lambda: self.onCloseOtherFrame(self.newwindow)
                self.logout_button = Button(self.newwindow, text="done", command=self.logout)
                self.logout_button.grid(row=2, padx=5, pady=10)
                self.login_gui.name_entry.delete(0,'end')
                self.login_gui.pass_entry.delete(0,'end')

        elif not user_exist:
            messagebox.showinfo(title='Not in database', message='Credit Card Number is not in our Files')

        elif not password_correct:
            messagebox.showinfo(title='Incorrect Pin', message='Incorrect Pin, Please try again')

    def onCloseOtherFrame(self, otherframe):
        otherframe.destroy()
        self.master.deiconify()



if __name__ == "__main__":
    root = Tk()
    LoginController(root)
    mainloop()
