class Employee():
    language = "Python"
    salary = "60000"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        print("I am creating an object.")
gudu = Employee("Gudu",70000, 2501297239)
prasenjit = Employee("Prasenjit",80000,2501297440)
print(gudu.name,gudu.salary,gudu.pin)
print(prasenjit.name,prasenjit.salary,prasenjit.pin)