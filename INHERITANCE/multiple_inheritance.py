class Employee():
    company = "SpaceX"
    name = "Default name"
    def show(self):
        print(f"The name of the employee is {self.name} & the name of the company is {self.company}")
class coder():
    language = "Pyhton"
    def print_language(self):
        print(f"Out of all language here is your language: {self.language}")
class programmer(Employee, coder):
    company = "Infotech"
    def show(self):
        print(f"The name is {self.company} and it is good with {self.language}")
a = Employee()
b = programmer()
a.company
a.show()
b.company
b.show()
b.print_language()