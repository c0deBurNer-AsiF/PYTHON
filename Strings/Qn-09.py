#write a python script to find a pattern in a given string

s=input("Enter strings:")
p=input("Enter the pattern which one u want to search:")
if p in s:
    print(p,"is in the string:",s)
else:
    print(p,"is not in the string:",s)



#number wise pattern search---->
'''
l=input("Enter strings:").split(' ')
n=int(input("Enter the pattern:"))
for i in l:
    if len(i)==n:
        print(i)

'''
