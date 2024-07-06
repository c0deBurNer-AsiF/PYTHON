#create a list from a given list by selected only even places elements!


l=[int(e) for e in input("Enter numbers seprated by comma:").split(",")]
l1=[]
for i in l[1::2]:
    l1.append(i)
print("Even places elements are:-->",l1)

