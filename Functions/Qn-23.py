#print all prime number between two given number(TSRN)

def prime(a,b):
    for n in range(a+1,b):
        i=2
        while i<n:
            if n%i==0:
                break
            i+=1
        else:
            print(n,end=' ')



#2nd method--->
'''
def prime(a,b):
    for n in range(a+1,b):
        i=2
        while i<n:
            if n%i==0:
                break
            i+=1
        else:
            print(n,end=' ')
prime(int(input("Enter 1st number:")),int(input("Enter 2nd number:")))                
'''
