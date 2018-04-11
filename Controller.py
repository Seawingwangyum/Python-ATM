from Transactionlog import *


class account:

    __NEXT__ACCT_NUM = 10000
    __CHARGE_FEE = 10

    def __init__(self, balance=0, first_name="Anon", last_name = "nymous"):
        self.first_name = first_name
        self.last_name = last_name
        self.account_num = account.__NEXT__ACCT_NUM
        self.balance = balance
        self.account_log = Transaction_log()
        account.__NEXT__ACCT_NUM += 1
        return

    @property
    def full_name(self):
        fullname = "{} {}".format(self.first_name, self.last_name)
        return fullname

    @property
    def return_balance(self):
        return 'Balance is ${}'.format(self.balance)


    def withdraw(self, amount):
        if self.balance >= amount and amount >= 0:
            self.balance = self.account_log.log_withdraw(amount, self.balance, True)
        else:
            self.balance = self.account_log.log_withdraw(amount, self.balance, False)
        return

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.account_log.log_deposit(amount, self.balance, True)
        else:
            self.balance = self.account_log.log_deposit(amount, self.balance, False)
        return

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