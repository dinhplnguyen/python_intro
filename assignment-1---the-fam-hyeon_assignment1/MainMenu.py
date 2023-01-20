import fam
from Budget import Budget
from bank import Bank
from fam import FAM

class MainMenu:
    users = ["Jeff", "Lawrence", "Chrissy"]

    def menu(cls):
        menu_choice = int(input("1. View Budgets\n"
                                "2. Record a Transaction\n"
                                "3. View Transaction by Budget\n"
                                "4. View Bank Account Details\n"
                                "5. End the program\n"))
        return menu_choice

    def addUser(cls, dictionaries, budget):
        # budgets1 = Budget(1000, 100, "locked")
        dictionaries["Paul"] = budget

    def chooseUser(cls, users):
        i = 1
        print("Log in as: " , i)
        for x in users:
            print(f"{i}. ", x)
            i = i + 1
        userLen = len(users) + 1
        print(userLen, ". Add new User")
        inputs = int(input())
        print("user choose ", inputs)
        if inputs > userLen or inputs < 1:
            cls.chooseUser(users)
        return inputs


def main():
    mainmenu = MainMenu()
    FAM.view_users
    # user1 = "Jeff"
    # user2 = "Lawrence"
    # user3 = "Chrissy"
    # users = [user1, user2, user3]
    print(mainmenu.users[0])

    # print("Testing adding user")
    # user_input = FAM.create_users()
    # print(user_input)

    # print("Log in as: ")
    # i = 1
    # for x in users:
    #     print(f"{i}. ", x)
    #     i = i + 1
    # print(len(users), ". Add new User")
    inputs = 0
    # userName = int(input())

    # print("hello ", users[userName - 1])
    budgets1 = Budget(500, 100, "locked")
    budgets2 = Budget(600, 100, "locked")
    budgets3 = Budget(700, 100, "locked")
    user1Account = Bank(11111, 1000, "First Bank")
    user2Account = Bank(22222, 2000, "Second Bank")
    user3Account = Bank(33333, 3000, "Third Bank")

    userAccount = {mainmenu.users[0]: user1Account, mainmenu.users[1]: user2Account, mainmenu.users[2]: user3Account}
    userBudget = {mainmenu.users[0]: budgets1, mainmenu.users[1]: budgets2, mainmenu.users[2]: budgets3}

    user_log_in_choice = mainmenu.chooseUser(mainmenu.users)
    print("user chose", user_log_in_choice)

    print(mainmenu.addUser.length)
    if user_log_in_choice == 4:
        budgets4 = Budget(1000, 100, "locked")
        mainmenu.addUser(userBudget, budgets4)
        mainmenu.users.append("Paul")
        print(mainmenu.addUser.length)
        user_log_in_choice = mainmenu.chooseUser(mainmenu.users)


    mainUser = mainmenu.users[user_log_in_choice - 1]



    print("the current user is ", mainUser)

    # this will append new user
    # budgets4 = Budget(1000, 100, "locked")
    # addUser(userBudget, budgets4)
    # print(userBudget)
    # print(userBudget["paul"].get_budget())
    # choice1 = 1

    choice1 = 0
    while choice1 != 5:
        choice1 = mainmenu.menu()
        if choice1 == 5:
            break
        if choice1 == 1:
            print("you've chosen 1")
            # print(userBudget[mainUser].get_budget())
            print(userBudget[mainUser])
        elif choice1 == 2:
            print("you've chosen 2")
        elif choice1 == 3:
            print("you've chosen 3")
        elif choice1 == 4:
            print("you've chosen 4")
            print(userAccount[mainUser].__repr__())
        else:
            print("you've wrong choice")


if __name__ == '__main__':
    main()
