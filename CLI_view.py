class Terminal:
    def __init__(self):
        print("Login\n")
        self.username = input('Username: ')
        self.password = input('Password: ')

    def options(self):
        print("\nOptions:\n1 - Edit Users\n2 - Add new Account\n3 - Delete Account\n4 - ATM Maintenance\n5 - Logout")
        return input("\nEnter your option from above: ")
#--------------edit users--------------
    def enter_user(self):
        return input("Enter user account name: ")

    def edit_user(self):
        print("\nOptions:\n1 - View Account Info\n2 - Change Account Type\n3 - Change Account Name\n4 - Remove Funds")
        print("5 - Add Funds\n6 - Transfer Funds\n7 - Back")
        return input("\nEnter your option from above: ")

    def account_info(self):
        print("\nAccount Info")

    def change_account_type(self):
        print("\nOptions:\n1 - Account\n2 - Account\n 3 - Account\nBack")
        return input("Enter option: ")

    def change_account_name(self):
        return input("Enter new Account name: ")
        print("Account name changed.")

#-------------------------------------

if __name__ == '__main__':
    user = Terminal()
    option = user.options()
    if option == '1':
        user.enter_user()
        option2 = user.edit_user()
        if option2 == '1':
            user.account_info()
        elif option2 == '2':
            user.change_account_type()
        elif option == '3':
            user.change_account_name()
