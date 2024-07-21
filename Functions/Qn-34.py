#find the largest sorted subsequence in a given list.Return the largest subsecuence as a list.(TSRS) 
#not completed

def largest_sorted_subsequence(l):
    l1,l2,i,n=[],[],0,0
    while i<len(l):
        if n<l[i]:
            l1.append(l[i])    
        else:
            if len(l2)<len(l1):
                l2=[e for e in l1]
                l1.clear()
                l1.append(l[i])
            else:
                l1.clear()
                l1.append(l[i])
        n=l[i]            
        i+=1        
    return print(l2)
#result=largest_sorted_subsequence([int(e) for e in input("Enter integer values(seprated by comma):").split(",")])    

