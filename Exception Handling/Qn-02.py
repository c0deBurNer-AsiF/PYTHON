#define a function to find greater value among three given data. Handle all possible exception.

def greaterBetweenThree(first,second,third):
    print(first if first>third else third if first>second else second if second>third else third) 
'''
try:
    greaterBetweenThree('asif','abir','aman')
except ValueError as e:
    print(e)

except TypeError as e:
    print(e)    

except:
    print("Value should be all in same type")        
'''


#2nd process--->>>


def greaterBetweenThree(first,second,third):
    try:
        if type(first)==type(second)==type(third):
            print('Greater value is:',first if first>third else third if first>second else second if second>third else third)
        else:
            raise TypeError("All values types should be same")
    except TypeError as e:
        print(e)
    except:
        print("Unknown Exception")
'''
greaterBetweenThree('abc','abd',2)                
'''             


#3rd process---->>


def greaterBetweenThree(first,second,third):
    try: 
        print('Greater value is:',first if first>third else third if first>second else second if second>third else third)
    except TypeError as e:
        print(e)
    except:
        print("Unknown Exception")
'''
greaterBetweenThree('abc','abd',2)                
'''
