"""Demonstrate polymerphism using a shape base
class with circle & square subclasses that each impliment area()"""
class Shape():
    def __init__(self):
        raise NotImplementedError("Subclass must impliment area()")
class circle(Shape):
        def __init__(self,radius):
            self.radius = radius
        def area(self):
            return 3.14 * self.radius**2
class square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    
shapes = [circle(5), square(4)]
for s in shapes:
    print(f"{type(s).__name__} area : {s.area()}")
            