"""Loan account class - Design a class with private attributes to store borrower & loan details"""
class LoanAccount:
    def __init__(slf):
        slf.__borrower = ""
        slf.__loan_amount = 0
        slf.__int_rate = 0
    def set_data(self, borrower, loan, interest):
        self.__borrower = borrower
        self.__loan_amount = loan
        self.__int_rate = interest
    def displaydetails(slf):
        print(f"Name of Borrower : {slf.__borrower}")
        print(f"Amount : {slf.__loan_amount}")
        print(f"Rate of interest : {slf.__int_rate}")
c1 = LoanAccount()
c1.set_data("ram", 20000, 8.5)
c1.displaydetails()