from tkinter import *

class history:
    def __init__(self, parent):
        self.master = parent
        self.master.geometry("400x380")
        self.history_frame = Frame(self.master)

        self.history_label = Label(self.history_frame, width=56,text="Account history:")
        self.history_list = Listbox(self.history_frame, width=40, height=15)
        self.return_button = Button(self.master, text="Return")

        self.history_frame.grid(row=0, column=0)


        self.history_label.grid(row=0, column=0, pady=10)
        self.history_list.grid(row=1,column=0)
        self.return_button.grid(row=1, column=0, pady=20)

if __name__ == "__main__":
    root = Tk()
    history(root)
    mainloop()