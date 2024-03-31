#write a python script to check if a year is leap year or not

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
    
