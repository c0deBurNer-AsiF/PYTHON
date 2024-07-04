
#write a python script to find maximum length word in a given string

s=input("Enter a string:").split(" ")
l=0
l1=[]
for i in s:
    if l<=len(i):
        l=len(i)
        l1=i
print("The maximum lenth word is:--->",l, "and the word is:-->",l1)        

    

