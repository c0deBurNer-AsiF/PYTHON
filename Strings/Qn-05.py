#write a python script to count occurence of a given pattern in a given string

l=input("Enter string").strip()
print("Total words in this string-->",len([i for i in range(0,len(l)) if l[i]==' ' and l[i+1]!=' '])+1)


#2nd method--->

'''
l=input("Enter strings:").strip()
count=1
for i in range(0,len(l)):
    if l[i]==' ' and l[i+1]!=' ':
        count+=1
    i+=1

print("Total words in this string-->",count)

 ''' 
