#define a class polygon with instance object variable to store number of sides and a list of n sides length value
#Define a subclass triangle of polygon with instance method getArea()

            
class polygon:

    def __init__(self):
        self.number_of_sides=int(input("Enter number of sides:"))
        self.list=[eval(e) for e in input("Enter {} values of sides separated by comma:".format(self.number_of_sides)).split(',')]
class triangle_of_polygon(polygon):
    def __init__(self):
        super().__init__()
    def perimeter(self): 
          
        self.semi_perimeter= (self.list[0]+self.list[1]+self.list[2])/2
        
    def getArea(self):
       return print('Area of this triangle:',(self.semi_perimeter*((self.semi_perimeter-self.list[0])*(self.semi_perimeter-self.list[1])*(self.semi_perimeter-self.list[2])))**.5)
    



'''
obj=triangle_of_polygon()
obj.perimeter()
obj.getArea()
'''
