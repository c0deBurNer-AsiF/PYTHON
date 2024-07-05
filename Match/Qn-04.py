'''
write a python script to take one data from user and evaluate the type of data. 
is the data is of int type  then print Monday, if the data is of float type then print Tuesday, 
if the data is of complex type then print Wednesday and if the data is of type bool then print Thursday

'''             
x=eval(input("Enter any type of data(without srt):"))
match x:
    case x if type(x)==int:
        print("Monday")

    case x if type(x)==float:
        print("Tuesday")

    case x if type(x)==complex:
        print("Wednesday")

    case x if type(x)==bool:
        print("Thursday")
