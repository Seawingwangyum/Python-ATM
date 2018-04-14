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

    def create_user_list(self):
        accnum = self.view.ask_number()
        name = self.view.ask_name()
        pin = self.view.ask_pin()
        type = self.view.ask_type()
        card = self.view.ask_card()
        bal = self.view.ask_balance()
        file = self.view.ask_file()
        return self.model.create_user_list(accnum, name, pin, type, card, bal, file)

    def write(self):
        self.model.write(self.view.edit_user(), self.create_user_list())

def main():
    while True:
        terminal = CLI()
        while True:
            login = terminal.view.v_login()
            password = terminal.view.v_password()
            initlogin = terminal.login(login, password)
            if initlogin == True:
                break

        terminal.write()




if __name__ == '__main__':
    main()
