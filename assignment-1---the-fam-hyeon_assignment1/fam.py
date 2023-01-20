"""This module represents a helper class"""
import user
import bank
import Budget
import transaction


class FAM:

    @staticmethod
    def view_users(list_of_user):
        """
        display list of user
        :param list_of_user
        """
        for every_user in list_of_user:
            print(every_user)

    @staticmethod
    def create_users():
        """
        create user
        """
        user_name = input("Enter your name: ")
        user_age = input("Enter your age: ")
        user_type = FAM.set_user_type()
        new_bank = FAM.set_bank()
        budget = FAM.set_budget_info()
        new_user = user.User(user_name, user_age, user_type, new_bank, budget)
        return new_user

    @staticmethod
    def set_user_type():
        """
        set user type
        """
        angel_user = "Angel"
        troublemaker_user = "Troublemaker"
        rebel_user = "Rebel"
        user_input = False
        user_type = None
        while not user_input:
            user_type_input = int(input("Please select one of the following options:\n"
                                        "1. The Angel\n"
                                        "2. The Troublemaker\n"
                                        "3. The Rebel\n"))
            if user_type_input == 1:
                user_input = True
                user_type = angel_user
            elif user_type_input == 2:
                user_input = True
                user_type = troublemaker_user
            elif user_type_input == 3:
                user_input = True
                user_type = rebel_user
            else:
                print("Not a valid option, please try again!")
                pass
        return user_type

    @staticmethod
    def set_bank():
        """
        :return: new bank item
        """
        print("Enter your bank info...")
        account_num = input("Account number: ")
        balance = input("Current balance: ")
        bank_name = input("Bank name: ")
        new_bank = bank.Bank(account_num, balance, bank_name)
        return new_bank

    @staticmethod
    def set_budget_info():
        """
        :return: new budget
        """
        print("Enter your budget for...")
        game = int(input("Games and Entertainment:  "))
        clothing = int(input("Clothing and Accessories: "))
        eating_out = int(input("Eating out: "))
        misc = int(input("Miscellaneous: "))
        new_budget = Budget.Budget(game, clothing, eating_out, misc)
        return new_budget

    @staticmethod
    def set_transaction():
        """

        :return:  new transaction
        """
        print("Enter your transaction info...")
        amount = input("Amount: ")
        budget_category = FAM.set_budget_transaction()
        vendor = input("Vendor name: ")
        new_transaction = transaction.Transaction(amount, budget_category, vendor)
        return new_transaction

    @staticmethod
    def set_budget_transaction():
        """

        :return: return budget type
        """
        budget_category = None

        while budget_category is None:

            print("Choose your budget type...")
            print("1. Games and Entertainment\n"
                  "2. Clothing and Accessories\n"
                  "3. Eating out\n"
                  "4. Miscellaneous")

            budget_choice = int(input())
            if budget_choice == 1:
                budget_category = "game"
            elif budget_choice == 2:
                budget_category = "clothing"
            elif budget_choice == 3:
                budget_category = "eating_out"
            elif budget_choice == 4:
                budget_category = "misc"
            else:
                print("Not a valid budget type, please try again")
                pass

        return budget_category

