#Write a python script to find out common elements between two sets.


s1=set(eval(input("Enter first set:")))
s2=set(eval(input("enter second set:")))
for e in s1.intersection(s2):
    print(e,end=' ')
