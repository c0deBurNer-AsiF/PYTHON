#define a class book with instance object variables Bookid,title and price.
#initialise them via __init__() method. Also define method to show book variables 


class book:
    def __init__(self):
        self.bookid=int(input("Enter bookid:"))
        self.title=input("Enter title:")
        self.price=eval(input("Enter price:"))
    def show_book_variables(self):
        print("Bookid:",self.bookid)
        print("Title:",self.title)
        print("Price:",self.price)
'''
obj=book()
obj.show_book_variables()
'''
