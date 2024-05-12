'''
Define a class Student with instance variables rollno, name, semester, branch. Also define instance member
functions for user input data to set values of instance variables and display students data
'''

class student:
    def inputdata(self):
        self.name=input("Enter your name")
        self.rollno=input("Enter your rollno")
        self.semester=input("Enter your semester")
        self.branch=input("Enter your branch")
    def showdata(self):
        print("Name:",self.name,"|","Roll No.:",self.rollno,"|","Semester:",self.semester,"|","Branch:",self.branch)

