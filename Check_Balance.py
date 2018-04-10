from tkinter import *
class check_balance:
    def __init__(self, parent):
        self.master = parent
        self.master.geometry("400x140")
        self.information_frame = Frame(self.master)
        self.button_frame = Frame(self.master)
        self.action_label = Label(self.information_frame,text="Total Balance: ")
        self.balance_amount = Label(self.information_frame, text="$XXXXXXXXXXXXXXXXXX", width=55)
        self.back_button = Button(self.button_frame, text="Back", width=10)
        self.information_frame.grid(row=0, column=0)
        self.button_frame.grid(row=1,column=0, pady=20)
        self.action_label.grid(row=0,column=0, pady=10)
        self.balance_amount.grid(row=1, column=0, padx=10)
        self.back_button.grid(row=0,column=0, padx=10)
if __name__ == "__main__":
    root = Tk()
    check_balance(root)
    mainloop()