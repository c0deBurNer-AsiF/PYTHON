#Write a python script to create a dictionary in which each item is a pair of roll number (as KEY) and student name (as VALUE)

print("Enter rollno and name like rollno:name,rollno:name..:")
d={int(e[0:e.index(':'):]) : e[e.index(':')+1::] for e in input().split(',')}
print(d)



#2nd method
'''
words={}
l=list(input("Enter Roll number:").split(','))
for i in l:
   print("Enter name of this roll number:",i)
   words[i]=input()
print(words)
'''
