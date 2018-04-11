from tkinter import *

class continue_screen:

    def __init__(self, parent):
        self.master = parent
        self.master.geometry('300x170')
        # self.master.configure(background="pink")
        self.master.title("Continue?")

        self.top_frame = Frame(self.master)
        self.bot_frame = Frame(self.master)

        self.continue_label=Label(self.top_frame, text="Are You Finished?", height=5, width=42)
        self.yes_button=Button(self.bot_frame, text="Yes", width=15)
        self.no_button=Button(self.bot_frame, text="No", width=15)

        self.top_frame.grid(row=0,column=0)
        self.bot_frame.grid(row=1, column=0)

        self.continue_label.grid(row=0, column=0)
        self.yes_button.grid(row=0, column=1, padx=10)
        self.no_button.grid(row=0, column=0, padx=10)

if __name__ == "__main__":
    root = Tk()
    continue_screen(root)
    mainloop()