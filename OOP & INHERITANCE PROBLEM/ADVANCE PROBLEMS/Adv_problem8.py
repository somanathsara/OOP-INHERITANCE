#Show how the super() function is used to call a parent class constructor.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        
class car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def display(self):
        print(f"{self.brand} : {self.model}")
c1 = car("BMW","M4")
c1.display()

            