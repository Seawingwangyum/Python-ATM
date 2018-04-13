#from Transactionlog import *


class acc_info:

    __NEXT__ACCT_NUM = 10000
    __CHARGE_FEE = 10

    def __init__(self, list):
        print(list)
        self.acc_num = list[0]
        self.name = list[1]
        self.password = list[2]
        self.acc_type = list[3]
        self.card_num= list[4]
        self.balance= int(list[5])
        self.Transactionlog = list[6]
        return


    @property
    def return_balance(self):
        return 'Balance is ${}'.format(self.balance)


    def withdraw(self, amount):
        if amount < 0 and amount >= self.balance:
            self.balance = self.balance + amount
            return True
        else:
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            return True
        else:
            return False


    def __str__(self):
        string = "{}, {}".format(self.account_num, self.full_name)
        return string

    def change_first_name(self, new_name):
        self.first_name = new_name
        return

    def change_last_name(self, new_name):
        self.last_name = new_name
        return

    def charge_fee(self):
        self.balance = self.account_log.log_fee(account.__CHARGE_FEE, self.balance)

    def show_transaction(self):
        self.account_log.print_transact(self.full_name)
        return

    def pay_interest(self):
        self.balance = self.balance
        return


if __name__ == "__main__":
    acc1 = account(1000)
    acc1.withdraw(100)
    acc1.withdraw(-100)
    acc1.withdraw(1000)

    acc1.deposit(100)
    acc1.deposit(0)
    acc1.deposit(-100)

    acc1.charge_fee()


    acc1.show_transaction()