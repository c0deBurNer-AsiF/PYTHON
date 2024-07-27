#write a function to check if a given number N is prime or not.
# Define a decorator to print total number of prime number before N


def decor_prime(prime_function):
    def prime_before_n(n):
        print('Its prime' if prime_function(n)==True else 'Its not prime')
        print("Before {} , primes are:".format(n))
        for e in range(1,n):
            for i in range(2,e):
                if e%i==0:
                    break
            else:
                print(e,end=' ')
    return prime_before_n            

@decor_prime
def N_is_prime_or_not(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True        

#N_is_prime_or_not(int(input("Enter a number:")))

