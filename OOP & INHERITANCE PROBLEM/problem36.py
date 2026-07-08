"""Pay roll system class - manage employee salaryb with private data."""
class Payrollsystem:
    def __init__(self):
        self.__employee = ""
        self.__salary= 0 
    def set_data(self, name, salary):
        self.__employee = name
        self.__salary = salary
    def update_salary(self,salary):
        self.__salary = salary
    def display(self):
        print(f"Employee name : {self.__employee}")
        print(f"Salary : {self.__salary}")
p1 = Payrollsystem()
p1.set_data("Amu", 70000)
p1.display()
p1.update_salary(90000)
p1.display()