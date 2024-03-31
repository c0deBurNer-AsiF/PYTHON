#write a python script to print a set of three words in dictionary order. words are given by user

x=str(input("Enter 1st name"))
y=str(input("Enter 2nd name"))
z=str(input("Enter 3nd name"))

if x<y<z:
    print(x,y,z,sep=" ")
    
elif y<x<z:
    print(y,x,z,sep=" ")

elif z<y<x:
    print(z,y,x,sep=" ")

elif z<x<y:
    print(z,x,y,sep=" ")

elif y<z<x:
    print(y,z,x,sep=" ")

elif x<z<y:
    print(x,z,y,sep=" ")
