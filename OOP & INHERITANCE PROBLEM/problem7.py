"""Shoping cart class- Develope a class to manage items in a 
shopping cart with encapsulated item details & total price."""
class Shopingcart():
    def __init__(self):
        self.__item = " "
        self.__price = 0
        self.__no_of_items = 0
        self.__total_price = 0
    def set_data(self, item, price, no_of_items):
        self.__item = item
        self.__no_of_items = no_of_items
        self.__price = price
    def total_price(self):
        self.__total_price = self.__no_of_items * self.__price
    def display_details(self):
        print(f"Name of the item: {self.__item}")
        print(f"No of items: {self.__no_of_items}")
        print(f"Total price: {self.__total_price}")
cust1 = Shopingcart()
cust1.set_data("ball", 70, 50)
cust1.total_price()
cust1.display_details()
        