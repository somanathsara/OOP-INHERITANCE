"""Employee attendace class - Design a class to mark attendace & calculate working days"""
class EmployeeAttendace():
    def __init__(self,name, attendance):
        self.__attendace = attendance 
        self.__working_days = 0
        self.__name = name
    def total_working(self):
        if(self.__attendace == "present"):
            self.__working_days += 1
    def displaydetails(self):
        print(f"Employee name : {self.__name}")
        print(f"Total working days : {self.__working_days}")
e1 = EmployeeAttendace("Rohan", "present")
e1.total_working()
e1.displaydetails()
