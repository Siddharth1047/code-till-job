# OOP Revision

# 1. Global & Local variables
jj = 10 

def my_function():
    global jj # use the global keyword to change the global variable value
    jj = 5
    y = 9
    print(y)

my_function()
print(jj)   

# Class
class Person:
    name = "Sid"
    occupation = "Python Developer"
    bank_balance = 100 # that's low ;)

    # Method (Function in a class == Method)
    def info(self):
        print(f"{self.name} is an amazing {self.occupation}")

a = Person()
a.info()
a.name = "John"
a.occupation = "Smoker"
a.info() 
b = Person()
b.name = "Python"
b.occupation = "DaddyOfAllProgrammingLanguages"
b.info()

# Constructor [__init__()]
class Person1:
    def __init__(self, n, o):
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is an amazing {self.occ}")

aa = Person1("Sid", "PythonDev")
bb = Person1("Jenny", "Woman")
aa.info()
bb.info()

# Access Modifiers
"""
There are no access modifiers in python, all variables're public by default.
But of you really want to make a variable private use "__" before that variable name.
For protected use "_" before the variable.
"""
class Employee:
    def __init__(self):
        self.__name = "Sid"

lo = Employee()
# print(lo.__name) # now even if you call the varibale it'll not be able to execute it
# kind of a note
print(lo._Employee__name) # now you can access it. (Name Mangling in Python)

# Decorators
def greet(s):
    def relax():
        print("Good Morning")
        s()
        print("Thanks for seeing this repo")
    return relax

@greet
def hello():
    print("Hii Watcher..!!")

hello()
