"""
Create a bank account class that has attributes owner, balance and two methods deposit and withdraw.
Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, 
and test to make sure the account can't be overdrawn.

class Account:
    pass
"""

class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"Your deposit:({amount}), New balance:({self.balance})")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print(f"Your withdramal amount:({amount}), New balance:({self.balance})")
    def __str__(self):
         return f"Owner name ({self.owner}),Balance ({self.balance})"


owner_name = input("Enter owner name: ")
balance = float(input("Enter balance: "))
 
acc = Account(owner_name,balance)
print (acc)

d_amount=float(input("Enter a deposit:"))
acc.deposit(d_amount)

w_amount=float(input("Enter a withramal:"))
acc.withdraw(w_amount)

print(acc)
