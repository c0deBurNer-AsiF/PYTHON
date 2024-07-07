#print distinct elements along with their frequencies of occurences in the list:

l=[int(e) for e in input("Enter integer value seprated by comma:").split(",")]
i=0
for e in l:
    if i==l.index(e):
        print(e,"occurance-->",l.count(e))
    i+=1
