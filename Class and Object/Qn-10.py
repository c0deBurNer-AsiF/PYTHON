#Define a class team with instance object variable a list of team members name.
#provide methods to input members names and display members names

class team:
    def __init__(self):
        self.names=[]

    def input_members_names(self):
        self.names=[e for e in input("Enter team members names seprated by comma:").split(",")]

    def display_names(self):
        print(self.names)

'''
obj=team()
obj.input_members_names()
obj.display_names()
'''
