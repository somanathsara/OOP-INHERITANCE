"""Book store class - Create a class with private attributes to manage book stocks & sales"""
class BookStore():
    def __init__(self):
        self.__book = ""
        self.__stock = 0
        self.__sales = 0
    def set_data(self, book,stock):
        self.__book = book
        self.__stock = stock
    def saleBook(self, quantity):
        if(quantity < self.__stock):
            self.__stock -= quantity
            self.__sales += quantity
            print("Book sold succesfully")
        else:
            print("Not Enough books.!")
    def displaydetails(self):
        print(f"Book name: {self.__book}")
        print(f"stock : {self.__stock}")
        print(f"Sales : {self.__sales}")
c1 = BookStore()
c1.set_data("Pracical Binary Analysis", 274)
c1.saleBook(57)
c1.displaydetails()