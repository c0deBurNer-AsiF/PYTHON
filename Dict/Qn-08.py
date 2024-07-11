#create a dictionary where key values are cricket player name and data-values are tuple of 4 elements-->
#matches played,total runs,half centuries and centuries

n=int(input("How many players detail you want to store:"))
d={}
for i in range(0,n):
    p,m,t_n,h_c,c=input("\nenter {}st player name:".format(i+1)),int(input("Total match played:")),int(input("Total runes:")),int(input("half centuries:")),int(input("Total centuries:"))
    d[p]=(m,t_n,h_c,c)
print("\n",d)  




#2nd method---->
'''
print("Enter keys as player name and values are tuple of matches played,total run,half centuries,centuries-->")
print("Input values like that--->player_name:Match_played, Total_runs, Half_centuries, Centuries:")
print("Values are seprated by 'space'")
d={e[0:e.index(':')]:eval(e[e.index(':')+1::]) for e in input().split(" ")}
print(d)
'''
