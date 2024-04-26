#write a python function to print reverse of a binary representation of a given number.(Takes Something, Return Nothing)

def rbin(x):
    while x>0:
        print(x%2,end=' ')
        x=x//2



#2nd method---->
'''
def reverse(y):
    y=bin(y)[2::]
    print(y[::-1])
       
x=int(input("Enter a number for print reverse of binary representation:"))
reverse(x)
'''
