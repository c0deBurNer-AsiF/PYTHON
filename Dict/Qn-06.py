#create a dict object where first N natural numbers are keys and their squares are data value...

print({int(e):int(e)**2 for e in range(1,int(input("Enter how many numbers squares you want to print:"))+1)})


#2nd method---->(values are inputed by user)
#print({int(e[0:e.index(":")]):int(e[e.index(":")+1::])**2 for e in input("Enter key and values like this key:value,key:value...").split(",")})
