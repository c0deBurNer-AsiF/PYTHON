#create list of prime numbers between two given numbers(TSRS)

def isPrime(n):
    for e in range(2,n):
        if n%e==0:
            return False
        else:
            return True
def btw_2num_primes(a,b):
    l=[e for e in range(a+1,b) if isPrime(e)]
    return l 

'''
def isPrime(n):
    for e in range(2,n):
        if n%e==0:
            return False
        else:
            return True
def btw_2num_primes(a,b):
    l=[e for e in range(a+1,b) if isPrime(e)]
    return l    

result=print(btw_2num_primes(int(input("Enter 1st number:")),int(input("Enter 2nd number:"))))
'''

#2nd method--->

'''
def list_prime(a,b):
    l=[]
    for e in range(a+1,b):
       i=2
       while i<e:
             if e%i==0:
                 break
             i+=1
       else:
           l.append(e) 
    return print("List of prime numbers between {} and {} is {}".format(a,b,l)) 
            
result=list_prime(int(input("Enter 1st integer:")),int(input("Enter 2nd integer:")))
'''

