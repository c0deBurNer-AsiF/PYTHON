#define a class rectangle with lenght and breadth as instance object variable.
#provide setDimension(),showDimension() and getArea() method in it.




class rectangle:
    def setDimension(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def showDimension(self):
        print("Length:",self.length,"\nBreadth:",self.breadth)

    def getArea(self):
        return print('Area:',self.length*self.breadth)
'''   
obj=rectangle()
obj.setDimension(7,5)
obj.showDimension()
obj.getArea()    
'''

class rectangle:
    def setDimension(self):
        self.length=int(input("Enter length of the rectangle:"))
        self.breadth=int(input("Enter breadth of the rectangle:"))

    def showDimension(self):
        print("Length:",self.length,"\nBreadth:",self.breadth)

    def getArea(self):
        return print('Area:',self.length*self.breadth)
'''       
obj=rectangle()
obj.setDimension()
obj.showDimension()
obj.getArea()    
'''
