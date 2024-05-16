'''Define a class Book to store book related information like bookid,title,price,author,publisher.
define function to input,show,change price'''


class Book:

    def input(self):
        self.bookid=int(input("Enter bookid:"))
        self.title=input("Enter title:")
        self.price=int(input("enter price:"))
        self.author=input("Enter the author name:")
        self.publisher=input("Enter publisher name:")

    def show(self):
        print("Book ID:",self.bookid)
        print("Title:",self.title)
        print("Price:",self.price)
        print("Author:",self.author)
        print("Publisher:",self.publisher)

    def change_price(self):
        while True:
            try:  
               self.price=int(input("Enter your new price:"))
               break
            
            except:
                print("Price should be a number!!")


