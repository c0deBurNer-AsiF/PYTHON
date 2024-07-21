#to check if two given list have same elements in any order or not. Return True or False. (TSRS)

def TrueOrFalse(l1,l2):
    return sorted(l1)==sorted(l2)
#result=print(TrueOrFalse([eval(e) for e in input("Enter 1st list elements(seprated by comma):").split(",")],[eval(e) for e in input("Enter 2nd list elements(Seprated by comma:)").split(",")]))



#2nd method--->
'''
def TrueOrFalse(l1,l2):
    print('True' if set(l1)==set(l2) else 'False')
result=TrueOrFalse([eval(e) for e in input("Enter 1st list elements(seprated by comma):").split(",")],[eval(e) for e in input("Enter 2nd list elements(Seprated by comma:)").split(",")])    
'''
#3rd method--->
'''
def TrueOrFalse(l1,l2):
    return print(set(l1)==set(l2))
result=TrueOrFalse([eval(e) for e in input("Enter 1st list elements(seprated by comma):").split(",")],[eval(e) for e in input("Enter 2nd list elements(Seprated by comma:)").split(",")])
'''
