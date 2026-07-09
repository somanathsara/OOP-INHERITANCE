"""Demonstarte Single inhertance : A dog class inhertited from Animal class
"""
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")
class Dog(Animal):
    def speak(self):                     #Method overriding
        print(f"{self.name} barks")
obj = Animal("Generic Animal")
obj.speak()
obj2 = Dog("Blacky")
obj2.speak()
        