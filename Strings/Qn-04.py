#Write a python script to count occurrence of a given character in a given string.

l=input("Enter strings:")
x=input("Enter a character of occurrence count:")
count=0
for a in l:
    if a==x:
        count+=1
print("Occurrence of",x,"--->",count)
