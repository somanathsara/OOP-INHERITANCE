"""write a class complex to represent complex number along with overloaded operator '+'
'*' whch adds and multiplies them."""
class Complex():
    def __init__(self,r,i):
        self.i = i
        self.r = r
    def __add__(self,c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    def __mul__(self,c2):
        real_part = self.r*c2.r - self.i*c2.i
        imag_part = self.r*c2.i + self.i*c2.r 
        return Complex(real_part,imag_part)
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
c1 = Complex(5,3)
c2 = Complex(2,3)
print(c1+c2)
        
        