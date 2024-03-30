#Write a python script to accept one complex number from user and display the greater number between real part and imaginary part

r=int(input("Enter the real part value:"))
i=int(input("Enter the imaginary part value"))

print("The complex number is")
print("%d+%di"%(r,i))

if r<i:
    print("Imaginary part is greater")

else:
    print("Real part is greater")
