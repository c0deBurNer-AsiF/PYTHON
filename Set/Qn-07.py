#Write a python script to check whether a given set is a subset of another given set or not

s1=set(eval(input("Enter first set(say s1):")))
s2=set(eval(input("Enter second set(say s2):")))

print("s1 is subset of s2" if s1.issubset(s2) else "s2 is subset of s1" if s2.issubset(s1) else "None is subset of anyone")
