#write a python function to calculate sum of all even numbers and sum of all odd numbers
#from a given list of int values(Takes Something, Return Something)

def sum_all(s):
    even=[]
    odd=[]
    for i in s:
        even.append(i) if i%2==0 else odd.append(i)
    return "sum of even numbers:",sum(even),"sum of odd numbers:",sum(odd)  



#2nd method--->
'''
def sum_all(s):
    even=[]
    odd=[]
    for i in s:
        even.append(i) if i%2==0 else odd.append(i)
    return "sum of even numbers:",sum(even),"sum of odd numbers:",sum(odd)        

  
l=[int(e) for e in input("Enter int values seprated by comma:").split(',')]
c=sum_all(l)
print(c) 
'''
