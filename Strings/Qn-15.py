#check if a given string is only alphabet or not!


for i in input("Enter a string:"):
    if i>='a' and i<='z' or i>='A' and i<='Z':
        pass
    else:
        print("Its not a alphabet only")
        break
else:
    print("Alphabets only")    
