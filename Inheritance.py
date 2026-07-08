#Inheritance:Inheritance is an OOP concept in which one class acquires the properties (variables) and behaviors (methods) of another class.
class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    pass
d = Dog()
d.eat()
##Pass is written because in python after declaring a class we cannot leave a class empty we have to write atleast a line of code.
#Parent class is the class which is inherited here Animal is the parent class
#Child class is the class which inherits the properties of the parent class here Dog is the child class


#When both class have constructors
class Animal:

    def __init__(self):
        print("Animal Constructor")


class Dog(Animal):

    def __init__(self):
        print("Dog Constructor")


d = Dog()
#here Dog construcot will be printed 
#To get the Animal construcot you have to use the Super() keyword
class Animal:

    def __init__(self):
        print("Animal Constructor")


class Dog(Animal):

    def __init__(self):
        super().__init__()
        print("Dog Constructor")


d = Dog()
#Super()  is the keyword to use parents class methods and constructor
#It is used when the parent class and child class have same method name
#Types of Inheritance:
#1.Single Inheritance:Oned parent-->Child
#2.Multilevel Inheritance:GrandParent-->Parent-->Child
#3.Multiple Inheritance:One child inherits from multiple parents
#4.Hierarchical Inheritance:One Parent Many children
#5.Hybrid Inheritance:Combination of two or more inheritance


##Mini Project in inheritance
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
        print("***Person Details***")
        print(self.name)
        print(self.age)
class student(person):
    def __init__(self,name,age,roll,marks):
        super().__init__(name,age)
        self.roll=roll
        self.marks=marks
    def display_student(self):
        print("***Display Student***")
        print(self.name)
        print(self.age)
        print(self.roll)
        print(self.marks)
s1=student("ccg",18,33,87)
s1.display_person()
s1.display_student()