'''write a python script to print indices of all occurrence of a given element in a given list'''

l=[int(a)for a in input("Enter numbers which are separeted with comma").split(',')]
print(l)
s=0
n=int(input("Enter any number from this list"))
for e in l:
    if e==n:
        s=l.index(e)
        print(s,end=" ")
        l.remove(e)
        l.insert(s,0)


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
