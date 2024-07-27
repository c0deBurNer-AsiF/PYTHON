#write a function to check if the given sides of a triangle can from a valid triangle or not.
#define a decorator to print 'Right Angled Triangle' if the triangle is right angle triangle 

def triangle_decor(triangle_function):
    def right_angle_or_not(a,b,c):
        print(triangle_function(a,b,c))
        if (a+b>c and a+c>b and b+c>a)==True:
            l=[]
            l.append(a),l.append(b),l.append(c)
            l=sorted(l)
            print("Its a right angle triangle" if l[0]**2+l[1]**2==l[2]**2 else "Its not a right angle triangle")
                
        else:
            print("Because of invalid triangle!!.. right angle triangle is not possible!!")
    return right_angle_or_not
                    

@triangle_decor
def triangle_valid_or_not(a,b,c):
   return 'Its a valid triangle' if (a+b>c and a+c>b and b+c>a)==True else 'Its not a valid triangle'

#triangle_valid_or_not(3,4,5)    
