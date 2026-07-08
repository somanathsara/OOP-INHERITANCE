"""Resturant order class - develope a class to simulate food order & billing using encapsulation."""
class ResturantOrder():
    def __init__(self):
        self.__name = ""
        self.__food_item = ""
        self.__quantity = ""
        self.__price = 0
        self.__bill = 0
    def set_data(self, custname, food, quantity, price):
        self.__food_item = food
        self.__name = custname
        self.__quantity = quantity
        self.__price = price
    def Billing(self):
        self.__bill = self.__price * self.__quantity
    def displaydetails(self):
        print(f"Customer name: {self.__name}")
        print(f"Food oredered: {self.__food_item}")
        print(f"Total price: {self.__bill}")
c1 = ResturantOrder()
c1.set_data("Gudu","panner roll", 5, 125)
c1.Billing()
c1.displaydetails()