"""Electribill class - design a class that calculates bills based on units
consumed & rate per unit using private variables."""

class Electric_bill():
    def __init__(self):
        self.__rate = 0
        self.__unit = 0
        self.__bill = 0
    def set_data(self,unit, rate):
        self.__unit  = unit
        self.__rate = rate
    def calculate_bill(self):
        self.__bill = self.__unit * self.__rate
    def display_bill(self):
        print(f"Unit consumed: {self.__unit}")
        print(f"Rate per unit: {self.__rate}")
        print(f"Total bill:{self.__bill}")
eb1 = Electric_bill()
eb1.set_data(500, 7)
eb1.calculate_bill()
eb1.display_bill()
