'''write a python script to print indices of all occurrence of a given element in a given list'''

l=[int(a)for a in input("Enter numbers which are separeted with comma").split(',')]
print(l)
n=int(input("Enter any number from this list"))
i=0
for e in l:
    if e==n:
        print(l.index(e))
        l.remove(e)

#2nd method---->
'''
l=[int(e) for e in input("Enter numbers separated by comma:").split(',')]
x=int(input("Select any element from this list"))
print(l)
i=0
while i<len(l):
    if l[i]==x:
        print(i,end=" ")
    i+=1   
'''
