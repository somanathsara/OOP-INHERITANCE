"""productInventory class - manage product name, quantity, and price using private attributes."""
class HotelMenu():
    def __init__(self):
        self.__name = ""
        self.__price = 0
        self.__quantity = 0
    def set_data(self,pname, quantity, price):
        self.__name =  pname
        self.__quantity  = quantity
        self.__price = price
    def displaydetails(self):
        print(f"Product name : {self.__name}")
        print(f"Quantity : {self.__quantity}")
        print(f"Product price : {self.__price}")
c1 = HotelMenu()
c1.set_data("Watch", 1, 678)
c1.displaydetails()        
        