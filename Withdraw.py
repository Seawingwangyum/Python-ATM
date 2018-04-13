from tkinter import *
from Controller import *
from tkinter import messagebox

class withdraw:

    def __init__(self, last_menu, parent, account):
        self.last_menu=last_menu
        self.master = parent
        self.account = account
        self.master.geometry("400x140")
        
        self.information_frame = Frame(self.master)
        self.button_frame = Frame(self.master)
        
        self.action_label = Label(self.information_frame,text="withdraw: ")
        self.withdraw_amount = Entry(self.information_frame, width=63)
        self.confirm_button = Button(self.master, text="Confirm", width=10, command = self.withdraw_money)

        self.information_frame.grid(row=0, column=0)

        self.action_label.grid(row=0,column=0, pady=10)
        self.withdraw_amount.grid(row=1, column=0, padx=10)
        self.button_frame.grid(row=1,column=0, pady=20)
        self.confirm_button.grid(row=1, column=0, padx=50, sticky=E)

    def withdraw_money(self):
        try:
            money = self.withdraw_amount.get()
            accepted = self.account.withdraw(int(money))
            if accepted == True:
                messagebox.showinfo(title="confirmation", message="you have withdrawied ${}".format(money))
                self.last_menu.deiconify()
                self.master.destroy()
        except ValueError:
            self.master.withdraw()
            messagebox.showinfo(title="Invalid", message="trevor is a soyboy")
            self.master.deiconify()
        
if __name__ == "__main__":
    root = Tk()
    withdraw(root, "hello")
    mainloop()