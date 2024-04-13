#write a python script to remove duplicate characters from a given string.

l=input("Enter strings:")
for e in l:
    if l.count(e)==1:
        print(e)




#remove duplicate words from a string----->
'''
n=int(input("Enter how many names you want to add:"))
l=[]
for e in range(n):
    print(e+1,"Enter name")
    l.append(input())
    
print("Non repeatable words are:")
for e in l:
    if l.count(e)==1:
        print(e)
'''



#removing if any words repeat more than 1 time , then 2nd repeatable word will be removed--->
'''
n=int(input("Enter how many names you want to add:"))
l=[]
for e in range(n):
    print(e+1,"Enter name")
    l.append(input())
    
s=set(l)
for e in s:
    print(e)
'''    
