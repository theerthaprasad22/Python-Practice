#Polymorphism means one interface, many forms.
#Polymorphism allows the same method, function, or operator to behave differently depending on the object or data it is working with.
#1.Method overriding:Run time,Its run type beacuse python decides which to be executed on the basis of the object
#2.Method overloading:Compile time,Same name difderent parameters,but python doesnt support it,because the first method is overwritten by the second
#We can achieve similar behaviour using default arguments
class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c


obj = Calculator()

print(obj.add(5))

print(obj.add(5, 10))

print(obj.add(5, 10, 15))

#3.Operator Overloading:SAme operators behave differently when called eg:
print(5 + 3)##Adds
print("Hello " + "World")##Concatinates

