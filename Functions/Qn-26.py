#Calculate lcm of two numbers(TSRS)

def lcm(x,y):
    i=x if x>=y else y
    while i<=x*y:
        if i%x==0 and i%y==0:
            return print("LCM of {} ,{} is {}".format(x,y,i))
        i+=1



'''
def lcm(x,y):
    i=x if x>=y else y
    while i<=x*y:
        if i%x==0 and i%y==0:
            return print("LCM of {} ,{} is {}".format(x,y,i))
        i+=1
result=lcm(int(input("Enter 1st number:")),int(input("Enter 2nd number:")))
'''
