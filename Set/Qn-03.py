#Write a python script to take union of two sets

s1=set(eval(input("Enter frist set:")))
s2=set(eval(input("Enter second set:")))
print("Union of two set's is")
for e in s1.union(s2):
    print(e,end=' ')
