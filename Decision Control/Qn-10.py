"""Write a python script to accept marks of five subjects from user(assuming maaximum marks is 100). display student's resuot as PASS or FAIL,
if the student in PASS then also display his percentage and division"""

ben=int(input("Enter your marks(Bengali)"))
eng=int(input("Enter your marks(English)"))
math=int(input("Enter your marks(math):"))
phy=int(input("Enter your marks(physics):"))
com=int(input("Enter your marks(computer):"))

s=float((ben+eng+math+phy+com)/5)
   
if ben>34 and eng>34 and math>34 and phy>34 and com>34:
    print("Pass")
    print("Obtained %g percentage marks"%s)
    print("Division",end=":")
    if s>74:
        print("Star marks")
        
    elif s>59 and s<75:
         print("First division")

    elif s>44 and s<60:
         print("Seceond division")

    elif s>34 and s<45:
         print("Third division")


else:
    print("Failed")
         
