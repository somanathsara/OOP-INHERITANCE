# create a class person with attributes name and age and a method to display them.
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def display(self):
        print(f"Name of the person : {self.__name}")
        print(f"Age of the person : {self.__age}")
obj1 = Person("Amu", 20)
obj1.display()