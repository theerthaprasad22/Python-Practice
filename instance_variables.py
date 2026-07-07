##Instance Variable=Variable which is declared which is different for each object such as name of a student
##Every object have different copy
##Acess with self
##Class Variable=Variable which is declared which is same for each object such as college name for every students
##Every Objects ahve same copy
##Acess with class name


##Instance variables
##class variables
class Car:
    wheels=4
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def show(self):
        print(self.brand)
        print(self.color)
        print(Car.wheels)
c1=Car("bmw","black")
c1.show()

##Changing class variable value
class Car:
    wheels=4
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def show(self):
        print(self.brand)
        print(self.color)
        print(Car.wheels)
Car.wheels=5
c1=Car("bmw","black")
c1.show()

##Changing Class variable
class Student:
    school_name="Lovely"
    def __init__(self,roll,marks):
        self.roll=roll
        self.marks=marks
    def display(self):
        print(self.roll)
        print(self.marks)
        print(Student.school_name)
    def school(self):
        Student.school_name="KV"
s1=Student(1,99)
s1.display()
s1.school()
s1.display()
s2=Student(2,59)
s2.display()
s3=Student(3,79)
s3.display()