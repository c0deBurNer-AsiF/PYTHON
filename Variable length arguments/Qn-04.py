#write a function which takes variable length arguments to recive strings.
# return the list of maximum length string or strings if multiple strings  have same length 


def max_str(*t):
    length=0
    for i in t:
        if length<len(i):
            length=len(i)

    return [e for e in t if length==len(e)]
'''
s=(input("Enter strings seprated by comma:").split(','))
result=print(max_str(*s))            
'''
