#write a python script to calculate sum of all the integers of the list given by user.

l=[int(a) for a in input("Enter numbers which are separeted with comma").split(',')]
s=0
for i in l:
    s=s+i
print("Sum of all integers numbers is %d"%s)
