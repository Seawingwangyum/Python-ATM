from tkinter import *

class history:
    def __init__(self, parent):
        self.master = parent
        self.master.geometry("400x380")
        self.history_frame = Frame(self.master)
        self.history_list_frame = Frame(self.master)
        self.scrollbar_frame = Frame(self.history_list_frame)

        self.history_label = Label(self.history_frame, width=60,text="Account history:")
        self.history_list = Listbox(self.history_list_frame, width=50, height=15)
        self.history_scrollbar = Scrollbar(self.history_list_frame)
        self.return_button = Button(self.master, text="Return")

        self.history_frame.grid(row=0, column=0)
        self.history_list_frame.grid(row=1,column=0)
        # self.scrollbar_frame.grid(row=0,column=1)


        self.history_label.grid(row=0, column=0, pady=10)
        self.history_list.pack(side=LEFT)
        self.history_scrollbar.pack(side=RIGHT, fill=Y)
        self.return_button.grid(row=3, column=0, pady=20)

if __name__ == "__main__":
    root = Tk()
    history(root)
    mainloop()