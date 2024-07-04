#write a pyhthon script to check whether a given number is positive, negative or zero
x=int(input("Enter a number:"))
match x:
    case x if x>0:
        print("Its a positive number!")
    case x if x==0:
        print("Its a zero")
    case x if x<0:
        print("Its a negative number!")        
     
