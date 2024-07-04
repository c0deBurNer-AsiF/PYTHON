#write a python script to check if a year is leap year or not


x=input("Enter a year to check its leap year or not:")
if x[-1]=='0' and x[-2]=='0':
    if int(x)%400==0:
        print("Its a leap year")
    else:
        print("Its not a leap year")
else:
    if int(x)%4==0:
        print("Its a leap year")
    else:
        print("Its not a leap year") 



#2nd method--->
'''
x=int(input("Enter a year"))

if x%100==0:
    if x%400==0:
        print("Its a leap year")
    else:
        print("Its not a leap year")

elif x%100!=0:
    if x%4==0:
        print("Its a leap year")
    else:
        print("Its not a leap year")
    
'''
