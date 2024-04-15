#write a python script to calculate average of tuple values. Assuming values are of int type only.

t=eval(input("enter tuple:"))
s=0
for i in t:
    s=s+i
print("Avarage of tuple values is",s/len(t)) 
