"""TrainReservation Class - Design a class to store 
passenger & ticket details privately with methods to confirm or cancel tickets."""
class Train_reservation:
    def __init__(self):
        self.__name = ""
        self.__num = 0
        self.__status = ""
    def set_data(self,name, ticketnum):
        self.__name = name
        self.__num = ticketnum
        self.__status = "confirm"
    def show_data(self):
        print(f"Passenger name: {self.__name}")
        print(f"Ticket number: {self.__num}")
        print(f"Ticket status: {self.__status}")
p1 = Train_reservation()
p1.set_data("Mano ranajn sara", 347)
p1.show_data()