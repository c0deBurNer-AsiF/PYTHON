#Write a python script to count vowels in a given string

l=input("Enter a string:")
vowels="AEIOUaeiou"
count=0
for x in vowels:
    for a in l:
        if x==a:
            count+=1

print("Vowels in this string:",count)
