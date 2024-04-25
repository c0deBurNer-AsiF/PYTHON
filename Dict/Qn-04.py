#write a python script to sort a dict according to VALUE

d={int(e[0:e.index(':'):]):e[e.index(':')+1::] for e in input("Enter a key and value like this key:value,key:value...:").split(',')}
for i in sorted(d.values()):
    for e in d:
       if i==d[e]:
        print(e,'----',d[e])
