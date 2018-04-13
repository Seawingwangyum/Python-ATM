from tkinter import *
class check_balance:
    def __init__(self, last_menu, parent, account):
        self.last_menu = last_menu
        self.master = parent
        self.account = account
        self.master.geometry("400x420")
        self.information_frame = Frame(self.master)
        self.history_frame = Frame(self.master)
        
        self.action_label = Label(self.information_frame,text="Total Balance: ")
        self.balance_amount = Label(self.information_frame, text="${}".format(self.account.balance), width=55)

        self.history_label = Label(self.history_frame, text="Account history:")
        self.history_list = Listbox(self.history_frame, width=40, height=15)
        
        
        self.information_frame.grid(row=0, column=0)
        self.history_frame.grid(row=1, column=0)

        self.action_label.grid(row=0,column=0, pady=10)
        self.balance_amount.grid(row=1, column=0, padx=10)

        self.history_label.grid(row=0, column=0, pady=10)
        self.history_list.grid(row=1,column=0)

if __name__ == "__main__":
    root = Tk()
    check_balance(root)
    mainloop()