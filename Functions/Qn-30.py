#filter out words from a text starting from a same alphabet and store them in a list.
#Now create a dict with alphabets as a key-values and list of words starting from that alphabet as a data vales
#take text as an argument and return dict object (TSRS)
def extract(text):
    d={}
    for e in 'abcdefghijklmnopqrstuvwxyz':
        l=[words for words in text.split(' ') if words.startswith(e)]
        if len(l)>0:
            d[e]=l
    return d

'''
def extract(text):
    d={}
    for e in 'abcdefghijklmnopqrstuvwxyz':
        l=[words for words in text.split(' ') if words.startswith(e)]
        if len(l)>0:
            d[e]=l
    return d

result=print(extract(input("Enter some text(seprated by one space)").strip().lower())) 
'''



#2nd method--->

'''
def key_values(s):    
    d,l,i={},[],0
    while i<len(s):
        l=[]
        l.append(s[i]) 
        for j in s[1::]:
            if s[i][0]==j[0]:
                l.append(j)                   
        d[s[i][0]]=l
        s=[e for e in s if e not in l]
    return print(d)
result=key_values(input("Enter text (dont use doble space):").strip().split(' '))
'''
           

