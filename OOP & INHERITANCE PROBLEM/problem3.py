"""Employ salary class - Develop a private class 
attribute to store employ details & manage salary detaild securely"""

class Employee():
    def __init__(self):
        self.__name = ""
        self.__emp_id = ""
        self.__salary = 0
    def set_details(self, name, empid, salary):
        self.__name = name
        self.__salary = salary
        self.__empid = empid
    def update_salary(self, newsalary):
        if(newsalary > 0):
            self.__salary = newsalary
            print(f"Salary updated succesfully")
        else:
            print("Invalid salary")
    def display_details(self):
        print(f"Employee name: {self.__name}")
        print(f"Employee id: {self.__empid}")
        print(f"Salary:{self.__salary}")
    
e1 = Employee()
e1.set_details("ram", 239, 60000)
e1.update_salary(90000)
e1.display_details()
e2 = Employee()
e2.set_details("shyam", 240, 70000)
e2.display_details()