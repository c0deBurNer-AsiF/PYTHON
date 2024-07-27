#write a python script to find number of vowels in each of the string in a given list of the string.
#Use map function

def count_vowels(s):
    count=0
    for e in s:
        if e in 'aeiouAEIOU':
            count+=1
    return count
def f1():
    s=[e for e in input("Enter strings seprated by comma:").split(",")]
    print(list(map(count_vowels,s))) 
#f1()
