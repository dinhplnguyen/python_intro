"""This module represents a user"""
class User:
    user_id = 0

    def __init__(self, user_name, user_age, user_type,
                 bank, budget):
        """
        :param user_name: name of user
        :param user_age: age of user
        :param user_type: type of user
        :param bank: bank class
        :param budget: budget class
        """
        self._user_name = user_name
        self._user_age = user_age
        self._user_type = user_type
        self._bank = bank

        self._user_id = User.generate_id()
        self._budget = budget

    def get_user_id(self):
        """
        :return: user if
        """
        return self._user_id

    def get_user_name(self):
        """

        :return: username
        """
        return self._user_name

    def get_user_age(self):
        """

        :return: user's age
        """
        return self._user_age

    def get_user_type(self):
        """

        :return: user type
        """
        return self._user_type

    def get_bank(self):
        """

        :return: bank
        """
        return self._bank

    def get_budget(self):
        """

        :return: budget
        """
        return self._budget

    def __str__(self):
        return " {0}  {1}" \
            .format(self._user_id, self._user_name)

    @staticmethod
    def generate_id():
        User.user_id += 1
        return User.user_id
