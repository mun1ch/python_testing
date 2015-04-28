class BankAccount:
    def __init__(self,account_name):

        self.balance = 0
        self.name = account_name

    def showbalance(self):
        return print("Account name: %s with a balance of: %d" % (self.name,self.balance))

    def deposit(self,amount):
        self.balance += amount
        print('Deposit complete')
        self.showbalance()

    def withdraw(self,amount):
        if (self.balance - amount) >=0:
            self.balance -= amount
            print("Withdraw complete")
            self.showbalance()
        else:
            return print("Sorry, You can't withdraw more money than you have.")


class BallerAccount(BankAccount):
    def __init__(self,n):
        if type(n)==str:
            BankAccount.__init__(self,n)
            self.name = n + '_BallerAccount'
        else:
            self.balance = n.balance
            self.name = n.name + '_BallerAccount'

    def deposit(self,amount):
        if (self.balance + amount) >= 50000:
            BankAccount.deposit(self,amount)
        else:
            return print('Deposit error. You must have at least 50,000 in this account to use it.')

    def withdraw(self,amount):
        if (self.balance - amount) >= 50000:
            BankAccount.withdraw(self,amount)
        else:
            return print('Withdraw error. You must have at least 50,000 in this account to use it.')


a1 = BallerAccount("Alex")
a1.showbalance()
a1.deposit(500000)
a1.withdraw(699)
