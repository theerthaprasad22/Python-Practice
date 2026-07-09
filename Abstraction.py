#Abstraction is the process of hiding implementation details and showing only the essential features to the user.
#Abstaction is achieved in pythoin using  a module in python:from abc import ABC, abstractmethod
#ABC:Abstact Base class
#An abstract class is a class that cannot be instantiated (cannot create objects directly).
#An abstract method is a method that has no implementation in the parent class.
#abstract classes are meant to be inherited, not used directly.
#Creating an object of abstact class will give you error
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


d = Dog()

d.sound()
#Abstact class can have normal methods too
#Example of multiple Abstarct class
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
#Child class
class Rectangle(Shape):

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)
