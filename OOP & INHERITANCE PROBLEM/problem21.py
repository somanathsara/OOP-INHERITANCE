"""Online Quiz class  - create a class with encapsulated  attributes
for question , options , correct answers."""
class OnlineQuiz:
    def __init__(self):
        self.__question = ""
        self.__option = []
        self.__correct_ans = ""
    def set_data(self, question, options, correct_ans):
        self.__question = question
        self.__option = options
        self.__correct_ans = correct_ans
    def displaydetails(self):
        print(f"Number of question : {self.__question}")
        print(f"Options : {self.__option}")
        print(f"Correct answers : {self.__correct_ans}")
s1 = OnlineQuiz()
s1.set_data("What is the symbol of Gold ?", "Au,Cu,Ag,Na", "Au")
s1.displaydetails()