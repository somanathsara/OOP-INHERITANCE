#Add a static method is problem to greet the user Welcome to Calculator.
class Calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"The square of the number {self.n} is {self.n ** 2}")
    def cube(self):
        print(f"The cube of the number is {self.n} is {self.n ** 3}")
    def squareroot(self):
        print(f"The squareroot of the number {self.n} is {self.n ** (1/2)}")
    @staticmethod
    def hello():
        print("Welcome to calculator.")
a = Calculator(16)
a.hello()
a.square()
a.cube()
a.squareroot()
        
