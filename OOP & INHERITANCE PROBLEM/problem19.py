"""CreditCardAccount class - create a class to manage card number , holdername, & balance securely"""
class Credit_card_Account:
    def __init__(self):
        self.__card_number = 0
        self.__holder_name = ""
        self.__balance = 0
    def set_data(self, name, number, balance):
        self.__holder_name = name
        self.__card_number = number
        self.__balance = balance
    def show_details(self):
        print(f"Name : {self.__holder_name}")
        print(f"Card number : {self.__card_number}")
        print(f"Balance Enquiry : {self.__balance}")
p1 = Credit_card_Account()
p1.set_data("Gudu", 250976876, 700000)
p1.show_details()