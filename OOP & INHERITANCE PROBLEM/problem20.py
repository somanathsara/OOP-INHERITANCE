"""HotelMenu class  - Design a class with private attributes for dishes, prices & availability."""
class Hotel_menu:
    def __init__(self):
        self.__dish = ""
        self.__price = 0
        self.__availability = True
    def set_data(self, dish, price):
        self.__dish = dish
        self.__price = price
    def show_details(self):
        print(f"Dish name:{self.__dish}")
        print(f"Price of the dish:{self.__price}")
        print(f"Avaliability:{self.__availability}")
c1 = Hotel_menu()
c1.set_data("fish", 60)
c1.show_details()