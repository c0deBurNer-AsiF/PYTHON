#write a python function to find next prime number of a given number.(Takes Something, Return Something)

def prime(n):
    n=n+1
    while True:
         for i in range(2,n):
             if n%i==0:
                 break
         else:
             return "Next prime number is",n
         n+=1  

#2nd method---->
'''
def prime(n):
    n=n+1
    i=2
    while n:
        i=2
        while i<n:
            if n%i==0:
                n+=1
                break
            i+=1
        if i==n:
            return "Next prime number is",n        
'''



#3rd method---->
'''
def prime(n):
    n=n+1
    while True:
         for i in range(2,n):
             if n%i==0:
                 break
         else:
             return "Next prime number is",n
         n+=1   
l=int(input("Enter a number to get the next prime number:"))
print(prime(l))
'''
