#write a lambda expression to check if a number is even. 

(lambda a:print("Its a even number" if a%2==0 else "Its not a even number"))(int(input("Enter a number to check its even or not:")))



# 2nd method--->>.




l=(lambda a:print("Its a even number" if a%2==0 else "Its not a even number"))
l(int(input("Enter a number to check its even or not:")))
