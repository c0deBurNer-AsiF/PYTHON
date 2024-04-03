#write a python script to print first N prime number. Value of N is given by user.

x=int(input("Enter how many prime number you want:"))
i=2
n=1
while x>0:
    n+=1
    i=2
    while n>i:
        if n%i==0:
            break
        else:
            i+=1

    if n==i:
        print(i)
        x-=1
  
