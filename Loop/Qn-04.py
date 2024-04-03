#write a python script to print all prime numbers between two given numbers.

x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
i=2


while x<y:
    x+=1
    i=2
    while x>i:
        if x%i==0:
            break
        else:
            i+=1

    if x==i:
        print(x)
      
