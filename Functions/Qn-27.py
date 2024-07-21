#count words in a string(TSRS)

def c_words(s):
    s=s.strip()
    count=0
    for i in range(0,len(s)):
        if s[i]==' ' and s[i+1]!=' ':
            count+=1
    return print("Total words in this string is {}".format(count+1))



'''
def c_words(s):
    s=s.strip()
    count=0
    for i in range(0,len(s)):
        if s[i]==' ' and s[i+1]!=' ':
            count+=1
    return print("Total words in this string is {}".format(count+1))
result=c_words(input("Enter a string:"))
'''
