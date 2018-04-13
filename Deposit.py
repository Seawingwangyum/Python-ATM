from tkinter import *
from Controller import *
from tkinter import messagebox

class deposit:

    def __init__(self, last_menu, parent, account):
        self.last_menu=last_menu
        self.master = parent
        self.account = account
        self.master.geometry("400x140")
        
        self.information_frame = Frame(self.master)
        self.button_frame = Frame(self.master)
        
        self.action_label = Label(self.information_frame,text="Deposit: ")
        self.deposit_amount = Entry(self.information_frame, width=63)
        self.cancel_button = Button(self.master, text="Cancel", width=10, command=self.cancel_transaction)
        self.confirm_button = Button(self.master, text="Confirm", width=10, command = self.deposit_money)

        self.information_frame.grid(row=0, column=0)

        self.action_label.grid(row=0,column=0, pady=10)
        self.deposit_amount.grid(row=1, column=0, padx=10)
        self.button_frame.grid(row=1,column=0, pady=20)
        self.cancel_button.grid(row=1, column=0,padx=50, sticky=W)
        self.confirm_button.grid(row=1, column=0, padx=50, sticky=E)

    def deposit_money(self):
        try:
            money = self.deposit_amount.get()
            accepted = self.account.deposit(int(money))
            if accepted == True:
                self.master.withdraw()
                messagebox.showinfo(title="confirmation", message="you have depositied ${}".format(money))
                self.master.deiconify()
                self.last_menu.deiconify()
                self.master.destroy()
        except ValueError:
            self.master.withdraw()
            messagebox.showinfo(title="Invalid", message="trevor is a soyboy")
            self.master.deiconify()

    def cancel_transaction(self):
        self.last_menu.deiconify()
        self.master.destroy()
        
if __name__ == "__main__":
    root = Tk()
    deposit(root, "hello")
    mainloop()