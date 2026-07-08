"""Course Enrollmet class - Create a class with private data for 
course name, duration, and enrolled students."""
class Course_Enrollment():
    def __init__(self):
        self.__c_name = ""
        self.__duration = ""
        self.__enrolled_student = 0
    def set_data(self, name, duration, enrolled_student):
        self.__c_name = name
        self.__duration = duration
        self.__enrolled_student = enrolled_student
    def display_details(self):
        print(f"Course name : {self.__c_name}")
        print(f"Duraton : {self.__duration}")
        print(f"Enrolled students : {self.__enrolled_student}")
s1 = Course_Enrollment()
s1.set_data("B.tech","30hr56min", 167 )
s1.display_details()