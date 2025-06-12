class student:

    def __init__(self,fname,age):
        self.fname=fname
        self.age=age


    def student_details(self):
        print(f"the student name is {self.fname} and age is {self.age}")

s1=student("vishnu",18)
s1.student_details()
