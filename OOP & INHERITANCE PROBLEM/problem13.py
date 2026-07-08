"""PatientRecordClass - Design a class with private attributes 
for patient name, age, and diagnosis."""
class Patient_record():
    def __init__(self):
        self.__name = ""
        self.__age = 0
        self.__diagnosis = ""
    def details(self, name, age, dignosis):
        self.__name = name
        self.__age = age
        self.__diagnosis =dignosis
    def show_details(self):
        print(f"Patient Name: {self.__name}\nPatient age: {self.__age}\nPatient dignosis: {self.__diagnosis}")
p1 = Patient_record()
p1.details("madhupuspa", 50,"Diabetis")
p1.show_details()
        