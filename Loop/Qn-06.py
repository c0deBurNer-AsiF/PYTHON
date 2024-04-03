#write a python script to print first N odd natural numbers in reverse order using range function in for loop.

x=int(input("Enter how many natural number you want to print in reverse order:"))

range(x)

for n in range(x*2-1,0,-2):
    print(n)
  
