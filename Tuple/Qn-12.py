#write a python script to count the frequency of elements of a tuple

t=eval(input("Enter tuple seprated by comma:"))
n=0
for i in t:
    if t.index(i)==n:
        print(i,"--->",t.count(i),"times")    
    n+=1
