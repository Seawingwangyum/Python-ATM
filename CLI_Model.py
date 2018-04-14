import csv

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

#-------------edit users----------------

    def account_info(self, account):
        with open('account.csv', 'r') as user_accounts:
            csv_reader = csv.reader(user_accounts)

            next(csv_reader)

            for line in csv_reader:
                if line[4] == account:
                    return line
                else:
                    return ''

    def change_account_type(self, account, new_type):
        with open('account.csv', 'r') as user_accounts:
            csv_reader = csv.reader(user_accounts)

            next(csv_reader)

            for line in csv_reader:
                if line[4] == account:
                    line[3] = new_type
                else:
                    return ''

    def change_account_name(self, account, new_name):
        with open('account.csv', 'r') as user_accounts:
            csv_reader = csv.reader(user_accounts)

            next(csv_reader)

            for line in csv_reader:
                if line[4] == account:
                    line[1] = new_name
                else:
                    return ''

    def remove_funds(self, account, amount):
        pass
