#check if an year is a leap year or not(TSRS)

def leap(y):
    return print('Its leap year' if int(y)%400==0  else 'not leap year' if y.endswith('00')   else 'leap year' if int(y)%4==0 else'not a leap year')


#2nd method--->
'''
def leap(y):
    return print('Its leap year' if int(y)%400==0  else 'not leap year' if y.endswith('00')   else 'leap year' if int(y)%4==0 else'not a leap year')
result=leap(input("Enter a year:"))        
'''
