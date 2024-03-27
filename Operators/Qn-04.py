#write a python script to calculate simple interest, data required should be taken from user

p=input("Enter the principal value:")
r=input("Enter the interest rate:")
t=input("Enter time period:")

s=int(p)*float(r)*int(t)/100
print("The simple interest is ",s)
