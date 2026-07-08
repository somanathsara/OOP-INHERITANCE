"""Vehicle Fuel class - Demonstrate a class that maintains fuel 
type and level securely, with methods to refil & check fuel"""

class Vehicle_fuel():
    def __init__(self,type):
        self.__level = 0
        self.__type = type
    def Fuel_refil(self,level):
        self.__level += level
    def Check_fuel(self):
        print(f"Fuel Type: {self.__type}")
        print(f"Fuel level = {self.__level}")
v1 = Vehicle_fuel("Petrol")
v1.Fuel_refil(10)
v1.Check_fuel()