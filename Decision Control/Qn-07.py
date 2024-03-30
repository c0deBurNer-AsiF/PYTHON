#write a python script to check nature of roots of a given quadratic equations

a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=int(input("Enter the value of c"))

print("The Equation is\n")
print("%dx**2+%dx+%d"%(a,b,c))

sum=b**2-4*a*c

if sum<0:
    print("Roots are Imaginary")

elif sum>0:
    print("Roots are real")

else:
    print("Roots are Equal and real")
