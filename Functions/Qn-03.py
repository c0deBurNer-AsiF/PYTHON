#write a python function to print first N prime numbers.(Takes Something, Return Nothing)

def nprime(x):
    a=2
    while x>0:
        if all(a%i!=0 for i in range(2,a)):
            print(a)
            x-=1
        a+=1   


#2nd method---->
'''
def prime(a):
    x=2
    while a>0:
       if all(x%i!=0 for i in range(2,x)):
           print(x,end=' ')
           a-=1
       x+=1    


p=int(input("Enter a number to get prime numbers:"))
prime(p)
'''
