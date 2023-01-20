import abc
class BankAccount (abc.ABC):
init_lself, account_number, account_holder,
def
selt. account account number
self. account_holder account_holder
self. balance = ø
sel f. deposit ( initiat_deposit
@abc.abstractmethod
def deposit (self, amount):
pass
@abc.abstractmethod
def withdraw(self, amount):
pass
class SavingsAccount(BankAccount) :
def deposit(self, amount):
if amount
self. balance +2 amount
def withdraw(self, amount):
deduction amount
self. balance
(amount deduction)
nane
my_account —
main
' ' , "John Smith",
5øøø
my_account. withdraw( 5001
pr int (my_account.balance)