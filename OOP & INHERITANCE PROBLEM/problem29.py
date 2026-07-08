"""Laptop store class - create aclass with private data and for brand, price and stock"""
class Laptopstore():
    def __init__(self):
        self.__brand = ""
        self.__price = 0 
        self.__stock =0
    def set_data(self, brand, price, stock):
        self.__brand = brand
        self.__price =price
        self.__stock =stock
    def displaydetils(self):
        print(f"Laptop brand: {self.__brand}")
        print(f"Laptop price : {self.__price}")
        print(f"Total number of laptop's : {self.__stock}")
c1 = Laptopstore()
c1.set_data("Asus ROG", 150000, 30)
c1.displaydetils()