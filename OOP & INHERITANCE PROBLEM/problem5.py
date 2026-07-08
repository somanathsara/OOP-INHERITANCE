"""Car rental class - create a class to handle car information
, rental rates, and avalability, using encapsulation for secure data access"""
class Car_rental():
    def __init__(self, car_name,rent_per_day):
        self.__car_name = car_name
        self.__rent_per_day = rent_per_day
        self.__available = True
    def rent_car(self):
        if(self.__available):
            self.__available = False
            print(f"{self.__car_name} car has been rented.")
        else:
            print(f"{self.__car_name} is unavailable.!")
    def return_car(self):
        if(not self.__available):
            self.__available = True
            print(f"{self.__car_name} has been returned. ")
    def display_details(self):
        print(f"Car name: {self.__car_name}")
        print(f"Car rent per day: {self.__rent_per_day}")
cust1 = Car_rental("BMW", 50000)
cust1.display_details()
cust1.rent_car()
cust1.display_details()
cust1.return_car()
cust1.display_details()