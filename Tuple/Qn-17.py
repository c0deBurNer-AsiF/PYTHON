#sum of all the odd numbers stored in tuple

print("sum of all odd numbers stored in a tuple",sum([e for e in tuple([eval(e) for e in input("Enter integers seprated by comma:").split(",")]) if e%2!=0]))

