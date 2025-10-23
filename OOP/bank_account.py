class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited {amount}.New balance:{self.balance}")
    def withdraw(self,amount):
        if self.balance>1000:
            self.balance-=amount
            print(f"Withdresw {amount}.New balance:{self.balance}")
        else:
            print("insufficient balance")
    def check_balance(self):
        print(f"Account number:{self.account_number}\n Balance:{self.balance}")
account1=BankAccount(1234567895,3000)
account2=BankAccount(458599849389,100)
account1.deposit(3000)
account2.withdraw(1000)
account1.check_balance()
account2.check_balance()
