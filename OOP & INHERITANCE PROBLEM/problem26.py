"""Cinema hall class - create a class to handle seat booking and avalabilty details."""
class Cinemahall():
    def __init__(self):
        self.__name = ""
        self.__seat_num = 0
        self.__avalability = "pending"
    def set_data(self,name, seatnum):
        self.__name = name
        self.__seat_num = seatnum
    def Seatbooking(self):
        if(self.__avalability):
            self.__avalability = "Booked"
            print("Seat booking succesful")
    def displaydetails(self):
        print(f"Customer name : {self.__name}")
        print(f"Seat number : {self.__seat_num}")
        
c1 = Cinemahall()
c1.set_data("Amu", 467)
c1.Seatbooking()
c1.displaydetails()        