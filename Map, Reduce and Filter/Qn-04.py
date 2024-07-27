#write a python script to filter only int values in a given list elements.use filter function

def filtering_int():
    l=[eval(e) for e in input("Enter elements seprated by comma(if you type a stirng plz use ''):").split(',')]
    print(list(filter(lambda i: i if type(i)==int else None, l)))
filtering_int()


#2nd method---->

def filtering_intOnly(x):
    if type(x)==int:
        return x
    
#print(list(filter(filtering_intOnly,[eval(e) for e in input("Enter elements seprated by comma:(if you enter string , then use '' plz):").split(',')])))


