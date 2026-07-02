#Write a class calculator capable of finding square, cube & squareroot of a number.
class Calculator():
    def __init__(self,n):
       self.n = n
    def square(self):
        print(f"The square of the number {self.n} is {self.n ** 2}")
    def cube(self):
        print(f"The cube of the number {self.n} is {self.n**3}")
    def squareroot(self):
        print(f"The squareroot of the number {self.n} is {self.n **(1/2)}")
a = Calculator(4)
a.square()
a.cube()
a.squareroot()
    
    