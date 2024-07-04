#write a python script to extract number from a given text and store all the numbers in a list


s=input("Enter a string:").split(" ")
print(s)
l=[]
for i in s:
    for n in i:
       if n not in '0123456789':
           break
    else:
        l.append(i)   
          

print(l) 
