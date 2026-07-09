"""Demonstrate a bank Account with private data members for deposit withdraw & balance check."""
class Bankaccount:
    def __init__(self, name, amount):
        self.__name = name
        self.__amonut = amount
    def Deposit(self, amount):
        if(amount < 0):
            print("Deposit amonut must be positive")
        else:
            self.__amonut += amount
    def Withdraw(self, amount):
        if(amount > self.__amonut):
            print("Insufficient balance.")
        else:
            self.__amonut -= amount
    def displaydetails(self):
        print(f"Name of the person : {self.__name}")
        print(f"Amount : {self.__amonut}")
obj1 = Bankaccount("Somanath sara", 200000)
obj1.displaydetails()
obj1.Deposit(50000)
obj1.displaydetails()
obj1.Withdraw(40000)
obj1.displaydetails()