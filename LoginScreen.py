from tkinter import *

class loginscreen:

    def __init__(self, parent):
        self.username = ""
        self.password = ""
        self.master = parent
        self.master.geometry('300x170')
        # self.master.configure(background="pink")
        self.master.title("login window")

        self.name_frame = Frame(self.master)
        self.pass_frame = Frame(self.master)
        self.button_frame = Frame(self.master)
        self.empty_frame=Frame(self.master)

        self.name_label = Label(self.name_frame, text = "UserName: ", width=41)
        self.name_entry = Entry(self.name_frame, width=40)
        self.pass_label = Label(self.pass_frame, text = "Password: ", width=41)
        self.pass_entry = Entry(self.pass_frame, width=40)
        self.login_button = Button(self.button_frame, text="Login", width=30, height=2)
        
        self.name_frame.grid(row=0,  column=5, pady=5)
        self.pass_frame.grid(row=1,  column=5, pady=5)
        self.button_frame.grid(row=2,column=5, pady=5)

        self.name_label.grid(row=0, column=0, padx=5)
        self.name_entry.grid(row=1, column=0, padx=5)
        self.pass_label.grid(row=0, column=0, padx=5)
        self.pass_entry.grid(row=1, column=0, padx=5)
        self.login_button.grid(row=0, column=0, pady=10)

if __name__ == "__main__":
    root = Tk()
    loginscreen(root)
    mainloop()