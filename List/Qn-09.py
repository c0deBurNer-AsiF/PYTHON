#calculate average of elements of a list:

l=[int(e) for e in input("Enter numbers sperated by comma:").split(",")] 
print("Average is-->",sum(l)/len(l))
