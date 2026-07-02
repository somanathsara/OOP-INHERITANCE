#create a class programmer for storing information of few programmer working at microsoft.
class Programmer():
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        print(f"Programmer at {self.company}: ")
p1 = Programmer("Nirmala",70000,139)
print(p1.name,p1.salary,p1.pin)
p2 = Programmer("Prasenjit", 70000, 246)
print(p2.name,p2.salary,p2.pin)
p3 = Programmer("Partha",70000,392)
print(p3.name,p3.salary,p3.pin)
