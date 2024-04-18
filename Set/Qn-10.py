'''
two sets represent two identical dices.(dices value are follow 1 to 6).
Write a python script to produce sample space to get sum of dice values when rolled N. N is given by user
'''

n=int(input("Enter a number(between 2 to 12):"))
if 1<n<13:
   for i in range(1,7):
      for j in range(1,7):
         if i+j==n:
             print({i,j},end=',')
             
else:
   print("Please enter number between 2 to 12")
