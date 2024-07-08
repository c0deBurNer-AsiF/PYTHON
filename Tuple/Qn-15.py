
#Create a list of tuple from a given list of string, 
# where each tuple is a collection of string begin with same character

l=[e for e in input("Enter strings seprated by comma:").split(",")]
l1,l2,i=[],[],0
while l:
    for e in l[1::]:
        if l[i][0]==e[0]:
            l2.append(e)
    l2.append(l[i])
    l1.append(tuple(l2))
    l=[e for e in l if e not in l2]
    l2.clear()
print(l1)            





#2nd method---->

'''
l=[e for e in input("Enter strings seprated by comma:").split(',')]
l1,l2,i,j=[],[],0,0
while i<len(l):
    j=1+i
    while j<len(l):
        if l[i][0]==l[j][0]:
            l2.append(l[j])
            
        j+=1
    l2.append(l[i])
    print(l2)
    for e in l2:
        l.remove(e)
    l1.append(tuple(l2))
    l2.clear()
print(l1)       
'''
