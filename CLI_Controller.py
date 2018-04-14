from CLI_Model import CLI_Model
from CLI_view import *

class CLI:

    def __init__(self):
        self.view = Terminal()
        self.model = CLI_Model()

    def login(self, login, password):
        model_output = self.model.m_login(password, login)
        if model_output == True:
            self.view.v_login_success()
            return True
        else:
            self.view.v_login_fail()
            return False

    def view_account_info(self, card):
        model_output = self.model.account_info(card)
        if model_output == '':
            self.view.account_does_not_exist()
        else:
            self.view.account_info()

if __name__ == '__main__':
    terminal = CLI()
    while True:
        login = terminal.view.v_login()
        password = terminal.view.v_password()
        initlogin = terminal.login(login, password)
        if initlogin == True:
            break

    terminal.view.options()
