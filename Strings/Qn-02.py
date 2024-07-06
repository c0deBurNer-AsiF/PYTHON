#Write a python script to count vowels in a given string

count=0
for i in input("Enter a string:"):
    if i in "aeiouAEIOU":
       count+=1
print("Total number of vowels--->",count)        



#2nd method--->
'''
l=input("Enter a string:")
vowels="AEIOUaeiou"
count=0
for x in vowels:
    for a in l:
        if x==a:
            count+=1

print("Vowels in this string:",count)
'''
