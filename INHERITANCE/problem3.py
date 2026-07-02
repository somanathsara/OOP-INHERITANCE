"""Create a class Employyee & add salary & increment property to it.
Write a method 'salaryAfterincrement' method with a @property decorator 
with a setter which changes the value of the increment based on the salary"""
class Employee():
    def __init__(self):
        self.salary = 2000
        self.increment = 20
    @property
    def salaryAfterincrement(self):
        return (self.salary +(self.salary)*(self.increment/100))
    @salaryAfterincrement.setter
    def salaryAfterincrement(self, salary):
        self.increment = ((salary/self.salary) - 1)*100
emp1 = Employee()
emp1.salaryAfterincrement = 50000 
emp1.increment = 20           
print(emp1.salaryAfterincrement)