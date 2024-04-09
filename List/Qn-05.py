'''write a python script to create a list of squares of first N natural numbers.
Use for loop to fill list with elements. Value of N is taken from user''' 

a=int(input("Enter how many natural numbers squares you want:"))
s=range(1,a+1)
l=[]

for i in s:
    l+=[i**2]
print(l)

#2nd method--->
'''
l=[e**2 for e in range(1,int(input("Enter a natural number:"))+1)]
print(l)
'''
