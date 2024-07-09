#You have a list of name of candidates,
# some of then wearing black hat and some of them wearing red shoe and some of them wearing both.
# now you have to given a list of name of candidates wearing black hat.
# there is another list of candidates wearing red shoe.
# write a python script to find out the name of candidate wearing black hat and red shoe...


l=['player1','player2','player3','player4','player5']
l_cap=['player2','player3','player1']
l_shoe=['player2','player1','player3','player5']
s_cap=set(tuple(l_cap))
s_shoe=set(tuple(l_shoe))
print("Black hat and red shoe wearing candidates are:",s_cap.intersection(s_shoe))
