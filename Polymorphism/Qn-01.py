#define a python class person with name and age as a instance object variables.
#define Student and Teacher two subclasses of Person. 
#provide rollno as instance object variable in student, provide subject as instance object variable in Teacher class.
#Now define a function show to print values of instance object varibales in both the classes.
#Demonstrate polymorphic behaviour or show function


class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

class Student(Person):
    def __init__(self,n,a,r):
        super().__init__(n,a)
        self.rollNo=r

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

    def show_rollNo(self):
        print(self.rollNo)

class Teacher(Person):
    def __init__(self,n,a,s):
        super().__init__(n,a)
        self.subject=s
    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

    def show_subject(self):
        print(self.subject)
'''
obj=Student("asif",21,45)
obj.show_name()
obj.show_age()
obj.show_rollNo()
obj=Teacher("Nil",21,"Maths")
obj.show_name()
obj.show_age()
obj.show_subject()
'''


#2nd type---->>


class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

class Student(Person):
    def rollNo_input(self,r):
        self.rollNo=r

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

    def show_rollNo(self):
        print(self.rollNo)

class Teacher(Person):
    def subject_input(self,s):
        self.subject=s
    
    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

    def show_subject(self):
        print(self.subject)

'''
obj=Student("asif",21)
obj.rollNo_input(214045)
obj.show_name()
obj.show_age()
obj.show_rollNo()
obj=Teacher("Nil",21)
obj.subject_input("Maths")
obj.show_name()
obj.show_age()
obj.show_subject()
'''



#3rd type---->>


class Person:
    def __init__(self):
        self.name=input("Enter your name:")
        self.age=eval(input("Enter your age:"))

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

class Student(Person):
    def rollNo_input(self):
        self.rollNo=eval(input("Enter your roll number:"))

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

    def show_rollNo(self):
        print(self.rollNo)

class Teacher(Person):
    def subject_input(self):
        self.subject=input("Enter your subject name:")
    
    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

    def show_subject(self):
        print(self.subject)
'''
obj=Student()
obj.rollNo_input()
obj.show_name()
obj.show_age()
obj.show_rollNo()
obj=Teacher()
obj.subject_input()
obj.show_name()
obj.show_age()
obj.show_subject()
'''
