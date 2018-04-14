#from Transactionlog import *
import datetime
from write_file import *


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

    def withdraw(self, amount):
        # withdraws money from an account, and appends to logs
        if (amount <= self.balance) and (amount > 0):
            self.balance -= amount
            self.save_to_transaction_history("Withdrew - ${}".format(amount))
            self.update_balance()
            return True
        else:
            return False

    def deposit(self, amount):
        # deposits money into an account, and appends to logs
        if amount > 0:
            self.balance = self.balance + amount
            self.save_to_transaction_history("Deposited - ${}".format(amount))
            self.update_balance()
            return True
        else:
            return False

    def save_to_transaction_history(self, transaction):
        now = datetime.datetime.now()
        self.transaction_history.append(": {}- {}".format(now,transaction))
        self.write_to_logs()
        return

    def write_to_logs(self):
        with open(self.transactionlog, 'a') as translog:
            for action in self.transaction_history:
                translog.write("{}\n".format(action))

    def read_history_logs(self):
        try:
            history = []
            with open(self.transactionlog, 'r') as translog:
                lines = translog.readlines()
                for line in lines:
                    history.append(line.rstrip('\n'))
                return history
        except FileNotFoundError:
            self.write_to_logs()
        except TypeError:
            self.write_to_logs()

    def update_balance(self):
        account_list = [self.acc_num, self.name, self.password, self.acc_type, self.card_num, str(self.balance), self.transactionlog]
        write_file(1, account_list)

if __name__ == "__main__":
    pass