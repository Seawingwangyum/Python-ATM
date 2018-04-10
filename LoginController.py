from tkinter import *
from tkinter import messagebox

from LoginScreen import loginscreen

class LoginController:
    def __init__(self, parent):
        self.master = parent
        self.login_gui = loginscreen(parent)

        self.login_gui.login_button.bind("<Click>", self.login)