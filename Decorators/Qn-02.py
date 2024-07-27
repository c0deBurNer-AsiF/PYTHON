#define a decorator to display "Happy New Year" message at the beginning.

def decor(welcome_function):
    def print_msg():
        print("Happy new year")
        welcome_function()
    return print_msg    

@decor 
def welcome():
    print("Welcome!")
#welcome()
