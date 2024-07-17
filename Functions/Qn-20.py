#calculate factorial of a number(TSRS)

def fact(n):
   m=1
   for i in range(1,n+1):
    m=m*i
   return print('factorial of {} is {}'.format(n,m))




#2nd method---->
'''
def fact(n):
   m=1
   for i in range(1,n+1):
    m=m*i
   return print('factorial of {} is {}'.format(n,m))
result=fact(int(input("Enter a number:")))   
'''
