"""write a python script to print a sequence of number with given step size and boundary value.
For example boundary values are 10 and 30, step is 2 then your output should be 10,12,14,16,18,20,22,24,26,28,30"""

start=int(input("Enter the starting value:"))
stop=int(input("Enter the stop value:"))
step=int(input("Enter the sequence value:"))

for n in range(start,stop+1,step):
    print(n)
