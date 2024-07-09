
#write a python script to create a set of tuple , wheres each tuple has 2 elements representing dice upper face number.
#take a number N from user and generate all possible tuples, in such a way that tuple elements sums to N

x=int(input("Enter a number which is sum of a dice:"))
s=set()
for i in range(1,7):
    for j in range(1,7):
        if i+j==x:
            s.add((i,j))
print(s)            
