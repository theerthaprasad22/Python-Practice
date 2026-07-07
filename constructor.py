#A constructor is a special method that is automatically called whenever an object is created.
#init initializes an object when created
#Types of consturctor-Default Constructor
                    #-Parameterized Consturctor

##Example:
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    
    def display(self):
        print(self.title)
        print(self.author)
b1=Book("hfhf","fh")
b1.display()

    