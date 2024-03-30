#write a python script to take month value in neumerical format and display number of days in it

print("1.January\n2.februrary\n3.March\n4.April\n5.May\n6.June\n7.July\n8.August\n9.September\n10.October\n11.November\n12.December")
x=int(input("which month's number you want to know:"))
if x==1:
    print("31 Days")
    
elif x==2:
    print("28 Days")

elif x==3:
    print("31 Days")

elif x==4:
    print("30 Days")

elif x==5:
    print("31 Days")

elif x==6:
    print("30 Days")

elif x==7:
    print("31 Days")    

elif x==8:
    print("31 Days")
    
elif x==9:
    print("30 Days")

elif x==10:
    print("31 Days")   

elif x==11:
    print("30 Days")

elif x==12:
    print("31 Days")

else:
    print("Invalid number")
