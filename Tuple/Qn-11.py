#write a python script to check whether a tuple is a subset of another tuple or not

t1=eval(input("Enter a tuple (say t1):"))
t2=eval(input("Enter a tuple (say t2):"))
i=0
n=0
if len(t1)>=len(t2):
    while i<len(t2):
        n=0
        while n<len(t1):
            if t2[i]==t1[n]:
                break
            else:
                n+=1        
        else:
            print("t2 is not subset of t1")
            break
        i+=1    
    else:
        print("t2 is subset of t1")
        
if len(t2)>=len(t1):
    while i<len(t1):
        n=0
        while n<len(t2):
            if t1[i]==t2[n]:
                break
            else:
                n+=1        
        else:
            print("t1 is not subset of t2")
            break
        i+=1    
    else:
        print("t1 is subset of t2")




