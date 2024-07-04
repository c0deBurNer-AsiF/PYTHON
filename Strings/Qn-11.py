#Write a python script to reverse a string word wise.(Example:"Asif ali sahaji" is a given string and resulting string must be "sahaji ali Asif")
x=input("Enter string:").split(" ")
print(' '.join(x[::-1]))
