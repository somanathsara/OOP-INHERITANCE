"""Write a __str__() method to print the vector as follow.
7i + 8j + 10k
assume vector of dimension 3 for this problem.
"""
class Vector():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other):
        result = Vector(self.x+other.x, self.y+other.y, self.z+other.z)
        return result
    def __str__(self):
        return f"{self.x}i  + {self.y}j + {self.z}k"
v1 = Vector(7,8,10)
print(v1) 
        
    