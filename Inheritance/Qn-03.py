#demostrate the use of super() in inheritance.

class A:
    def __init__(self):
        print("Hello")
class B(A):
    def __init__(self):
        super().__init__()
        print("Hii")
'''
obj=B()
'''
