# Name: Dinh & Hyeon
# Student number:

"""This module represents a user menu"""
import user
import fam
import Budget
import bank


class UserMenu:

    current_user = None
    list_of_all_user = []

    def __init__(self):
        self._fam_account = fam.FAM()
        UserMenu.load_sample_users()

    def display_user_menu(self):
        user_input = None

        while user_input != 3:
            if UserMenu.current_user is None:
                print("\nWelcome to Family Appointed Moderator")
                print("-----------------------")
                print("1. Login to sample accounts")
                print("2. Create new account")
                print("3. Exit")
                string_input = input("Please enter your choice (1-3) ")

                if string_input == '':
                    continue
                user_input = int(string_input)

                if user_input == 1:
                    print("ID  Username")
                    self._fam_account.view_users(UserMenu.list_of_all_user)
                    UserMenu.current_user = UserMenu.get_user_by_id(int(input("Enter user id to login: ")))

                elif user_input == 2:
                    UserMenu.add_user(self._fam_account.create_users())

                elif user_input == 3:
                    print("Thanks for choosing us, see you later.")

                else:
                    print("Not a valid option, please try again.")

            else:
                print("\nWelcome back to your account,", UserMenu.current_user.get_user_name())
                print("-----------------------")
                print("1. View your budget")
                print("2. View your transactions by budget")
                print("3. View your bank account details")
                print("4. Record a transaction")
                print("5. Logout")
                string_input = input("Please enter your choice (1-5) ")
                current_user_input = int(string_input)
                if current_user_input == 1:
                    print("Viewing your budgets:")
                    print(UserMenu.current_user.get_budget())

                elif current_user_input == 2:
                    print("Type in the transaction of the budget you want to see")

                    UserMenu.current_user.get_bank().\
                        show_transaction_by_budget(self._fam_account.set_budget_transaction())

                elif current_user_input == 3:
                    print("Viewing your bank account")
                    print(UserMenu.current_user.get_bank())

                elif current_user_input == 4:
                    if UserMenu.current_user.get_budget().get_locked() == "locked":
                        print("You've been locked out due to exceeding your budget")
                        return
                    UserMenu.current_user.get_bank().check_status(UserMenu.current_user.get_user_type(),
                                                                  UserMenu.current_user.get_budget(),
                                                                  UserMenu.current_user.get_budget().get_budget_spent())

                    UserMenu.current_user.get_bank().add_transaction(self._fam_account.set_transaction())
                    # UserMenu.current_user.get_budget().update_spent() need to get the budget_category and amount

                elif current_user_input == 5:
                    print("Successfully logout, you are at main menu.")
                    UserMenu.current_user = None

    @staticmethod
    def add_user(new_user):
        UserMenu.list_of_all_user.append(new_user)

    @staticmethod
    def load_sample_users():
        user_1 = user.User("Dinh", 19, "Angel", bank.Bank(123, 123, 123), Budget.Budget(123, 123, 12, 456))
        user_2 = user.User("Harry", 25, "Rebel", None, None)
        user_3 = user.User("Dany", 33, "Troublemaker", None, None)
        UserMenu.add_user(user_1)
        UserMenu.add_user(user_2)
        UserMenu.add_user(user_3)

    @staticmethod
    def get_user_by_id(user_id):
        found_user = None
        for find_user in UserMenu.list_of_all_user:
            if find_user.get_user_id() == user_id:
                found_user = find_user
                break
        return found_user


def main():
    menu = UserMenu()
    menu.display_user_menu()


if __name__ == '__main__':
    main()