#Define a pyhton class person with instance object varibales name and age.
#set instace object varibles in __init__() method. Also define show() method to display name and age of a person


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(self.name,self.age,sep='\n')    

'''
obj=person('asif',21)
obj.show()
'''
