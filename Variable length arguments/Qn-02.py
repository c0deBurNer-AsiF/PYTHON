#write a function which recieve variable length arguments to find greatest argument. It returns greatest argument

def greatest_arg(*n):
    return max(n)
'''
t=(eval(i) for i in input("Enter integers seprated by comma:").split(","))
result=print("Greatest arguments is",greatest_arg(*t))
