'''
Define a class Emoployee with instance variable empid, name, salary.
Define constructor to initialize member variables.
Define function to show emoployee data
'''


class Employee:
    def __init__(self,e,n,s):
        self.empid=e
        self.name=n
        self.salary=s
    def EmployeeData(self):
        print("Name:",self.name)
        print("Employee ID:",self.empid)
        print("Salary:",self.salary)
