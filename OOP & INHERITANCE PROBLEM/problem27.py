"""Train schedule class - Design a class with private data for train timing, routes, capacity."""
class Trainschedule():
    def __init__(self):
        self.__rout = ""
        self.__timing = ""
        self.__capacity = 0
        self.__number = 0
    def set_data(self, number, capacity, rout, timing):
        self.__rout = rout
        self.__number = number
        self.__capacity = capacity
        self.__timing = timing
    def displaydetails(self):
        print(f"Train number : {self.__number}")
        print(f"Root number : {self.__rout}")
        print(f"Time line : {self.__timing}")
        print(f"Maximum passenger: {self.__capacity}") 
p1 = Trainschedule()
p1.set_data(5678, 50,"hyderabad","2hr 30min")
p1.displaydetails()