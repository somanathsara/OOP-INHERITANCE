#syntax : super().__init__()
class Employee():
    def __init__(self):
        print("Constructor is employee")
    a = 1
class Programmer(Employee):
    def __init__(self):
        print("Constructor is a programmer.")
    b = 2
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor is manager.")
    c = 3
obj = Manager()
print(obj.a, obj.b, obj.c)
        
        