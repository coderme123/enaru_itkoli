class BankAccount:
    def _init_(self, account_number, account_name, initial_balance):
        self.__account_number = account_number
        self.__account_name = account_name
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit Successful. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal Successful. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_account_details(self):
        return f"Account Number: {self._account_number}, Account Name: {self.account_name}, Balance: {self._balance}"

    def get_balance(self):
        return self.__balance


account = BankAccount("1234567890", "John Doe", 1000)
print(account.get_account_details())

account.deposit(500)
account.withdraw(200)

print(account.get_balance())
try:
    print(account.__balance)
except AttributeError:
    print("Cannot access private attribute directly.")
