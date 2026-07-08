"""OnlineExam Class - Create a class with 
private attributes for exam name, total marks, and candidate score."""
class Online_Exam:
    def __init__(self):
        self.__exam_name = ""
        self.__total_marks = 0
        self.__candidate_score = 0
    def set_data(self, name, marks, candidatescore):
        self.__exam_name = name
        self.__total_marks = marks
        self.__candidate_score = candidatescore
    def show_details(self):
        print("Exam name :",self.__exam_name)
        print("Total marks :",self.__total_marks)
        print("Candiddate mark :",self.__candidate_score)
s1 = Online_Exam()
s1.set_data("Nirmal", 10, 8.15)
s1.show_details()