
#print N natural number
def n_natural(n):
    if n>0:
        n_natural(n-1)
        print(n,end=(','))
    
#n_natural(5)


#print N natural number in reverse
def n_natural(n):
    if n>0:
        print(n,end=(','))
        n_natural(n-1)
    
#n_natural(5)


#print N odd numbers
def n_odd(n):
    if n>0:
        n_odd(n-1)
        print(n*2-1)
#n_odd(5)


# print N odd numbers in reverse order
def n_odd(n):
    if n>0:
        print(n*2-1)
        n_odd(n-1)
#n_odd(5)     


#print "c0deBurner" 5 times
def N_times_print(r=5):
    if r>0:
        print("c0deBurner")
        N_times_print(r-1)
#N_times_print()


#print N even natural number
def N_even_natural(n):
    if n>0:
        N_even_natural(n-1)
        print(n*2,end=" ")
#N_even_natural(10)



#print N even natural number in reverse
def N_even_natural(n):
    if n>0:
        print(n*2,end=" ")
        N_even_natural(n-1)
#N_even_natural(10)


#print squres of N natural number
def n_sqr(n):
    if n>0:
        n_sqr(n-1)
        print(n**2,end=' ')
#n_sqr(10)        


#print cubes of N natural number
def n_cubes(n):
    if n>0:
        n_cubes(n-1)
        print(n**3,end=' ')
#n_cubes(10) 



#reverse of a number
def reverse(n):
    if n<10:
        return print(n)
    print(n%10,end=(""))
    reverse(n//10)
#reverse(234637)


#sum of N natural number
def Nsum(n):
    if n==1:
        return 1
    return n+Nsum(n-1)
#print(Nsum(5))  



#sum of odd numbers
def nOddSum(n):
    if n==1:
        return 1
    return n*2-1+nOddSum(n-1)
#print(nOddSum(5))



#sum of even natural number
def nSumEven(n):
    if n==1:
        return 2
    return n*2+nSumEven(n-1)
#print(nSumEven(5))


#sum of square of N natural number
def SumSqr(n):
    if n==1:
        return 1
    return n**2+SumSqr(n-1)
#print(SumSqr(5))



#sum of cubes of N natural  number
def SumCubes(n):
    if n==1:
        return 1
    return n**3+SumCubes(n-1)
#print(SumCubes(5))



#sum of a digit 
def sum_digit(n):
    if n<10:
        return n
    return n%10+sum_digit(n//10)
#print(sum_digit(456))



#factorial of a number
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
#print(fact(5))



#decimal to binary
def binary(n):
    if n>0:
        binary(n//2)
        print(n%2,end="")
#binary(25)



#decimal to octal 
def oct(n):
    if n>0:
        oct(n//8)
        print(n%8,end="")

#oct(13)    



#print first N prime numbers 
def prime(n,m=2,i=2):
    if n>0:
        if i<m:
            if m%i==0:
                return prime(n,m=m+1,i=2)
            elif m%i!=0:
                return prime(n,m,i=i+1)
        elif i==m:
            print(m,end=" ")
            prime(n-1,m=m+1,i=2)
#prime(11)



#write a recursive funtion to calculate sum of first N prime numbers
def prime(n,m=2,i=2):
    if n>0:
        if i<m:
            if m%i==0:
               return  prime(n,m=m+1,i=2)
            else:
               return prime(n,m,i=i+1)
        else:
            return m + prime(n-1,m=m+1,i=2)
    return 0    
            
#print(prime(5))        
