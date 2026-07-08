"""Student record class - create a class  with private attributes to store student names, 
rollno., and marks. Include methods to set and display student details."""
class Student():
    def __init__(self):
        self.__mark = 0
        self.__roll = 0
        self.__name = "AVSDBHKERF"
    def set(self,name,roll,mark):
        self.__name = name
        self.__mark = mark
        self.__roll = roll
    def display_details(self):
        print(f"Student name: {self.__name}")
        print(f"Student mark: {self.__mark}")
        print(f"Student Roll: {self.__roll}")
s1 = Student()
s1.set("Ram", 239, 9.27)
s1.display_details()