"""Create a class Account with a private attribute
__balance & provide a getter & setter method. """
class Account:
    def __init__(self, balance):
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, value):
        if(value < 0):
            raise ValueError("Balance cannot be negeative.")
        self.__balance = value
obj  = Account(20000)
print(obj.balance)
obj.balance = 50000000
print(obj.balance)
obj.balance = -5000
print(obj.balance)