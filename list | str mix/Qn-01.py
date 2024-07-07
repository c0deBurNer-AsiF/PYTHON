#remove all non int value from a list:

l,l1=[eval(e)for e in input("Enter heterogenious value seprated by comma:").split(",")],[]
for i in l:
    if type(i)!=int:
        l1.append(i)
print(l1)
