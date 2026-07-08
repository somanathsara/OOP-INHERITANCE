"""GymMembership class - create a class with private data for 
member name , membership type, & duration. """
class Gym_membership:
    def __init__(self):
        self.__name = ""
        self.__member_type = ""
        self.__duration = ""
    def set_data(self, name, type, duration):
        self.__name = name
        self.__member_type = type
        self.__duration = duration
    def display_details(self):
        print(f"Member name: {self.__name}")
        print(f"Membership Type: {self.__member_type}")
        print(f"Duration : {self.__duration}")
m1 = Gym_membership()
m1.set_data("Balaram", "Head", "1 year")
m1.display_details()