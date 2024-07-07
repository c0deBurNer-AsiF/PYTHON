
#to find frist repeated string in a list of string:


l=[e for e in input("Enter a string sperated by comma:").split(",")]
i=0
for e in l:
    if i!=l.index(e):
        print('This is the first repeated string in this strings:-->',e)
        break
    i+=1
