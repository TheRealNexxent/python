#OOPS In Python.

x = 1
#1, is the object of class int!
print(type("Hello"))
#Here, Hello, is an object of the class Str!

#Basically theyre all part of classes as objects. Objects are everywhere in python!

def hello():
    print("hello")

print(type(hello)) #Here this is also object of class function!

#We will eventually move on from these BUILT IN CLASSES to make our own classes now.

# print(x + hello) # Will do nothing since both are objects of different classes and not same types.


strings = "Hi"
print(strings.upper()) #Here Upper is a method of the class str, and strings is an object.

class dog:
    def __init__(self, name, age):
        self.name = name #Attribute of class dog which is name.
        self.age = age
        print(name)
    def bark(self):
        print("Woof!")
    def meow(self):
        return "Mew!"
    def addone(self, x):
        return x+1
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
#Here we have created a class dog, and added a method, which is basically a function within a class.


d = dog("Tim", 12)
print(d.name)
d2 = dog("Bim", 13)
print(d2.name)
print(d2.age)
print(d2.get_name())
print(d2.get_age())
d.bark() #Using a method of dog. Calling on dog object.
d.meow()
d.addone(2)
#Here, I've assigned an instance of the class dog to variable a!

print(type(d)) #Will print main dog since by default the module is main.