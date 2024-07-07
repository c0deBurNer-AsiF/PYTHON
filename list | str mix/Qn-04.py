#count strings which ends at character "s" in a list of string:

l=[e for e in input("Enter strings seprated by comma:").split(",")]
count=0
for i in l:
    if i[-1]=="s":
        count+=1
print("total number of string ends with 's' -->",count)        

#2nd method--->
'''
l=[e for e in input("Enter strings seprated by comma:").split(",")]
count=0
for i in l:
    if i.endswith('s')==True:
        count+=1
print("Total number of strings end with 's'--->",count)        
'''
