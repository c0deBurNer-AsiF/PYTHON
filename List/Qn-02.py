#write a python script to find the greates number in the list of integers given by user.

l=[int(e) for e in input("Enter any number which are separated by comma").split(',')]
l.sort()
l.reverse()
print("Greatest number is",l[0])

#2nd method--->
'''
l=[int(x) for x in input("enter numbers separated by comma:").split(',')]
print("Maximum number of this list is:",max(l))
'''
