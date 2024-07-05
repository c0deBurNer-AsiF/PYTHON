#print unique digit of a given integer:


x,i=input("Enter a integer:"),0
for e in x:
    if i==x.index(e):
        print(e,end=' ')
    i+=1    
