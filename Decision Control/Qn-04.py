#write a python script to find greatest among three numbers

x,y,z=int(input("Enter first number:")),int(input("Enter second number:")),int(input("Enter the thired number:"))
if x>y:
    print(x if x>z else z)
else:
    print(y if y>z else z)    


#2nd method--->
'''
x,y,z=int(input("Enter first number:")),int(input("Enter second number:")),int(input("Enter the thired number:"))
if x>=y>=z or x>=z>=y:
    print(x)
elif y>=x>=z or y>=z>=x:
    print(y)
elif z>=x>=y or z>=y>=x:
    print(z)
else:
    print(x)
'''    



#3rd method--->
'''
x=int(input("Enter 1st number"))
y=int(input("Enter 2nd number"))
z=int(input("Enter 3rd number"))

if x>y and x>z:
    print("Greatest number is %d"%x)

elif y>x and y>z:
    print("Greatest number is %d"%y)

elif z>x and z>y :
    print("Greatest number is %d"%z)
'''

