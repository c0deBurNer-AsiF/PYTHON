#write a python script to reverse a tuple

print("Reverse tuple is",tuple(reversed(eval(input("Enter a tuple:")))))




#2nd Method--->
'''
t=eval(input("Enter a tuple:"))
print("User entered tuple is:",t)
l=list(t)
l.reverse()
t=tuple(l)
print("Reverse tuple is:",t)
'''
