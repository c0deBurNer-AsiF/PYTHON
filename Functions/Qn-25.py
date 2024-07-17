#print all factors of a given number(TSRN)

def factors(n):
      for i in range(1,n+1):
           if n%i==0:
                 print(i,end=',')


#2nd method--->
'''
def factors(n):
      for i in range(1,n+1):
           if n%i==0:
                 print(i,end=',')
factors(int(input("Enter a number:")))
'''
