#write a python script to check whether two given numbers is co-prime or not.

x=int(input("enter 1st number:"))
y=int(input("Enter 2nd number:"))
i=2
while i<=x:
    if x%i==0 and y%i==0:
        break
    else:
        i+=1

if i>x:
    print("Co-prime")
else:
    print("Non co-prime")

   
        
