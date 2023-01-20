"""This module represents a bank"""
class Bank:

    def __init__(self, account_num, balance, bank_name):
        """
        :param account_num: account number
        :param balance: current balance
        :param bank_name: bank name
        """
        self._list_of_transaction = []
        self._account_num = account_num
        self._balance = balance
        self._bank_name = bank_name

    def get_account_num(self):
        return self._account_num

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        self._balance = new_balance

    def add_transaction(self, new_transaction):
        if self._balance < new_transaction.get_amount():
            print(f"Amount enter exceeds available balance ${self._balance}")
            return
        elif new_transaction.get_amount() <= 0:
            print("Amount can't be less or equal to 0")
            return
        self._list_of_transaction.append(new_transaction)
        self._balance -= new_transaction.new_transaction.get_amount()

    def show_transaction_by_budget(self, budget_type):
        for every_transaction in self._list_of_transaction:
            if every_transaction.get_budget_category() == budget_type:
                print(every_transaction)

    def show_transactions(self):
        print("List of transaction...")
        print("Date and time \t\t\t Amount \t Budget type \t Vendor")
        for every_transaction in self._list_of_transaction:
            print(every_transaction)

    def check_status(self, user_type, budget, budget_spent):
        # i = 0
        # for x in budget:
        #     if budget_spent[i] / x >= 0.9:
        #         print(user_type, "you've used over 90% of your budget on ", x)

        print()

    # balances = property(get_balance, set_balance())

    def get_bank_name(self):
        return self._bank_name

    def __str__(self):
        print(f"Account number: {self._account_num}")
        print(f"Balance       : ${self._balance}")
        print(f"Bank Name     : {self._bank_name}")
        self.show_transactions()
        return "--End--"

    def __repr__(self):
        return self._account_num, self._balance, self._bank_name
