#Write a python script to create a dictionary in which each item is a pair of roll number (as KEY) and student name (as VALUE)



words={}
l=list(input("Enter Roll number:").split(','))
for i in l:
   print("Enter name of this roll number:",i)
   words[i]=input()
print(words)
