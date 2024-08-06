#Define a python function to calculate factorial of a number. Handle all possible exceptions


class NegativeValueError(Exception):
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return self.message
        
def factorial(value):
    if value<0:
        raise NegativeValueError('Negative value dont have factorial')
    result=1
    for i in range(value,0,-1):
        result*=i
    return print("Factorial of {} is {}".format(value,result))
'''
try:
    factorial(int(input("Enter a integer number:")))
except NegativeValueError as e:
    print(e)

except TypeError as e:
    print(e)

except ValueError as e:
    print(e)
'''



#2nd type---->>


class NegativeValueError(Exception):
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return self.message
        
def factorial(value):
    try:
        if value<0:
            raise NegativeValueError("Negative Value dont have Factorial")
        elif type(value)!=int:
            raise TypeError("Value should be integer!")
        result=1
        for i in range(value,0,-1):
            result*=i
        return print("Factorial of {} is {}".format(value,result))    
        
    except NegativeValueError as e:
        print(e)

    except TypeError as e:
        print(e)       

    except:
        print("Unknown exception")

'''
factorial('abc')                    
'''
