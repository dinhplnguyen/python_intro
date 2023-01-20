"""This module represents a transaction"""
from datetime import datetime


class Transaction:

    def __init__(self, amount, budget_category, vendor):
        """
        :param amount: int
        :param budget_category: type of budget
        :param vendor: name of store
        """
        self._date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self._amount = int(amount)
        self._budget_category = budget_category
        self._vendor = vendor

    def get_budget_category(self):
        """

        :return: type of budget
        """
        return self._budget_category

    def get_amount(self):
        """

        :return: amount
        """
        return self._amount

    def __str__(self):
        return "{0} \t {1} \t\t {2} \t\t\t {3}". \
            format(self._date, self._amount, self._budget_category, self._vendor)
