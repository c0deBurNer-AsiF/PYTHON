#Write a python script to sort a dict according to KEY

print("Enter rollno and name like this rollno:name,rollno:name....:")
d={int(e[0:e.index(':'):]):e[e.index(':')+1::] for e in input().split(',')}
for k in sorted(d):
   print(k,'---',d[k])



#2nd type---->>

'''
words={}
l=list(input("Enter character as a key:").split(','))
for i in l:
   print("Enter name of this roll number:",i)
   words[i]=input()
for i,k in sorted(words.items()):
   print(i,'---',k)
'''
