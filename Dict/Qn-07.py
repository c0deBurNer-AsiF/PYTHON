#sort a dictonary by its key in decending order..
d={int(e[0:e.index(':')]): e[e.index(':')+1:] for e in input("Enter key and values like key:values,key:values...").split(",")}
sorted_keys=[]
for i in sorted(d.keys()):
    sorted_keys.append(i) 
print("Sorted keys are:",sorted_keys) 



#2nd method--->
'''
d={int(e[0:e.index(':')]): e[e.index(':')+1:] for e in input("Enter key and values like key:values,key:values...").split(",")}
d_sorted_keys={}
for i in sorted(d.keys()):
    d_sorted_keys[i]=d[i]
print(d_sorted_keys)    
'''
