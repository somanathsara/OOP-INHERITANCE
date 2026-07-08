"""Online order class  - Design a class to store order details and 
manage order status securely"""
class OnlineOrder():
    def __init__(self):
        self.__name = ""
        self.__price = 0
        self.__status = "pending"
    def Order(self, name, price):
        self.__name = name
        self.__price = price
        self.__status = "confirmed"    
    def display_details(self):
        print(f"Your order is :{self.__name}")
        print(f"Price : {self.__price}")
        print(f"Status: {self.__status}")
cust1 = OnlineOrder()
cust1.Order("Stand", 469)
cust1.display_details()