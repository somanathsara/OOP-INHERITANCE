"""Write a class train which has methods to book a ticket, get status(no. of sits) 7 get fare information 
of train running under Indian railways."""
import random
class Train():
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self, fro, to):# fro is from
        print(f"Ticket is booked in TrainNo: {self.trainNo} from {fro} to {to}")
    def get_status(self):
        print(f"train no: {self.trainNo} is running on time.")
    def getfare(self, fro,to):
        print(f"Ticket fare in trainno: {self.trainNo} from {fro} to {to} is {random.randint(256,7888)}")
t = Train(12399)
t.book("Rampur","delhi")
# t.get_status()
t.getfare("Rampur", "delhi")