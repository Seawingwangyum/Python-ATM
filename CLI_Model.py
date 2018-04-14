import csv
from tempfile import NamedTemporaryFile
import shutil
from write_file import write_file

class CLI_Model:

    def __init__(self):
        pass


    def m_login(self, password, num):
        user_exist = False
        password_correct = False
        account_num = num
        pin = password
        with open('admin.csv', 'r') as admin_accounts:
            csv_reader = csv.reader(admin_accounts)

            next(csv_reader)

            for line in csv_reader:
                if line[0] == account_num:
                    user_exist = True
                    if line[2] == pin:
                        password_correct = True

        if user_exist == True and password_correct == True:
            return True
        else:
            return False

#-------------edit users----------

    def remove_funds(self, account, amount):
        with open('account.csv', 'r') as user_accounts:
            csv_reader = csv.reader(user_accounts)

            next(csv_reader)

            for line in csv_reader:
                if line[4] == account:
                    if line[5] >= amount:
                        line[5] -= amount
                else:
                    return ''

    def create_user_list(self, number, name, pin, type, cc, balance, file):
        return [number, name, pin, type, cc, balance, file]

    def write(self, option, account):
        return write_file(option, account)

    def edit_users(self, number, name, pin, type, cc, balance, file):
        write_file()
