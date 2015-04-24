class BankAccount:
    def __init__(self,account_name):

        self.balance = 0
        self.name = account_name

    def showbalance(self):
        return print("Account name: %s with a balance of: %d" % (self.name,self.balance))

    def deposit(self,amount):
        self.balance += amount
        return print("After deposit:, your balance is now: %d" % self.balance)

    def withdraw(self,amount):
        self.balance -= amount
        return print("After withdrawal:, you balance is now: %s" % self.balance)


a1 = BankAccount("Alex")
a1.showbalance()
a1.deposit(1000)
a1.withdraw(699)

