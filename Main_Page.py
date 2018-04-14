from tkinter import *
from tkinter import messagebox


class MainWindow:

    def __init__(self, parent, account):

        # create any instances of other support classes that are needed and save them
        # as attributes of this window
        self.username = account
        self.master = parent
        self.master.title('Main')
        # set main window attributes such as title, geometry etc
        #
        self.master.geometry('600x500')


        self.top_frame = Frame(self.master)
        self.options_frame = Frame(self.master)
        self.bottom_frame = Frame(self.master)

        self.top_frame.grid(row=0, pady=5, padx=110)
        self.options_frame.grid(row=1, pady=5, padx=110)
        self.bottom_frame.grid(row=2, pady=5, padx=110)

        # set up menus if there are any
        #
        # define/create widgets and bind to events
        #
        self.Welcome_label = Label(self.top_frame, font=100, height=3, text='Welcome '+self.username+"!")
        self.deposit_button = Button(self.options_frame, width=50, height=3, text="Deposit", pady=5)
        self.withdraw_button = Button(self.options_frame, width=50, height=3, text="Withdraw", pady=5)
        self.check_balance_button = Button(self.options_frame, width=50, height=3, text="Check Balance", pady=5)
        self.check_history_button = Button(self.options_frame, width=50, height=3, text="Check History", pady=5)
        self.done_button = Button(self.bottom_frame, height=1, width=7, text="Done")

        # place widgets in window (ie use pack or grid or whatever layout manager to place widgets)
        #
        self.Welcome_label.grid(row=0, padx=5, pady=5)
        self.deposit_button.grid(row=0,padx=5, pady=10)
        self.withdraw_button.grid(row=1, padx=5, pady=10)
        self.check_balance_button.grid(row=2, padx=5, pady=10)
        self.check_history_button.grid(row=3, padx=5, pady=10)
        self.done_button.pack(side=RIGHT, padx=5, pady=20)



    ##################
    # now we define command and/or callback functions as needed
    #

    #def _command1(self):
    #    pass

    #def _command2(self):
    #    pass


if __name__ == "__main__":
    root = Tk()
    MainWindow(root, 'Linden')
    mainloop()