'''write a python script to calculate sum of all even numbers and sum of all odd numbers
of the list. List data given by user''' 

l=[int(e)for e in input("Enter numbers").split(',')]
odd=0
even=0
for n in l:
    if n%2==0:
        even=even+n

    else:
        odd=odd+n

print("Sum of even numbers:",even)        
print("Sum of odd numbers:",odd)            
