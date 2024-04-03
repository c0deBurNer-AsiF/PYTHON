#write a python script to check whether two given numbers is co-prime or not.

x=int(input("enter 1st number:"))
y=int(input("Enter 2nd number:"))
i=1
while i<=x*y:
    if i%x==0 and i%y==0:
        break
    else:
        i+=1

print("LCM of {} and {} is {}".format(x,y,i))        
