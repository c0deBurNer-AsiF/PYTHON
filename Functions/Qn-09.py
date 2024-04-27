#write a python function whicb takes a list of string as an argument and returns a dictionary
#whose each item is a pair of alphabet (as key) and list of strings begin with the alphabets.
def dic(l):
    l1=[]
    for i in l:
        l1.append(i[0:1:])
    d={l1[i]:[l[i]] for i in range(0,len(l1))}   
    return d

n=[e for e in input("Enter strings seprated with comma:").split(',')]
print(dic(n))


#2nd method---->
'''
def dic(l):
    l1=[]
    for i in l:
        l1.append(i[0:1:])
    d={l1[i]:[l[i]] for i in range(0,len(l1))}   
    return d
 '''   
