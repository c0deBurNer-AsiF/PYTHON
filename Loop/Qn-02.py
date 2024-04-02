#write a python script to print next prime number of a given number.

x=int(input("Enter a number to get next prime number"))
n=x

while x:
    i=2
    n+=1
    while n>i:
        if n%i==0:
            break
        
        i+=1

    if i==n:
        break


print("Next prime number is:",i)    
