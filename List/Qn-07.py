'''write a python script to print distinct list elementd along with their frequency of occurrence in the list'''

l=[int(a)for a in input("Enter numbers which are separeted with comma").split(',')]
i=0
for e in l:
    if i==l.index(e):
        print(e,"---",l.count(e))

    i+=1    
