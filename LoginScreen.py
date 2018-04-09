from tkinter import *

class loginscreen:

    def __init__(self, parent):
        self.username = ""
        self.password = ""
        self.master = parent

        self.label_frame = Frame(self.master)
        self.entry_frame = Frame(self.master)
        self.button_frame = Frame(self.master)
        self.name_label = Label(self.label_frame, text = "UserName: ")
        self.name_entry = Entry(self.entry_frame)
        self.pass_label = Label(self.label_frame, text = "Password: ")
        self.pass_entry = Entry(self.entry_frame)
        self.login_button = Button(self.button_frame, text="Login")
        
        self.label_frame.grid(row=0, pady=5)
        self.entry_frame.grid(row=1, pady=5)
        self.button_frame.grid(row=2, pady=5)
        self.name_label.grid(sticky=W, row=0, column=0, padx=5)
        self.name_entry.grid(row=0, column=0, padx=5)
        self.pass_label.grid(row=0, column=1, padx=5)
        self.pass_entry.grid(row=0, column=1, padx=5)
        self.login_button.grid(row=0, column=0)

if __name__ == "__main__":
    root = Tk()
    loginscreen(root)
    mainloop()