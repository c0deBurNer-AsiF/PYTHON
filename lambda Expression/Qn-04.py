#write a lambda expression to find HCF of two numbers
 
hcf=(lambda a,b,i=None:(i if a%i==0 and b%i==0 else hcf(a,b,i=i-1)) if i is not None else hcf(a,b,i=min(a,b)))
print(hcf(12,17))
