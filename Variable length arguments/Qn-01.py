#write a function which recieve variable length arguments to calculate average of integers.
#it returns average of of numbers 

def avg(*t):
    return sum(t)/len(t)
'''
s=(eval(i) for i in input("Enter integers seprated by comma:").split(','))
result=print('Average of these intergers are:',avg(*s))
'''
