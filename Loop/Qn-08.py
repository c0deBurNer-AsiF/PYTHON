#write a python script to print all prime factors of a givren number.

x=int(input("Enter any number to get it's prime factors:"))
i=2
while i<=x:
    if x%i==0:
        x=x/i
        print(i,end=" ")
    
    else:
        i+=1
