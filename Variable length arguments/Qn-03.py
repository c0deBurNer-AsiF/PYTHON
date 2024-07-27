#write a function which recieve variable length arguments to filter odd and even number.
#store all odd even numbers in a list and all even numbers in another list.
#store both lists in a tuple and return it


def odd_even(*t):
    l_odd,l_even=[],[]
    for i in t:
        l_odd.append(i) if i%2==0 else l_even.append(i)
    x=(l_odd,l_even)
    return x
'''    
n=(eval(i) for i in input("Enter integers seprated comma:").split(','))
result=print(odd_even(*n))
'''
