"""The method name property  decoratr is called getter method.
We can define a function + @name.setter decorator below."""
class Employee():
    a = 1
    @classmethod
    def show_class(self):
        print(f"The class attribute of a is {self.a} ")
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self, value):
        self.fname = value.split()[0]
        self.lname = value.split()[1]
emp = Employee()
emp.a= 18
emp.name = "Somanath sara"
print(emp.fname, emp.lname)
emp.show_class()

#We have to check why error occur.
        

        