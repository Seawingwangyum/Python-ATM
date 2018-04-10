from tkinter import *
class withdraw:
    def __init__(self, parent):
        self.master = parent
        self.master.geometry("400x140")
        self.information_frame = Frame(self.master)
        self.button_frame = Frame(self.master)
        self.action_label = Label(self.information_frame,text="Withdraw: ")
        self.withdraw_amount = Entry(self.information_frame, width=63)
        self.cancel_button = Button(self.button_frame, text="Cancel", width=10)
        self.confirm_button = Button(self.button_frame, text="Confirm", width=10)
        self.information_frame.grid(row=0, column=0)
        self.button_frame.grid(row=1,column=0, pady=20)
        self.action_label.grid(row=0,column=0, pady=10)
        self.withdraw_amount.grid(row=1, column=0, padx=10)
        self.cancel_button.grid(row=0,column=0, padx=10)
        self.confirm_button.grid(row=0, column=1, padx=10)
if __name__ == "__main__":
    root = Tk()
    withdraw(root)
    mainloop()