#sort list elements in descending order!

l=[int(e) for e in input("Enter numbers seprated by comma:").split(",")]
l.sort(reverse=True)
print(l)


#2nd method--->

'''
l=[int(e) for e in input("Enter number seprated by comma:").split(",")]
l.sort()
l.reverse()
print(l)
'''
