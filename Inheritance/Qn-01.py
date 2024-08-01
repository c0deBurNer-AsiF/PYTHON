#define a class Person with instance object variables name and age. 
#provide __init__() method to set instance object variables. Also define methods to show name and age.
#now define a subclass Employee of person with instance object variable salary
#provide __init__() method to initialise instance variable. Also define instance method to show Employee data

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def showData(self):
        print(self.name)
        print(self.age)

class employee(person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary

    def show_employee_data(self):
        super().showData()
        print(self.salary)
'''
obj=employee("Asif",21,50000)
obj.show_employee_data()
'''

#2nd process---->



class person:
    def __init__(self):
        self.name=input("Enter your name:")
        self.age=int(input("Enter your age:"))

    def showData(self):
        print(self.name)
        print(self.age)

class employee(person):
    def __init__(self):
        super().__init__()
        self.salary=eval(input("Enter your salary:"))

    def show_employee_data(self):
        super().showData()
        print(self.salary)
'''
obj=employee()
obj.show_employee_data()
'''
