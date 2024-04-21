#Write a python script to take dictionary from the keyboard and print the sum of value.


print("Enter number and ammount  like this number:ammount,Number:ammount....:")
d={int(e[0:e.index(':'):]):e[e.index(':')+1::] for e in input().split(',')}
print("Sum of all values is:",sum(int(i) for i in d.values()))
  


