'''write a python script to print indices of all occurrence of a given element in a given list'''

l=[int(a)for a in input("Enter numbers which are separeted with comma").split(',')]
print(l)
n=int(input("Enter any number from this list"))
i=0
for e in l:
    if e==n:
        print(l.index(e))
        l.remove(e)
