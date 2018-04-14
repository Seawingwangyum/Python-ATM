#from Transactionlog import *
import datetime


class acc_info:

    def __init__(self, list):
        self.acc_num = list[0]
        self.name = list[1]
        self.password = list[2]
        self.acc_type = list[3]
        self.card_num= list[4]
        self.balance= int(list[5])
        self.transactionlog = list[6]
        self.transaction_history = []
        return


    @property
    def return_balance(self):
        return 'Balance is ${}'.format(self.balance)


    def withdraw(self, amount):
        if (amount <= self.balance) and (amount > 0):
            self.balance -= amount
            return True
        else:
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            return True
        else:
            return False


    def change_first_name(self, new_name):
        self.first_name = new_name
        return

    def change_last_name(self, new_name):
        self.last_name = new_name
        return
    """
    def charge_fee(self):
        self.balance = self.account_log.log_fee(account.__CHARGE_FEE, self.balance)
    """
    def save_to_transaction_history(self, transaction):
        now = datetime.datetime.now()
        self.transaction_history.append("{}-{}".format(now,transaction))
        return

    def display_transaction(self):
        pass

    def pay_interest(self):
        self.balance = self.balance
        return


if __name__ == "__main__":
    pass