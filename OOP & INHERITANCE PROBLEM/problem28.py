"""School class room - manage student details & subjects securely using encapsulation."""
class Schoolclass():
    def __init__(self):
        self.__name = ""
        self.__rollnum = 0
        self.__subject = ""
    def set_data(self, name, roll, subject):
        self.__name = name
        self.__rollnum = roll
        self.__subject = subject
    def displaydetails(self):
        print(f"Student name: {self.__name}")
        print(f"Student roll number: {self.__rollnum}")
        print(f"Subject: {self.__subject}")
s1 = Schoolclass()
s1.set_data("Amu", 19, "chemistry")
s1.displaydetails()