#write a python function to find numbers from a given text, store number in a given list and return list(TSRS)

def num_find(l):
    l1=[]
    for e in l:
        for i in e[::]:
            if i not in '0123456789':
                break
        else:
            l1.append(e)    
    return print(l1)

#result=num_find([e for e in input("Enter a text:").split(" ")])
