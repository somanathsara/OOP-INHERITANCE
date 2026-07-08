"""Insurance policy class  - Design a class with private attributes for policy number, holdername & insurance"""
class Insurancepolicy():
    def __init__(self):
        self.__policy_num = 0
        self.__name = ""
        self.__insurance = 0
    def set_data(self, name, number, insurance):
        self.__name = name
        self.__policy_num = number
        self.__insurance = insurance
    def displaydetails(self):
        print(f"Customer name: {self.__name}")
        print(f"Policu number: {self.__policy_num}")
        print(f"Insurance  :{self.__insurance}")
c1 =Insurancepolicy()
c1.set_data("Amu", 345234, 60000)
c1.displaydetails()