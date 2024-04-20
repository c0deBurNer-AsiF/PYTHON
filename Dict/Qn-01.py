#Write a python script to print dict items(KEY, VALUE), each in one line.

words={}
l=list(input("Enter characters:").split(','))
for i in l:
   print("Enter words for key",i)
   words[i]=input()
for i,k in words.items():
   print(i,"--->",k)
