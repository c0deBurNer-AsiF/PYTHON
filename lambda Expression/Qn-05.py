#write a lambda expression to find N term of fibonacci series

f=(lambda n,a=-1,b=1:f(n-1,a=b,b=a+b) if n>1 else print(a+b))
f(5)

# Nth number fibonacci only--->>
f=lambda n:n if n==0 or n==1 else f(n-1)+f(n-2)
print(f(5))
