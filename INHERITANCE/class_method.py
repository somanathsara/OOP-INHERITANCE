class Person():
    def __init__(self,name):
        self.name = name
    @classmethod
    def from_birth_year(cls,name,birth_year):
        age = 2026 - birth_year
        cls.name = name
        print(f"The age of {cls.name} is {age}")
p = Person.from_birth_year("Ram", 2007)

    