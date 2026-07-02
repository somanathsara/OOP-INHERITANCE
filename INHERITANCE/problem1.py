"""Create a class 2D-vector &use it to craete another  class represnting a vector 3-D"""
class TwoDvector():
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def Show(self):
        print(f"The 2Dvector is {self.i}i + {self.j}j")
class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def Show(self):
        print(f"The 3D vector is {self.i}i + {self.j}j + {self.k}k")
        
            
v1 = TwoDvector(2,4)
v1.Show()
v2 = ThreeDvector(2,4,7)
v2.Show()
    