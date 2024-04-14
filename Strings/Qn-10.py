#write a python script to count occurence of a given pattern in a given string


s=input("Enter strings:")
p=input("Enter the pattern which one u want to search:")
if p in s:
    print(p,"---->",s.count(p))
else:
    print(p,"is not in the string:",s)
        

    

