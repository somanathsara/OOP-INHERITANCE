"""Build a class Secure Note with private messages and methods 
to reveal it only with the correct password."""
import getpass
class SecureNote():
    def __init__(self, note, password):
         self.__note = note
         self.__password = password
    def reveal(self, password):
        if(password == self.__password):
            return self.__note
        else:
            print("Access Denied! Wrong password")
note1 = SecureNote("Meeting at newdelhi", "sEcReAt@1235")
# print(note1.reveal("sEcReAT@1235"))
note1.reveal(input("Enter password: "))

