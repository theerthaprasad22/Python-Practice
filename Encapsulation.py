#Encapuslation is the process of combining data (variables) and methods (functions) into a single unit 
# (class) while restricting direct access to some of the object's data
#Encapsulation means wrapping data and methods together inside a class and controlling access to the data
#1.Public:A public variable or method can be accessed from anywhere.
#2.Protected:A protected member starts with one underscore.It does not stop you from acessing it give you a warning.
#3.Private:Private members start with two underscores.It prevents acsess.

#Getter:Returns the private value.
#Setter:A setter changes a private value after checking if the new value is valid.


class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)

account.withdraw(300)

print(account.get_balance())


#Getter and Setter
class Mobile:

    def __init__(self):
        self.__battery = 50

    def set_battery(self, value):

        if 0 <= value <= 100:
            self.__battery = value
        else:
            print("Invalid Battery")

    def get_battery(self):
        return self.__battery