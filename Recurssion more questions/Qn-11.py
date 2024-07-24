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



#write a recursive funtion to print first N prime numbers



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



