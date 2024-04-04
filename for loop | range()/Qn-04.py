#write a python script to print squares of numbers from a to b. Value of a and b are given by user

a=int(input("Enter the starting number:"))
b=int(input("Enter the ending number:"))

for n in range(a,b+1,1):
    print(n**2)
