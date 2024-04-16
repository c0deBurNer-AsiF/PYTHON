#write a python script to compare two tuples, whether they contain the same elements in any order or not

t1=sorted(eval(input("Enter first tuple:")))
t2=sorted(eval(input("Enter second tuple:")))
print("They contains the same elements") if t1==t2 else print("They can't contains the same elements")
