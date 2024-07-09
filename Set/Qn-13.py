#given a set of five player names. 
#write a python script to form all possible pair of players that is selecting two players at a time

s={"player1","player2","player3","player4","player5"}
s1=set()
for i in s:
    for j in s:
        if i!=j:
            if (tuple([i,j]) and tuple([j,i])) not in s1:
                s1.add((i,j))
print(s1)

#2nd method--->
'''
s,s1={'player1','player2','player3','player4','player5'},set()
l,l1=list(s),[]

for i in range(0,len(l)):
    for j in range(1+i,len(l)):
        l1.append((l[i],l[j]))

s1=set(l1)
print(s1)
'''
