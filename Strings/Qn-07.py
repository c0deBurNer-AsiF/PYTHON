#write a python script to check whether a given string is a palindrome or not

l=input("Enter a string:")
if l==l[::-1]:
    print("Its a palindrome")
else:
    print("Its not a palindrome")

#2nd method---->

'''
l=input("Enter strings:")
i=0
n=len(l)-1
while i<len(l) and n>=0:
    if l[i]!=l[n]:
        break
    n-=1
    i+=1
if i>=len(l) and n<0:
    print("Palindrome")
else:
    print("not a palindrome")

'''
