#Demonstrate multiple inheritance with class inherited from from 2 parent class.
class father():
    def skills(self):
        print("Gardening, Driving")
class Mother():
    def skills(self):
        print("Cooking, Painting")
class Child(father, Mother):
    def skills(self):
        father.skills(self)
        Mother.skills(self)
        print("coding")
obj = Child()
obj.skills()