class Terminal:
    def __init__(self):
        pass

    def options(self):
        print("\nOptions:\n1 - Edit Users\n2 - Add new Account\n3 - Delete Account\n4 - Logout")
        return input("\nEnter your option from above: ")

    def v_login(self):
        return input('\nUsername: ')

    def v_password(self):
        return input('Password: ')

    def v_login_success(self):
        print("Successfully Logged in.")

    def v_login_fail(self):
        print("Failed Login, please try again.")




#--------------edit users--------------
    def enter_user(self):
        return input("Enter user account card number: ")

    def edit_user(self):
        print("\nOptions:\n1 - Update/Change\n2 - Add user\n3 - Remove user")
        return input("\nEnter your option from above: ")

    def account_does_not_exist(self):
        print("\nAccount number does not exist. Please try again. ")

#-----------Add new Account------------

#askname
    def ask_name(self):
        return input("Enter account name: ")
#askpin
    def ask_pin(self):
        return input("Enter the password for this account (4 digits): ")
#asktype
    def ask_type(self):
        return input("Enter the type of account (Chequing, Savings): ")

    def ask_number(self):
        return input("Enter the account number (5 digits): ")

    def ask_card(self):
        return input("Enter the credit card number for this account (16 digits): ")

    def ask_balance(self):
        return input("Enter the balance: ")

    def ask_file(self):
        return input("Enter the filename of the transaction log: ")

    def account_success(self):
        print("New account created.")

    def account_fail(self):
        print("New account was unable to be created. Please re-enter info.")
#--------------------------------------



#-----------Delete Account---------------

    def ask_delete(self):
        return input("Enter the account name you would like to delete: ")

    def deleted_account(self, account):
        print("Account %s deleted." % account)

#----------------------------------------

if __name__ == '__main__':
    user = Terminal()
    option = user.options()
    while option != '5':
        if option == '1':
            option2 = user.edit_user()
            while option2 != '7':
                if option2 == '1':
                    user.account_info()
                elif option2 == '2':
                    user.change_account_type()
                elif option2 == '3':
                    user.change_account_name()
                elif option2 == '4':
                    user.removed_funds(user.remove_funds())
                elif option2 == '5':
                    user.added_funds(user.add_funds())
                elif option2 == '6':
                    user.transferred_funds(user.transfer_funds())
                elif option2 == '7':
                    option2
                else:
                    print('Invalid option')
                option = user.options()
