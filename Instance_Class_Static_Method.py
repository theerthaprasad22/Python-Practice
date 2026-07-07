#Instance Method:An instance method is a method that works with the instance (object) variables. It is used to perform operations on the data of a specific object.
"""Key Points
Uses self as the first parameter.
Can access both instance variables and class variables.
Must be called using an object.
Most commonly used method in OOP."""
#Class Method:A class method is a method that works with class variables instead of object variables. It is used to modify or access data shared by all objects.
"""Key Points
Uses @classmethod decorator.
Uses cls as the first parameter.
Can access class variables directly.
Can be called using either the class or an object (calling with the class is preferred)."""
#Statiuc method:A static method is a method that does not use instance variables or class variables. It performs a general utility task related to the class.
"""Key Points
Uses @staticmethod decorator.
Does not use self or cls.
Works like a normal function placed inside a class.
Usually called using the class name."""

#Library system using all the methods
class Library:
    library_name="lpulib"
    def __init__(self,book_name,author,price):
        self.book_name=book_name
        self.author=author
        self.price=price
    def display_book(self):
        print(self.book_name)
        print(self.author)
        print(self.price)
        print(Library.library_name)
    def update_price(self,newprice):
        self.price=newprice
        print(self.price)
    @classmethod
    def change_library_name(cls,new_lib):
        Library.library_name=new_lib
        print(Library.library_name)
    @staticmethod
    def discount(price,percent):
        return price*percent/100
l1=Library("Heaven","Thee",2000)
l1.display_book()
l1.update_price(2500)
l1.change_library_name("mvlib")
l1.display_book()
print(Library.discount(2500,10))
