#use iter and next method to print values of a given list using while loop which works equivalent to for loop.

l=[eval(e) for e in input("Enter elements seprated by comma:").split(',')]
it=iter(l)
while True:
    try:
        print(next(it),end=' ')
    except StopIteration:
        break

