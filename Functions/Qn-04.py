#write a python function to count words in a given string.(Takes Something, Return Something)


def countwords(a):
    a=a.strip()
    return(len([i for i in range(0,len(a)) if a[i]==' ' and a[i+1]!=' '])+1) 



#2nd method---->
'''
def countwords(a):
    return(len([i for i in range(0,len(a)) if a[i]==' 'and a[i+1]!=' '])+1)
      
x=input("Enter a string:").strip()
print("Total words in this string:",countwords(x))

'''


#3rd method---->
'''
def countwords(a):
    count=1
    i=0
    while i<len(a):
        if a[i]==' ' and a[i+1]!=' ':
            count+=1
        i+=1
    return(count)   

x=input("Enter a string:").strip()
print("Total words in this string:",countwords(x))

''''
