"""Bank account class- Demonstrate a class to simulate basic banking operation 
such as deposit, withdraw, and balance check using private data member. """
class Bank_account():
    def __init__(self,acc_holder, balance):
        self.__acc_holder = acc_holder
        self.__balance = balance
    def deposit(self,deposit_amount):
        if(deposit_amount > 0):
            self.__balance = self.__balance + deposit_amount
            print(f"Deposited : {deposit_amount}")
        else:
            print("Invalid deposit amonut.")
    def withdraw(self,withdraw_amount):
        if(withdraw_amount < self.__balance):
            self.__balance = self.__balance - withdraw_amount
            print(f"Withdraw: {withdraw_amount}")
        else:
            print("Insufficient balance!")
    def balance_check(self):
        print(f"Account Holder: {self.__acc_holder}")
        print(f"Balance: {self.__balance}")
acc1 = Bank_account("ram", 40000)
acc1.balance_check()
acc1.deposit(5000)
acc1.balance_check()
acc1.withdraw(30000)
acc1.balance_check()
        