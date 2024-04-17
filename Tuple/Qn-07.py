#write a python script to create tuples with homogeneous elements from a tuple containing heterogeneous elements


x=eval(input("Enter a tuple"))
t1,t2,t3,t4,t5=[],[],[],[],[]
for i in x:
    if type(i)==int:
        t1.append(i)
    elif type(i)==float:
        t2.append(i)
    elif type(i)==complex:
        t3.append(i)
    elif type(i)==str:
        t4.append(i)
    elif type(i)==bool:
        t5.append(i)
if len(t1)>0:
    print(tuple(t1))
if len(t2)>0:
    print(tuple(t2))
if len(t3)>0:
    print(tuple(t3))
if len(t4)>0:
    print(tuple(t4))
if len(t5)>0:
    print(tuple(t5))

