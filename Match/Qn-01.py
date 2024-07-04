#write a pyhthon script to check whether a given number is a three digit number or not

x=int(input("Enter a number:"))
match x:
    case x if 99<x<1000:
        print("Its a three digit number")
    case x if 0<x<100 or x>999:
        print("Its not a three digit number")
     

    
