from decimal import Decimal


class Transaction:
    def __init__(self, source, receiver, amount, date):
        self.source = source
        self.receiver = receiver
        self.amount = Decimal(amount)
        self.date = date
