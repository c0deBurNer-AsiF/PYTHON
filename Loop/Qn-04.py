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

#using for else method
"""
a=int(input("Enter lesser number:"))
b=int(input("Enter greater number:"))

z=range(a+1,b)
for x in z:
    for num in range(2,x):
        if x%num==0:
            break
        
    else:
        print(x)
        """
      
