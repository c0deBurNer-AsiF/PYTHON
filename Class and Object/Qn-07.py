#define a class circle with instance object variable radius. Provide setter and getter for radius.
#also define getArea() and getCircumference() method 

class circle:
    def __init__(self,radius):
        self.radius=radius
    def getter(self):
        return self.radius
    
    def setter(self,new_radius):
        self.radius=new_radius

    def getArea(self):
        return 3.14*self.radius**2 

    def getCircumference(self):
        return 2*3.14*self.radius
'''
obj=circle(5)
print(obj.getter())
obj.setter(7)
print(obj.getArea())
print(obj.getCircumference())
'''


#2nd type--->


class circle:
    def __init__(self,radius):
        self.radius=radius
    def getter(self):
        return print(self.radius)
    
    def setter(self,new_radius):
        self.radius=new_radius
        return print("New radius value:",self.radius)

    def getArea(self):
        return print('Area:',3.14*self.radius**2) 

    def getCircumference(self):
        return print("Circumference:",2*3.14*self.radius)
'''
obj=circle(5)
obj.getter()
obj.setter(7)
obj.getArea()
obj.getCircumference()
'''
