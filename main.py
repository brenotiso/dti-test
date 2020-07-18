import sys
import os
from datetime import datetime
from bank.bank import Bank
from bank.account import Account
from bank.customer import Customer
from bank.transaction import Transaction


def parse_date(raw_date):
    year, month, day = map(int, raw_date.split('-'))

    return datetime(year, month, day)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        file = sys.argv[1]
        file_exists = os.path.isfile(file)
        if not file_exists:
            print("O arquivo de entrada não existe ou não foi encontrado.")
            sys.exit()
    else:
        print("Número inválido de argumentos. Informe o arquivo de entrada.")
        sys.exit()

    data_file = open(file, 'r')
    data_lines = data_file.readlines()
    data_file.close()

    bank = Bank()

    for line in data_lines:
        source_uuid, balance, name, date, amount, receiver_uuid = line.strip().split('-%p')

        account = Account(balance)
        customer = Customer(source_uuid, name, account)
        transaction = Transaction(
            source_uuid, receiver_uuid, amount, parse_date(date))

        bank.add_customer(customer)
        bank.add_transaction(transaction)

    bank.process_transactions()

    bank.customers_balance()
