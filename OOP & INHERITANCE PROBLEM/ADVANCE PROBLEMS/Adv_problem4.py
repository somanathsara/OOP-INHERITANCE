"""Implimate a class Employee with private salary attribute.
Add methods to set & get salary with validation."""
class Employee:
    def __init__(self, name , balance):
        self.__salary = 0
        self.__name = name
        self.set_salary(balance)
    def set_salary(self, salary):
        if(salary < 0):
            print("Salary can not be negeative.")
        else:
            self.__salary = salary    
    def get_salary(self):
        return self.__salary
obj = Employee("Ram", 20000)
print(obj.get_salary())
obj.set_salary(50000)
print(obj.get_salary())
     
    
        