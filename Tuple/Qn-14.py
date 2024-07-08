#reverse a tuple:

print(tuple([eval(e) for e in input("Enter a tuple seprated by comma:").split(",")])[::-1])
