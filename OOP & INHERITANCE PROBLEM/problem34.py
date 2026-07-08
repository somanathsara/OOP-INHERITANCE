"""Food delivery class - Manage order detais and delivary details using encapsulation."""
class FoodDelivery():
    def __init__(self):
        self.__order_id = 0
        self.__customer = ""
        self.__status= "pending"
    def placeorder(self,name, id):
        self.__order_id = id
        self.__customer= name
    def updatestatus(self,status):
        self.__status = status
    def diplaydetails(self):
        print(f"Customer name: {self.__customer}")
        print(f"Order number: {self.__order_id}")
        print(f"Status: {self.__status}")
c1 = FoodDelivery()
c1.placeorder("Amu", 456)
c1.updatestatus("Delivered")
c1.diplaydetails()
print(c1.__status)
    