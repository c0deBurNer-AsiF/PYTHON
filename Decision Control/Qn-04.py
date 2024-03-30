#write a python script to find greatest among three numbers

x=int(input("Enter 1st number"))
y=int(input("Enter 2nd number"))
z=int(input("Enter 3rd number"))

if x>y and x>z:
    print("Greatest number is %d"%x)

elif y>x and y>z:
    print("Greatest number is %d"%y)

elif z>x and z>y :
    print("Greatest number is %d"%z)


