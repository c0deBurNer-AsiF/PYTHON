
#create two sets from a given set of numbers to separate even and odd numbers

s,s_even,s_odd={eval(e) for e in input("Enter integers seprated by comma:").split(",")},set(),set()
for i in s:
    s_even.add(i) if i%2==0 else s_odd.add(i)
print("Even numbers are:{}\nOdd numbers are:{}".format(s_even,s_odd))
