"""Library book class - Design a class with private attributes for book title, author, 
and availability.Include methods to issue and return books. """
class Library_books():
    def __init__(self,title,author):
        self.__book_title = title
        self.__book_author = author
        self.__book_availability = True
    def book_issue(self):
        if(self.__book_availability):
            self.__book_availability = False
            print(f"The book {self.__book_title} is issued.")
        else:
            print(f"{self.__book_title} book is alreday issued.")
    def return_book(self):
        if(not self.__book_availability):
            self.__book_availability = True
            print(f"{self.__book_title} is returned. ")
        else:
            print(f"{self.__book_title} is already available.")
    def display_book(self):
        print(f"Book name: {self.__book_title}")
        print(f"Book author: {self.__book_author}")
        print(f"Book availability: {self.__book_availability}")
student1 = Library_books("Python programming", "john smith")
student1.display_book()
student1.book_issue()
student1.display_book()
student1.return_book()
student1.display_book()

            