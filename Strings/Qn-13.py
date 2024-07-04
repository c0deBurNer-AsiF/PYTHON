#write a python script to check its a palindrome or not


x=input("Enter a string:").strip()
print("Its a palindrome!")if x==x[::-1] else print("Its not a palindrome!")
