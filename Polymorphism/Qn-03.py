#define a class Reuslt to hold result data for a test(attempt,right and wrong)
#overload + operator to combine the result of two test


class Result:
    def __init__(self,a,r,w):
        self.attempt=a
        self.right=r
        self.wrong=w

    def show_data(self):
        print(self.attempt)
        print(self.right)
        print(self.wrong)

    def __add__(self,other):
        return(Result(self.attempt+other.attempt,self.right+other.right,self.wrong+other.wrong))
        
'''
obj1=Result(60,35,25)
obj2=Result(70,50,20)
obj3=obj1+obj2
obj3.show_data()
'''
