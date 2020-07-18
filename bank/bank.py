class Bank:
    def __init__(self):
        self.__customers = {}
        self.__transactions = []

    def add_customer(self, customer):
        self.__customers[customer.uuid] = customer

    def add_transaction(self, transaction):
        transaction
        self.__transactions.append(transaction)

    def process_transactions(self):
        for transaction in self.__transactions:
            costumer_source = self.__customers[transaction.source]
            costumer_receiver = self.__customers[transaction.receiver]
            transaction_date = transaction.date.strftime(r'%d/%m/%Y')

            if costumer_source.account.balance > transaction.amount:
                costumer_source.account.balance -= transaction.amount
                costumer_receiver.account.balance += transaction.amount

                print(
                    '{} transferiu R$ {} para {} no dia {}'
                    .format(costumer_source.name, transaction.amount,
                            costumer_receiver.name, transaction_date)
                )
            else:
                print(
                    '{} não pode transferir R$ {} para {} no dia {} por possuir saldo insuficiente (R$ {})'
                    .format(costumer_source.name, transaction.amount,
                            costumer_receiver.name, transaction_date,
                            costumer_source.account.balance)
                )

    def customers_balance(self):
        print('Saldos:')
        for _, customer in self.__customers.items():
            print('{} - R$ {}'.format(customer.name, customer.account.balance))
