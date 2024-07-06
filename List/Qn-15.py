#Create two list from a given list of numbers in such a way that 
# the first list can have only positive number and second list have only non positive number:


l1,l2=[],[]
for i in [int(e) for e in input("Enter numbers seprated by comma:").split(",")]:
    l1.append(i) if i>0 else l2.append(i)
print("Postive numbers are-->",l1)
print("Non-positive numbers are-->",l2)    
