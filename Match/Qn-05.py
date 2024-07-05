'''
write a python script to take a string from user. 
if the string is part of "asif" then print 'One', 
if the string is part of "ali" then print "Two", 
if the string is part of "sahaji" then print "Three". 

'''
x=input("Enter a string:")
match x:
    case x if "asif" in x:
        print("One")
    case x if "ali" in x:
        print("Two")
    case x if "sahaji" in x:
        print("Three")        
