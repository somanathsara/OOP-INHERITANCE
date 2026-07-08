"""WaterBill class - Develope a class that calculates water bills 
using private attributes for consumption & rates."""
class Water_class:
    def __init__(self):
        self.__consumption = 0
        self.__rate_per_consumption = 0
        self.__total = 0
    def set_data(self, consum, rate_per_consume):
        self.__consumption = consum
        self.__rate_per_consumption = rate_per_consume
    def calculate_total(self):
        self.__total = self.__consumption * self.__rate_per_consumption
    def show_details(self):
        print(f"Water consumption: {self.__consumption}")
        print(f"Rate per consumption: {self.__rate_per_consumption}")
        print(f"Total bill: {self.__total}")
c1 = Water_class()
c1.set_data(50, 5)
c1.calculate_total()
c1.show_details()