#write a python function to calculate LCM of two numbers.(Takes something, Return something)

def lcm(a,b):
    g=a if a<b else b
    l=g
    while l<=a*b:
        if l%a==0 and l%b==0:
            return l  
        l+=g  




#2nd method---->

            '''
def lcm(x,y):
    for i in range(x if x<y else y,(x*y)+1):
        if i%x==0 and i%y==0:
            break
    return i


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=lcm(a,b)
print("LCM of {} and {} is {}".format(a,b,c))

''''


#3rd method---->
'''
def lcm(x,y):
    return next(i for i in range(x if x<y else y,(x*y)+1) if i%x==0 and i%y==0)
    
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=lcm(a,b)
print("LCM of {} and {} is {}".format(a,b,c))

''''
