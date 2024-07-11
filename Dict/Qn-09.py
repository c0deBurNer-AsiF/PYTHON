#write a python script to find maximum size of batch code from a dictionary, 
#where key values  in the dictionary are batch codes and data values are the size of the batch code

d={e[0:e.index(':')]:int(e[e.index(':')+1::]) for e in input("Enter batch name and batch size like batchName:batchSize...seprated by comma:\n").split(",")}
n=max(d.values())
for i in d:
    if n==d[i]:
        print(i)
        break 

#2nd method---->
'''
d={e:int(len(e)) for e in input("Enter bach codes(seprated by comma):").split(",")}
print(d)
n=max(d.values())
for i in d:
    if n==d[i]:
        print(i)
        break
'''

