import datetime
import pytz


class Account:
    """Simple account class with balance."""

    @staticmethod
    def current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [(Account.current_time(), balance)]
        print("Account created for " + self.name)
        self.show_balance()

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account.current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account.current_time(), -amount))
        else:
            print("Insufficient Balance!!!")
        self.show_balance()

    def show_balance(self):
        print("Balance: {}.".format(self.balance))

    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"

            else:
                tran_type = "withdrawn"
                amount *= -1

            print("{:5} {:5} is {} on {} (local time was {}).".format(self.name, amount, tran_type, date, date.astimezone()))

if __name__ == '__main__':
    alex = Account('Alex',100)
    alex.show_balance()

    alex.deposite(1500)
    alex.show_balance()
    alex.withdraw(450)
    alex.show_transaction()

    steph = Account('Steph', 800)
    steph.deposite(100)
    steph.withdraw(200)
    steph.show_transaction()