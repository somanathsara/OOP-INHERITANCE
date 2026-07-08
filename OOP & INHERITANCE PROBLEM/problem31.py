"""Online payment class - Securely handle transaction details by using private data members."""
class OnlinePayment():
    def __init__(self):
        self.__transaction_id = 0
        self.__payer_name = ""
        self.__amount = 0
        self.__payment_status = "Pending"
    def make_payment(self, id, name, amount):
        self.__payer_name = name
        self.__amount = amount
        self.__transaction_id = id
        if(self.__payment_status == "Pending"):
            self.__payment_status = "Payment succesful"
        else:
            self.__payment_status = "payment failed"
    def displaydetails(self):
        print(f"Payer name = {self.__payer_name}")
        print(f"Tramsaction id = {self.__transaction_id}")
        print(f"Amount : {self.__amount}")
        print(f"Payment status  :{self.__payment_status}")
c1 = OnlinePayment()
c1.make_payment(346833757487, "Amu", 400000)
c1.displaydetails()