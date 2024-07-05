'''
write a python script to make a menu driven program  in which user has to choose one of the option from four given option-
1. Odd-Even, 2.Positive-non positive, 3.Simple interest and 4. find roots of quadratic equation.
Match and execute appropriate code on user selection 
'''


print("1.Odd-Even","2.Postive-Non Positive","3.Simple Interest","4.Find roots of quadratic equation",sep="\n")
print("Select any choice as per your needs(Ex. if you want to calculate simple interest then tyoe 3:....) ")
x=int(input())
match x:


    case x if x==1:
        l_even=[]
        l_odd=[]
        for i in input("Enter numbers seprated by comma:").split(","):
            l_even.append(int(i)) if int(i)%2==0 else l_odd.append(int(i))
        print("Even numbers are:",l_even)
        print("Odd numbers are:",l_odd)
      
      
    case x if x==2:
        print("Its a positive number" if int(input("Enter a number:"))>0 else "Its a non-positive number")
      
      
    case x if x==3:
        p,r,t=int(input("Enter the principle value:")),float(input("Enter the rate of interest in '%' per annum:")),float(input("Enter the time:")) 
        print("Simple interest is:",(p*r*t)/100)


    case x if x==4:
        a,b,c=int(input("Enter the value of a:")),int(input("Enter the value of b:")),int(input("Enter the value of c:")) 
        print("Equation is\n{}x**2+{}x+{}".format(a,b,c))
        if b**2-(4*a*c)>0:
            print("Roots are real!")
        elif b**2-(4*a*c)<0:
            print("Roots are imaginary")
        else:
            print("Roots are real and Equal") 



    case _:
        print("Input out of range!!")   
