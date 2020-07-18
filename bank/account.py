from decimal import Decimal


class Account:
    def __init__(self, balance):
        self.balance = Decimal(balance)
