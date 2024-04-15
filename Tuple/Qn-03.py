#write a python script to marge two sorted tuples

t1=tuple(sorted(eval(input("Enter first tuple:"))))
t2=tuple(sorted(eval(input("Enter second tuple:"))))
t3=tuple(sorted((t1+t2)))
print("Resulting tuple is",t3)
