"""Flight ticket class - create a class to manage flight booking details 
like passenger name, flight number & price using private attributes."""
class FlightTicket():
    def __init__(self):
        self.__name = ""
        self.__fl_no = 0
        self.__price = 0
    def flight_booking(self, name, fl_no, price ):
        self.__name = name
        self.__fl_no = fl_no
        self.__price = price
    def display_details(self):
        print(f"Name of the passenger : {self.__name}")
        print(f"Flight number: {self.__fl_no}")
        print(f"Price : {self.__price}")
p1 = FlightTicket()
p1.flight_booking("Gudu", 529, 50000)
p1.display_details()