"""HotelRoomClass - Develope a class to manage 
room details & booking status using encapsulation."""
class Hotel_room():
    def __init__(self,roomnum):
        self.__num = roomnum
        self.__status = "Available"
    def booking(self):
        if(self.__status == "Available"):
            self.__status = "Booked"
            print(f"{self.__num} number room is booked.")
        else:
            print(f"{self.__num} number room is already fillup.")
    def show_data(self):
        print(f"Room no. = {self.__num}")
        print(f"Room avaliablity : {self.__status}")
p1 = Hotel_room(567)
p1.booking()
p1.show_data()

