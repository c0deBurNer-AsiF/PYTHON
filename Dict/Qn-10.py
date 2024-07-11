#create a dict object from a list of city names in such a way the alphabets are keys of dictionary and
# list of city names starting from that alphabet will be its data value 

l=['paris','kolkata','delhi','mumbai','pune','patna','kerala','deradun','karnataka','maharashtra','nalasupara','kalibari','mandarmani']
d={}
while len(l)>0:
        l1=[]
        l1=[l[0]]
        for j in l[1::]:
            if l[0][0]==j[0]:
                l1.append(j)
        d[l[0][0]]=l1
        l=[e for e  in l if e not in l1]

print(d) 

#2nd method---->
'''
l=['paris','kolkata','delhi','mumbai','pune','patna','kerala','deradun','karnataka','maharashtra','nalasupara','kalibari','mandarmani']
d={}
for i in 'abcdefghijklmnopqrstuvwxyz':
    l1=[]
    for j in l:
        if j.startswith(i):
            l1.append(j)
    if len(l1)>0:        
        d[i]=l1
print(d) 
'''

