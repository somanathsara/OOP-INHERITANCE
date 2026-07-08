"""Elctric vehicle class - Manage battery status & range details"""
class Electricvechile():
    def __init__(self):
        self.__vehicle = ""
        self.__battery = 0
        self.__range = 0       
    def set_data(self, name,battery,distance):
        self.__battery = battery
        self.__range = distance
        self.__vehicle = name
    def charge(self):
        self.__battery = 100
        print("Battery fully charged.")
    def display(self):
        print(f"Vehicle  : {self.__vehicle}")
        print(f"Battery : {self.__battery}")
        print(f"Range : {self.__range}")
p1 = Electricvechile()
p1.set_data("BMW", 78, 100)
p1.charge()
p1.display()
        