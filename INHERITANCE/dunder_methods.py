"""p1 + p2 = p1.__add__(p2)
p1 - p2 = p1.__sub__(p2)
p1 * p2 = p1.__mul__(p2)
p1 / p2 = p1.__truediv__(p2)
p1 // p2 = p1.__floordiv__(p2)
__str__() It is used to set what gets displayed upon calling str(obj).
__len__() It is usee to set  what get displayed upon calling len(obj).
"""
class Number():
    def __init__(self,n):
        self.n = n
    def __add__(self,num):
        return self.n + num.n 
    
n = Number(4)
m = Number(5)
print(n + m)
