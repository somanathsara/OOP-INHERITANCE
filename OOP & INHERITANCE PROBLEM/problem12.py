"""MovieTicketclass - Create a class to handle movie 
ticket booking details like seat number & movie name."""
class Movie_ticket():
    def __init__(self):
        self.__name = ""
        self.__seatnum = 0
    def seat_book(self, name, num):
        self.__name = name
        self.__seatnum = num
    def show_details(self):
        print(f"Movie name : {self.__name}\nSeat number : {self.__seatnum}")
p1 = Movie_ticket()
p1.seat_book("Interstellar", 345)
p1.show_details()