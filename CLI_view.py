class Terminal:
    def __init__(self):
        pass

    def options(self):
        print("\nOptions:\n1 - Edit Users\n2 - Add new Account\n3 - Delete Account\n4 - Logout")
        return input("\nEnter your option from above: ")

    def v_login(self):
        return input('Username: ')

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
        print("\nOptions:\n1 - View Account Info\n2 - Change Account Type\n3 - Change Account Name\n4 - Remove Funds")
        print("5 - Add Funds\n6 - Transfer Funds\n7 - Back")
        return input("\nEnter your option from above: ")

    def account_info(self):
        print("\nAccount Info")

    def account_does_not_exist(self):
        print("\nAccount number does not exist. Please try again. ")
#-------------------

    def change_account_type(self):
        print("\nOptions:\n1 - Account\n2 - Account\n 3 - Account\nBack")
        return input("Enter option: ")

    def changed_account_type(self, new_type):
        print("Changed account type to %s." % new_type)
#-------------------

    def change_account_name(self):
        return input("Enter new Account name: ")

    def changed_account_name(self, new_name):
        print("Changed account name to %s." % new_name)
#-------------------

    def remove_funds(self):
        return input("Enter amount to remove: ")

    def removed_funds(self, amount):
        print("Removed %s from Account." % amount)

#-------------------

    def add_funds(self):
        return input("Enter amount to add: ")

    def added_funds(self, amount):
        print("Added %s to Account." % amount)

#-------------------

    def transfer_to(self):
        return input("Enter account name you would like to transfer funds to: ")

    def transfer_funds(self):
        return input("Enter amount to transfer: ")

    def transferred_funds(self, account, amount):
        print("Trasnferred $%s to %s." % amount, account)

#-------------------------------------



#-----------Add new Account------------

#askname
    def ask_name(self):
        return input("Enter new account name: ")
#askpin
    def ask_pin(self):
        return input("Enter the password for this account: ")
#asktype
    def ask_type(self):
        print("\nAccount1 \nAccount2 \nAccount3")
        return input("Enter what type of account will be made using options above: ")

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
