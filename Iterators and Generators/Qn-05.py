#use iter and next method to check if all the elements of a list are even numbers using while loop
#which should work equivalent to for loop 



def all_even_or_not():
    l=[eval(e) for e in input("Enter numbers seprated by comma:").split(',')]
    it=iter(l)
    while True:
        try:
            if next(it)%2!=0:
               return False
        except StopIteration:
            break
    return True
'''
print(all_even_or_not())        
'''

#2nd process--->>



def if_all(l,isEven):
    it=iter(l)
    while True:
        try:
            if isEven(next(it)):
                return False
        except StopIteration:
            break
    return True
#print(if_all([12,3,10,6],lambda n : n%2==0))       



#3 print only even---->>


def print_even():
    l=[eval(e) for e in input('Enter elements seprated by comma:').split(',')]
    it=iter(l)
    while True:
        try:
            a=next(it)
            if a%2==0:
                print(a,end=' ')

        except StopIteration:
            break

print_even()

